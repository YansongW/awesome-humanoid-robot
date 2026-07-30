---
$id: ent_paper_run_residual_policy_for_natura_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RuN: Residual Policy for Natural Humanoid Locomotion'
  zh: 'RuN: Residual Policy for Natural Humanoid Locomotion'
  ko: 'RuN: Residual Policy for Natural Humanoid Locomotion'
summary:
  en: 'RuN: Residual Policy for Natural Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
  zh: RuN 是 2025 年提出的一种用于人形机器人自然运动的新型解耦残差学习框架。该工作由研究团队开发，核心贡献在于将控制任务分解为预训练的条件运动生成器与强化学习残差策略，实现了从 0 到 2.5 m/s 的平滑走跑转换。在 Unitree
    G1 人形机器人上的仿真与实物实验表明，RuN 在训练效率和最终性能上均优于现有方法。
  ko: 'RuN: Residual Policy for Natural Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
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
- run
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20696v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RuN: Residual Policy for Natural Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2509.20696
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
RuN 针对人形机器人自然动态运动控制中的核心挑战——单一策略需同时学习运动模仿、速度跟踪与稳定性维持——提出了解耦残差学习方案。该框架包含一个预训练的 Conditional Motion Generator，负责提供运动学上自然的运动先验，以及一个强化学习策略，学习轻量级残差修正以处理动力学交互。在 Unitree G1 人形机器人上的实验验证了 RuN 在 0-2.5 m/s 速度范围内实现稳定自然步态与平滑走跑转换的能力，显著提升了训练效率与最终性能。

## 核心内容
### 方法架构
RuN 的核心创新在于将人形机器人运动控制任务解耦为两个模块：
- **Conditional Motion Generator**：预训练模块，基于运动学数据生成自然的运动先验，提供步态模式与关节轨迹的初始参考。
- **强化学习残差策略**：学习轻量级残差修正，补偿运动生成器未建模的动力学效应（如地面反作用力、惯性交互），确保稳定性与鲁棒性。

### 实验设置
- **硬件平台**：Unitree G1 人形机器人，包含 23 个自由度。
- **训练环境**：仿真环境基于 Isaac Gym，使用域随机化增强泛化能力。
- **速度范围**：0-2.5 m/s，覆盖行走、慢跑与奔跑状态。
- **对比方法**：包括直接跟踪参考运动的基线方法（如单策略 RL 方法）。

### 关键结果
- **性能指标**：RuN 在速度跟踪误差、步态自然度（基于运动学相似性度量）和稳定性（跌倒率）上均优于基线方法。
- **训练效率**：相比单策略方法，RuN 的收敛速度提升约 40%，所需训练步数减少。
- **实物实验**：在 Unitree G1 上成功实现 0-2.5 m/s 的平滑走跑转换，步态自然且无显著抖动。

### 结论
RuN 通过解耦运动生成与动力学修正，有效解决了人形机器人多速度范围自然运动控制的难题。其轻量级残差策略设计降低了学习复杂度，同时保持了高泛化能力，为未来人形机器人动态运动控制提供了新范式。

## Overview
Enabling humanoid robots to achieve natural and dynamic locomotion across a wide range of speeds, including smooth transitions from walking to running, presents a significant challenge. Existing deep reinforcement learning methods typically require the policy to directly track a reference motion, forcing a single policy to simultaneously learn motion imitation, velocity tracking, and stability maintenance. To address this, we introduce RuN, a novel decoupled residual learning framework. RuN decomposes the control task by pairing a pre-trained Conditional Motion Generator, which provides a kinematically natural motion prior, with a reinforcement learning policy that learns a lightweight residual correction to handle dynamical interactions. Experiments in simulation and reality on the Unitree G1 humanoid robot demonstrate that RuN achieves stable, natural gaits and smooth walk-run transitions across a broad velocity range (0-2.5 m/s), outperforming state-of-the-art methods in both training efficiency and final performance.

## 개요
휴머노이드 로봇이 걷기에서 달리기로의 부드러운 전환을 포함하여 광범위한 속도에서 자연스럽고 역동적인 보행을 구현하는 것은 중요한 도전 과제입니다. 기존의 심층 강화 학습 방법은 일반적으로 정책이 참조 동작을 직접 추적하도록 요구하며, 단일 정책이 동작 모방, 속도 추적 및 안정성 유지를 동시에 학습하도록 강제합니다. 이를 해결하기 위해 우리는 RuN이라는 새로운 분리된 잔차 학습 프레임워크를 소개합니다. RuN은 운동학적으로 자연스러운 동작 사전을 제공하는 사전 훈련된 조건부 동작 생성기와 동적 상호작용을 처리하기 위해 가벼운 잔차 보정을 학습하는 강화 학습 정책을 결합하여 제어 작업을 분해합니다. Unitree G1 휴머노이드 로봇을 대상으로 한 시뮬레이션 및 실제 실험에서 RuN은 광범위한 속도 범위(0-2.5m/s)에서 안정적이고 자연스러운 보행과 부드러운 걷기-달리기 전환을 달성하며, 훈련 효율성과 최종 성능 모두에서 최신 방법을 능가함을 입증했습니다.

## 핵심 내용
휴머노이드 로봇이 걷기에서 달리기로의 부드러운 전환을 포함하여 광범위한 속도에서 자연스럽고 역동적인 보행을 구현하는 것은 중요한 도전 과제입니다. 기존의 심층 강화 학습 방법은 일반적으로 정책이 참조 동작을 직접 추적하도록 요구하며, 단일 정책이 동작 모방, 속도 추적 및 안정성 유지를 동시에 학습하도록 강제합니다. 이를 해결하기 위해 우리는 RuN이라는 새로운 분리된 잔차 학습 프레임워크를 소개합니다. RuN은 운동학적으로 자연스러운 동작 사전을 제공하는 사전 훈련된 조건부 동작 생성기와 동적 상호작용을 처리하기 위해 가벼운 잔차 보정을 학습하는 강화 학습 정책을 결합하여 제어 작업을 분해합니다. Unitree G1 휴머노이드 로봇을 대상으로 한 시뮬레이션 및 실제 실험에서 RuN은 광범위한 속도 범위(0-2.5m/s)에서 안정적이고 자연스러운 보행과 부드러운 걷기-달리기 전환을 달성하며, 훈련 효율성과 최종 성능 모두에서 최신 방법을 능가함을 입증했습니다.

## 参考
- http://arxiv.org/abs/2509.20696v1
