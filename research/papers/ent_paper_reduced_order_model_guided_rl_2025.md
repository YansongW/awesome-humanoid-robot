---
$id: ent_paper_reduced_order_model_guided_rl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
  zh: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
  ko: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
summary:
  en: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  zh: Reduced-Order Model-Guided RL (ROM-GRL) 是2025年提出的一种无需运动捕捉数据或复杂奖励塑形的人形机器人行走强化学习框架。该方法通过两阶段训练：先训练一个4自由度降阶模型生成节能步态模板，再引导全自由度策略学习，在1米/秒和4米/秒速度下均实现稳定对称步态，跟踪误差显著低于纯奖励基线。
  ko: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- reduced_order_model_guided_rl
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19023v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2509.19023
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ROM-GRL 由两个阶段构成：第一阶段使用Proximal Policy Optimization训练一个紧凑的4自由度降阶模型，生成能量高效的步态模板；第二阶段利用Soft Actor-Critic算法结合对抗判别器，使全自由度策略的五维步态特征分布与降阶模型示范相匹配。实验表明，在1米/秒和4米/秒速度下，该方法产生的步态稳定对称，跟踪误差远低于纯奖励基线。该框架通过将轻量级降阶模型指导蒸馏到高维策略中，弥合了纯奖励方法与模仿学习方法之间的差距，无需任何人类示范即可实现多样化的自然类人行为。

## 核心内容
### 方法架构
- **两阶段框架**：第一阶段训练4自由度降阶模型（ROM）生成步态模板；第二阶段使用Soft Actor-Critic算法结合对抗判别器，将ROM的示范蒸馏到全自由度策略中。
- **降阶模型**：仅包含4个自由度，通过Proximal Policy Optimization训练，生成能量高效的步态轨迹。
- **全自由度策略**：使用Soft Actor-Critic算法训练，并通过对抗判别器确保其五维步态特征分布与ROM示范匹配。

### 实验设置
- **速度条件**：在1米/秒和4米/秒两种速度下进行测试。
- **基线对比**：与纯奖励方法（pure-reward baseline）进行对比。

### 关键结果
- **步态质量**：ROM-GRL产生的步态稳定对称，跟踪误差显著低于纯奖励基线。
- **速度适应性**：在1米/秒和4米/秒速度下均表现良好，验证了方法的鲁棒性。

### 结论
ROM-GRL通过将轻量级降阶模型指导蒸馏到高维策略中，成功弥合了纯奖励方法与模仿学习方法之间的差距，无需任何人类示范即可实现多样化的自然类人行走行为。

## Overview
We introduce Reduced-Order Model-Guided Reinforcement Learning (ROM-GRL), a two-stage reinforcement learning framework for humanoid walking that requires no motion capture data or elaborate reward shaping. In the first stage, a compact 4-DOF (four-degree-of-freedom) reduced-order model (ROM) is trained via Proximal Policy Optimization. This generates energy-efficient gait templates. In the second stage, those dynamically consistent trajectories guide a full-body policy trained with Soft Actor--Critic augmented by an adversarial discriminator, ensuring the student's five-dimensional gait feature distribution matches the ROM's demonstrations. Experiments at 1 meter-per-second and 4 meter-per-second show that ROM-GRL produces stable, symmetric gaits with substantially lower tracking error than a pure-reward baseline. By distilling lightweight ROM guidance into high-dimensional policies, ROM-GRL bridges the gap between reward-only and imitation-based locomotion methods, enabling versatile, naturalistic humanoid behaviors without any human demonstrations.

## 개요
우리는 ROM-GRL(Reduced-Order Model-Guided Reinforcement Learning)을 소개합니다. 이는 모션 캡처 데이터나 복잡한 보상 설계 없이 인간형 보행을 구현하는 2단계 강화 학습 프레임워크입니다. 첫 번째 단계에서는 PPO(Proximal Policy Optimization)를 통해 간결한 4자유도(4-DOF) 축소 차수 모델(ROM)을 훈련합니다. 이를 통해 에너지 효율적인 보행 템플릿을 생성합니다. 두 번째 단계에서는 이러한 동적으로 일관된 궤적이 적대적 판별기로 보강된 SAC(Soft Actor-Critic)로 훈련된 전신 정책을 안내하여, 학생 모델의 5차원 보행 특징 분포가 ROM의 시연과 일치하도록 보장합니다. 1m/s 및 4m/s 속도에서의 실험 결과, ROM-GRL은 순수 보상 기반 기준선보다 현저히 낮은 추적 오차로 안정적이고 대칭적인 보행을 생성합니다. 가벼운 ROM 안내를 고차원 정책으로 증류함으로써, ROM-GRL은 보상 전용 방법과 모방 기반 보행 방법 간의 격차를 해소하여 인간 시연 없이도 다양하고 자연스러운 인간형 행동을 가능하게 합니다.

## 핵심 내용
우리는 ROM-GRL(Reduced-Order Model-Guided Reinforcement Learning)을 소개합니다. 이는 모션 캡처 데이터나 복잡한 보상 설계 없이 인간형 보행을 구현하는 2단계 강화 학습 프레임워크입니다. 첫 번째 단계에서는 PPO(Proximal Policy Optimization)를 통해 간결한 4자유도(4-DOF) 축소 차수 모델(ROM)을 훈련합니다. 이를 통해 에너지 효율적인 보행 템플릿을 생성합니다. 두 번째 단계에서는 이러한 동적으로 일관된 궤적이 적대적 판별기로 보강된 SAC(Soft Actor-Critic)로 훈련된 전신 정책을 안내하여, 학생 모델의 5차원 보행 특징 분포가 ROM의 시연과 일치하도록 보장합니다. 1m/s 및 4m/s 속도에서의 실험 결과, ROM-GRL은 순수 보상 기반 기준선보다 현저히 낮은 추적 오차로 안정적이고 대칭적인 보행을 생성합니다. 가벼운 ROM 안내를 고차원 정책으로 증류함으로써, ROM-GRL은 보상 전용 방법과 모방 기반 보행 방법 간의 격차를 해소하여 인간 시연 없이도 다양하고 자연스러운 인간형 행동을 가능하게 합니다.

## 参考
- http://arxiv.org/abs/2509.19023v1
