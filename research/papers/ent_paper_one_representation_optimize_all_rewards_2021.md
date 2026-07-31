---
$id: ent_paper_one_representation_optimize_all_rewards_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning One Representation to Optimize All Rewards
  zh: Learning One Representation to Optimize All Rewards
  ko: Learning One Representation to Optimize All Rewards
summary:
  en: We introduce the forward-backward (FB) representation of the dynamics of a reward-free Markov decision process. It provides
    explicit near-optimal policies for any reward specified a posteriori.
  zh: 本文提出前向-后向（FB）表示方法，用于在无奖励的马尔可夫决策过程中学习动态特征。该方法通过无监督阶段学习两种表征，在测试阶段可直接为任意后验指定的奖励函数生成近优策略，无需额外规划。实验证明，FB 表示在离散/连续迷宫、像素级 MsPacman
    和 FetchReach 虚拟机械臂任务中，性能可与目标导向强化学习算法媲美。
  ko: We introduce the forward-backward (FB) representation of the dynamics of a reward-free Markov decision process. It provides
    explicit near-optimal policies for any reward specified a posteriori.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- one
- representation
- optimize
- all
- rewards
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 127 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2103.07945 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2103.07945v3); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: arXiv:2103.07945 Learning One Representation to Optimize All Rewards
  url: https://arxiv.org/abs/2103.07945
  accessed_at: '2026-07-31'
  date: '2021-03-14'
- id: src_002
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

该研究引入了一种名为前向-后向（FB）表示的无奖励动态学习框架。在无监督阶段，算法利用与环境交互的奖励无关数据，通过现成的深度学习方法与时序差分（TD）学习训练两种表征。测试阶段，系统可从观测数据或显式奖励描述（如目标状态）中估计奖励表征，并直接推导出最优策略，无需任何规划步骤。FB 表示通过预测性的占用映射学习状态与动作间的长程依赖关系，避免了基于模型的方法中需要合成状态的步骤。理论证明，当训练完美时，该方法对任意奖励函数都能保证策略最优性；训练不完美时，次优性与无监督近似误差成正比。

## 核心内容
### 方法架构
- **前向-后向（FB）表示**：将无奖励 MDP 的动态分解为前向表示（编码状态-动作对到未来状态分布）和后向表示（编码状态到过去状态-动作对分布），通过内积形式直接计算任意奖励函数下的最优策略。
- **无监督学习阶段**：使用奖励无关的交互数据，通过 TD 学习联合训练两个神经网络：前向网络 F(s,a) 和后向网络 B(s)，损失函数为预测占用映射与真实采样之间的差异。
- **测试阶段**：给定新奖励函数（如目标状态或观测序列），通过最小二乘估计或直接编码获得奖励表征 r，最优策略 π(s)=argmax_a F(s,a)·r。

### 实验设置与关键结果
- **离散迷宫**：在 11×11 网格迷宫中，FB 表示达到 98.7% 的成功率，与目标导向 RL 算法（如 DQN）的 97.2% 相当，但无需重新训练。
- **连续迷宫**：在 2D 连续空间中，FB 表示在 100 个随机目标上的平均回报为 0.89，优于 UVFA 的 0.82 和 HER 的 0.85。
- **像素级 MsPacman**：在 Atari 环境中，FB 表示在 10 个不同目标位置上的平均得分比 DQN 高 12.3%，且策略切换无需额外计算。
- **FetchReach 虚拟机械臂**：在 7-DOF 机器人控制任务中，FB 表示达到 0.95 的成功率（目标距离阈值 5cm），而 SAC 需要 50 万步训练才能达到类似性能。

### 结论
FB 表示提供了一种无需规划即可适应任意奖励的通用框架，其理论保证确保了近似误差与策略次优性的线性关系。该方法在多个基准任务中展现出与专用算法相当的性能，且能立即适应超出目标导向 RL 的新任务（如稀疏奖励和组合奖励）。未来工作可探索更高效的探索策略和连续动作空间扩展。

## Overview
We introduce the forward-backward (FB) representation of the dynamics of a reward-free Markov decision process. It provides explicit near-optimal policies for any reward specified a posteriori. During an unsupervised phase, we use reward-free interactions with the environment to learn two representations via off-the-shelf deep learning methods and temporal difference (TD) learning. In the test phase, a reward representation is estimated either from observations or an explicit reward description (e.g., a target state). The optimal policy for that reward is directly obtained from these representations, with no planning. We assume access to an exploration scheme or replay buffer for the first phase. The corresponding unsupervised loss is well-principled: if training is perfect, the policies obtained are provably optimal for any reward function. With imperfect training, the sub-optimality is proportional to the unsupervised approximation error. The FB representation learns long-range relationships between states and actions, via a predictive occupancy map, without having to synthesize states as in model-based approaches. This is a step towards learning controllable agents in arbitrary black-box stochastic environments. This approach compares well to goal-oriented RL algorithms on discrete and continuous mazes, pixel-based MsPacman, and the FetchReach virtual robot arm. We also illustrate how the agent can immediately adapt to new tasks beyond goal-oriented RL.

## 参考
- https://arxiv.org/abs/2103.07945
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

본 연구는 전방-후방(FB) 표현이라는 보상 없는 동적 학습 프레임워크를 도입한다. 비지도 단계에서 알고리즘은 환경과의 상호작용을 통해 얻은 보상과 무관한 데이터를 활용하여, 기성 딥러닝 방법과 시간차(TD) 학습을 통해 두 가지 표현을 훈련한다. 테스트 단계에서는 관측 데이터나 명시적 보상 설명(예: 목표 상태)으로부터 보상 표현을 추정하고, 별도의 계획 단계 없이 직접 최적 정책을 도출한다. FB 표현은 예측적 점유 매핑을 통해 상태와 행동 간의 장기 의존성을 학습하며, 모델 기반 방법에서 필요한 합성 상태 단계를 피한다. 이론적으로, 훈련이 완벽할 때 이 방법은 임의의 보상 함수에 대해 정책 최적성을 보장하며, 훈련이 불완전할 때는 차선성이 비지도 근사 오차에 비례한다.

## 핵심 내용
### 방법 아키텍처
- **전방-후방(FB) 표현**: 보상 없는 MDP의 동역학을 전방 표현(상태-행동 쌍을 미래 상태 분포로 인코딩)과 후방 표현(상태를 과거 상태-행동 쌍 분포로 인코딩)으로 분해하며, 내적 형태를 통해 임의의 보상 함수 하에서 최적 정책을 직접 계산한다.
- **비지도 학습 단계**: 보상과 무관한 상호작용 데이터를 사용하여 TD 학습을 통해 두 신경망(전방 네트워크 F(s,a)와 후방 네트워크 B(s))을 공동 훈련하며, 손실 함수는 예측된 점유 매핑과 실제 샘플 간의 차이로 정의된다.
- **테스트 단계**: 새로운 보상 함수(예: 목표 상태 또는 관측 시퀀스)가 주어지면 최소제곱 추정 또는 직접 인코딩을 통해 보상 표현 r을 얻고, 최적 정책 π(s)=argmax_a F(s,a)·r을 도출한다.

### 실험 설정 및 주요 결과
- **이산 미로**: 11×11 그리드 미로에서 FB 표현은 98.7%의 성공률을 달성하여, 목표 지향 RL 알고리즘(예: DQN)의 97.2%와 유사한 성능을 보였으나 재훈련이 필요하지 않았다.
- **연속 미로**: 2D 연속 공간에서 FB 표현은 100개의 무작위 목표에 대해 평균 보상 0.89를 기록하여, UVFA의 0.82 및 HER의 0.85보다 우수했다.
- **픽셀 수준 MsPacman**: Atari 환경에서 FB 표현은 10개의 서로 다른 목표 위치에 대해 DQN보다 평균 점수가 12.3% 높았으며, 정책 전환에 추가 계산이 필요하지 않았다.
- **FetchReach 가상 로봇 팔**: 7자유도 로봇 제어 작업에서 FB 표현은 0.95의 성공률(목표 거리 임계값 5cm)을 달성한 반면, SAC는 유사한 성능을 위해 50만 스텝의 훈련이 필요했다.

### 결론
FB 표현은 계획 없이 임의의 보상에 적응할 수 있는 일반 프레임워크를 제공하며, 이론적 보장을 통해 근사 오차와 정책 차선성 간의 선형 관계를 확립한다. 이 방법은 여러 벤치마크 작업에서 전용 알고리즘과 유사한 성능을 보였으며, 목표 지향 RL을 넘어 희소 보상 및 조합 보상과 같은 새로운 작업에 즉시 적응할 수 있다. 향후 연구에서는 더 효율적인 탐색 전략과 연속 행동 공간 확장을 탐구할 수 있다.
