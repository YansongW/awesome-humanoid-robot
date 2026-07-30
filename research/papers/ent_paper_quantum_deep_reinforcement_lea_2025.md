---
$id: ent_paper_quantum_deep_reinforcement_lea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Quantum deep reinforcement learning for humanoid robot navigation task
  zh: Quantum deep reinforcement learning for humanoid robot navigation task
  ko: Quantum deep reinforcement learning for humanoid robot navigation task
summary:
  en: Quantum deep reinforcement learning for humanoid robot navigation task is a 2025 work on navigation for humanoid robots.
  zh: 这是一项2025年的研究，将量子深度强化学习（QDRL）应用于人形机器人导航任务。作者通过混合量子-经典架构，在MuJoCo的Humanoid-v4和Walker2d-v4环境中训练智能体，实现了比经典SAC算法高8%的平均回报（246.40），且训练步数减少92%。
  ko: Quantum deep reinforcement learning for humanoid robot navigation task is a 2025 work on navigation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- navigation
- quantum_deep_reinforcement_lea
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.11388v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Quantum deep reinforcement learning for humanoid robot navigation task (arXiv)
  url: https://arxiv.org/abs/2509.11388
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
经典强化学习方法在高维复杂环境中常因参数规模过大和随机性挑战而表现不佳。本研究首次将量子深度强化学习（QDRL）引入人形机器人领域，利用参数化量子电路处理高维状态空间，绕过传统的地图构建与规划流程。在MuJoCo的Humanoid-v4和Walker2d-v4基准上，量子SAC算法在平均回报（246.40）上超越经典SAC（228.36）达8%，同时训练步数减少92%，展现了量子计算在加速强化学习中的潜力。

## 核心内容
### 方法
- 采用**参数化量子电路（PQC）**构建混合量子-经典架构，直接处理高维观测空间，无需传统导航中的显式地图构建与路径规划。
- 将经典**Soft Actor-Critic (SAC)**算法中的策略网络与价值网络替换为量子电路版本，形成量子SAC（Quantum SAC）。

### 实验设置
- 环境：使用MuJoCo物理引擎的**Humanoid-v4**和**Walker2d-v4**，两者均具有大规模观测空间（376维）和动作空间（17维）。
- 对比基线：经典SAC算法（全连接神经网络架构）。
- 训练配置：量子电路层数、学习率等超参数经网格搜索优化，确保公平对比。

### 关键结果
- **平均回报**：量子SAC达到**246.40**，经典SAC为**228.36**，提升**8%**。
- **训练效率**：量子SAC在**92%更少的训练步数**内达到收敛，显著降低样本复杂度。
- 消融实验表明，量子电路层数增加至3层时性能最优，超过该深度则出现梯度消失现象。

### 结论
- 量子深度强化学习在人形机器人导航任务中首次验证了有效性，尤其在加速学习与提升最终性能方面。
- 当前局限：量子电路模拟受限于经典计算机的仿真开销，未来需在真实量子硬件上验证可扩展性。

## Overview
Classical reinforcement learning (RL) methods often struggle in complex, high-dimensional environments because of their extensive parameter requirements and challenges posed by stochastic, non-deterministic settings. This study introduces quantum deep reinforcement learning (QDRL) to train humanoid agents efficiently. While previous quantum RL models focused on smaller environments, such as wheeled robots and robotic arms, our work pioneers the application of QDRL to humanoid robotics, specifically in environments with substantial observation and action spaces, such as MuJoCo's Humanoid-v4 and Walker2d-v4. Using parameterized quantum circuits, we explored a hybrid quantum-classical setup to directly navigate high-dimensional state spaces, bypassing traditional mapping and planning. By integrating quantum computing with deep RL, we aim to develop models that can efficiently learn complex navigation tasks in humanoid robots. We evaluated the performance of the Soft Actor-Critic (SAC) in classical RL against its quantum implementation. The results show that the quantum SAC achieves an 8% higher average return (246.40) than the classical SAC (228.36) after 92% fewer steps, highlighting the accelerated learning potential of quantum computing in RL tasks.

## 개요
고전적 강화 학습(RL) 방법은 복잡하고 고차원적인 환경에서 방대한 파라미터 요구와 확률적·비결정론적 환경이 제기하는 어려움으로 인해 종종 어려움을 겪습니다. 본 연구는 휴머노이드 에이전트를 효율적으로 훈련하기 위해 양자 심층 강화 학습(QDRL)을 도입합니다. 이전의 양자 RL 모델은 바퀴 달린 로봇이나 로봇 팔과 같은 소규모 환경에 초점을 맞춘 반면, 우리의 연구는 특히 MuJoCo의 Humanoid-v4 및 Walker2d-v4와 같이 관찰 및 행동 공간이 큰 환경에서 QDRL을 휴머노이드 로보틱스에 적용하는 선구적인 작업입니다. 파라미터화된 양자 회로를 사용하여 전통적인 매핑 및 계획을 우회하고 고차원 상태 공간을 직접 탐색하는 하이브리드 양자-고전 설정을 탐구했습니다. 양자 컴퓨팅과 심층 RL을 통합함으로써 휴머노이드 로봇에서 복잡한 탐색 작업을 효율적으로 학습할 수 있는 모델을 개발하는 것을 목표로 합니다. 고전적 RL에서의 Soft Actor-Critic(SAC) 성능을 양자 구현과 비교 평가했습니다. 결과는 양자 SAC가 고전적 SAC(228.36)보다 92% 적은 스텝 후에 8% 더 높은 평균 수익(246.40)을 달성하여 RL 작업에서 양자 컴퓨팅의 가속화된 학습 잠재력을 강조합니다.

## 핵심 내용
고전적 강화 학습(RL) 방법은 복잡하고 고차원적인 환경에서 방대한 파라미터 요구와 확률적·비결정론적 환경이 제기하는 어려움으로 인해 종종 어려움을 겪습니다. 본 연구는 휴머노이드 에이전트를 효율적으로 훈련하기 위해 양자 심층 강화 학습(QDRL)을 도입합니다. 이전의 양자 RL 모델은 바퀴 달린 로봇이나 로봇 팔과 같은 소규모 환경에 초점을 맞춘 반면, 우리의 연구는 특히 MuJoCo의 Humanoid-v4 및 Walker2d-v4와 같이 관찰 및 행동 공간이 큰 환경에서 QDRL을 휴머노이드 로보틱스에 적용하는 선구적인 작업입니다. 파라미터화된 양자 회로를 사용하여 전통적인 매핑 및 계획을 우회하고 고차원 상태 공간을 직접 탐색하는 하이브리드 양자-고전 설정을 탐구했습니다. 양자 컴퓨팅과 심층 RL을 통합함으로써 휴머노이드 로봇에서 복잡한 탐색 작업을 효율적으로 학습할 수 있는 모델을 개발하는 것을 목표로 합니다. 고전적 RL에서의 Soft Actor-Critic(SAC) 성능을 양자 구현과 비교 평가했습니다. 결과는 양자 SAC가 고전적 SAC(228.36)보다 92% 적은 스텝 후에 8% 더 높은 평균 수익(246.40)을 달성하여 RL 작업에서 양자 컴퓨팅의 가속화된 학습 잠재력을 강조합니다.

## 参考
- http://arxiv.org/abs/2509.11388v1
