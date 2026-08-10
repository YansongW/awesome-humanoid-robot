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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.11388v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (780 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.11388v1

## 개요
고전 강화학습 방법은 고차원 복잡한 환경에서 파라미터 규모가 과도하게 커지고 무작위성 문제로 인해 성능이 저조한 경우가 많습니다. 본 연구는 처음으로 양자 심층 강화학습(QDRL)을 휴머노이드 로봇 분야에 도입하여, 파라미터화된 양자 회로를 활용해 고차원 상태 공간을 처리하고 전통적인 지도 구축 및 경로 계획 과정을 우회합니다. MuJoCo의 Humanoid-v4 및 Walker2d-v4 벤치마크에서 양자 SAC 알고리즘은 평균 보상(246.40)에서 고전 SAC(228.36)를 8% 초과 달성했으며, 동시에 훈련 스텝 수를 92% 줄여 양자 계산이 강화학습 가속화에 지닌 잠재력을 입증했습니다.

## 핵심 내용
### 방법
- **파라미터화된 양자 회로(PQC)**를 사용하여 하이브리드 양자-고전 아키텍처를 구축하고, 고차원 관측 공간을 직접 처리하며 전통적인 내비게이션의 명시적 지도 구축 및 경로 계획을 필요로 하지 않습니다.
- 고전 **Soft Actor-Critic (SAC)** 알고리즘의 정책 네트워크와 가치 네트워크를 양자 회로 버전으로 대체하여 양자 SAC(Quantum SAC)를 형성합니다.

### 실험 설정
- 환경: MuJoCo 물리 엔진의 **Humanoid-v4** 및 **Walker2d-v4**를 사용하며, 둘 다 대규모 관측 공간(376차원)과 행동 공간(17차원)을 가집니다.
- 비교 기준: 고전 SAC 알고리즘(완전 연결 신경망 아키텍처).
- 훈련 구성: 양자 회로 레이어 수, 학습률 등의 하이퍼파라미터는 그리드 서치를 통해 최적화되어 공정한 비교를 보장합니다.

### 주요 결과
- **평균 보상**: 양자 SAC는 **246.40**에 도달했고, 고전 SAC는 **228.36**으로 **8%** 향상되었습니다.
- **훈련 효율성**: 양자 SAC는 **92% 더 적은 훈련 스텝 수**로 수렴하여 샘플 복잡도를 크게 낮췄습니다.
- 절제 실험에 따르면 양자 회로 레이어 수가 3개로 증가할 때 성능이 최적이며, 이 깊이를 초과하면 그래디언트 소실 현상이 나타납니다.

### 결론
- 양자 심층 강화학습은 휴머노이드 로봇 내비게이션 작업에서 처음으로 유효성을 검증했으며, 특히 학습 가속화와 최종 성능 향상 측면에서 두드러집니다.
- 현재 한계: 양자 회로 시뮬레이션은 고전 컴퓨터의 시뮬레이션 오버헤드에 제한되며, 향후 실제 양자 하드웨어에서 확장성을 검증해야 합니다.
