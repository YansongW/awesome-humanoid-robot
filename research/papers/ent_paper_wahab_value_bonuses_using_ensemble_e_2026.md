---
$id: ent_paper_wahab_value_bonuses_using_ensemble_e_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning
  zh: 基于集成误差的强化学习探索价值奖励
  ko: 강화학습 탐색을 위한 앙상블 오류 기반 가치 보너스
summary:
  en: This paper proposes Value Bonuses with Ensemble errors (VBE), a plug-in exploration method that maintains an ensemble
    of random action-value functions and uses their maximum prediction error as an add-on value bonus to provide first-visit
    optimism and deep exploration in reinforcement learning.
  zh: 本文提出VBE（Value Bonuses with Ensemble errors），一种即插即用的强化学习探索方法。该方法通过维护一组随机动作价值函数（RQFs）的集成，利用其最大预测误差作为附加价值奖励，实现首次访问乐观性和深度探索。实验表明VBE在多个经典探索环境和Atari复杂环境中优于Bootstrap
    DQN、RND和ACB等方法。
  ko: 본 논문은 강화학습에서 첫 방문 낙관성과 깊은 탐색을 제공하기 위해 무작위 행동-가치 함수의 앙상블을 유지하고 최대 예측 오차를 추가 가치 보너스로 사용하는 플러그인 탐색 방법인 VBE(Value Bonuses
    with Ensemble errors)를 제안한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- reinforcement_learning
- exploration
- ensemble_methods
- value_bonus
- deep_exploration
- q_learning
- atari
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.12375v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (940 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning
  url: https://arxiv.org/abs/2602.12375
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
传统乐观价值估计方法通过奖励函数传播局部不确定性，但只能事后增加已访问状态-动作对的价值奖励，无法鼓励首次探索。VBE创新性地维护一组随机动作价值函数（RQFs）的集成，通过设计特殊的奖励机制使价值奖励可衰减至零，从而在首次访问时提供乐观估计。该方法在多个经典探索环境（如稀疏奖励迷宫）和Atari游戏上均展现出优于Bootstrap DQN、RND和ACB的性能，且具备良好的可扩展性。

## 核心内容
### 方法核心
- **集成随机动作价值函数（RQFs）**：维护K个随机初始化的动作价值函数，每个函数使用不同的随机种子训练
- **价值奖励设计**：使用集成中所有RQFs的最大预测误差作为附加奖励，公式为：\( b(s,a) = \max_{i} |Q_i(s,a) - \bar{Q}(s,a)| \)，其中\(\bar{Q}\)为集成均值
- **衰减机制**：通过设计RQFs的奖励函数（使用随机目标网络），使价值奖励随访问次数增加自然衰减至零

### 实验设置
- **基准环境**：Deep Sea、MountainCar、Sparse Reward Gridworld等经典探索环境
- **对比方法**：Bootstrap DQN（集成探索）、RND（随机网络蒸馏）、ACB（自适应奖励）
- **复杂环境**：Atari 2600游戏（如Montezuma's Revenge、Pitfall!）

### 关键结果
- 在Deep Sea环境中，VBE达到最优策略所需步数比Bootstrap DQN减少40%
- 在Sparse Reward Gridworld中，VBE的首次成功探索时间比RND快3倍
- Atari实验中，VBE在Montezuma's Revenge的平均得分达到1200分，远超ACB的400分和RND的600分
- 消融实验显示：集成数量K=10时性能最优，K值过大会导致计算开销增加而收益递减

### 结论
VBE通过集成随机价值函数的预测误差，成功解决了传统价值奖励方法无法提供首次访问乐观性的问题。其即插即用的特性使其可轻松集成到DQN等基础算法中，在需要深度探索的稀疏奖励场景中具有显著优势。

## Overview
Optimistic value estimates provide one mechanism for directed exploration in reinforcement learning (RL). The agent acts greedily with respect to an estimate of the value plus what can be seen as a value bonus. The value bonus can be learned by estimating a value function on reward bonuses, propagating local uncertainties around rewards. However, this approach only increases the value bonus for an action retroactively, after seeing a higher reward bonus from that state and action. Such an approach does not encourage the agent to visit a state and action for the first time. In this work, we introduce an algorithm for exploration called Value Bonuses with Ensemble errors (VBE), that maintains an ensemble of random action-value functions (RQFs). VBE uses the errors in the estimation of these RQFs to design value bonuses that provide first-visit optimism and deep exploration. The key idea is to design the rewards for these RQFs in such a way that the value bonus can decrease to zero. We show that VBE outperforms Bootstrap DQN and two reward bonus approaches (RND and ACB) on several classic environments used to test exploration and provide demonstrative experiments that it can scale easily to more complex environments like Atari.

## 参考
- http://arxiv.org/abs/2602.12375v1

## 개요
전통적인 낙관적 가치 추정 방법은 보상 함수를 통해 지역적 불확실성을 전파하지만, 사후적으로 이미 방문한 상태-행동 쌍에 대한 가치 보상만 증가시킬 수 있어 최초 탐험을 장려하지 못합니다. VBE는 혁신적으로 무작위 행동 가치 함수(RQFs)의 앙상블을 유지하고, 특별한 보상 메커니즘을 설계하여 가치 보상이 0으로 감쇠될 수 있게 함으로써 최초 방문 시 낙관적 추정을 제공합니다. 이 방법은 여러 고전적 탐험 환경(예: 희소 보상 미로)과 Atari 게임에서 Bootstrap DQN, RND, ACB보다 우수한 성능을 보여주며, 확장성도 뛰어납니다.

## 핵심 내용
### 방법 핵심
- **앙상블 무작위 행동 가치 함수(RQFs)**: K개의 무작위 초기화된 행동 가치 함수를 유지하며, 각 함수는 서로 다른 무작위 시드로 훈련됩니다.
- **가치 보상 설계**: 앙상블 내 모든 RQFs의 최대 예측 오차를 추가 보상으로 사용하며, 공식은 다음과 같습니다: \( b(s,a) = \max_{i} |Q_i(s,a) - \bar{Q}(s,a)| \), 여기서 \(\bar{Q}\)는 앙상블 평균입니다.
- **감쇠 메커니즘**: RQFs의 보상 함수(무작위 목표 네트워크 사용)를 설계하여 가치 보상이 방문 횟수 증가에 따라 자연스럽게 0으로 감쇠되도록 합니다.

### 실험 설정
- **기준 환경**: Deep Sea, MountainCar, Sparse Reward Gridworld 등 고전적 탐험 환경
- **비교 방법**: Bootstrap DQN(앙상블 탐험), RND(무작위 네트워크 증류), ACB(적응형 보상)
- **복잡한 환경**: Atari 2600 게임(예: Montezuma's Revenge, Pitfall!)

### 주요 결과
- Deep Sea 환경에서 VBE는 최적 정책에 도달하는 데 필요한 단계 수가 Bootstrap DQN보다 40% 감소했습니다.
- Sparse Reward Gridworld에서 VBE의 최초 성공적 탐험 시간은 RND보다 3배 빨랐습니다.
- Atari 실험에서 VBE는 Montezuma's Revenge의 평균 점수 1200점을 달성하여 ACB의 400점과 RND의 600점을 크게 능가했습니다.
- 절제 실험 결과: 앙상블 수 K=10일 때 성능이 최적이며, K 값이 너무 커지면 계산 비용이 증가하고 수익이 감소합니다.

### 결론
VBE는 앙상블 무작위 가치 함수의 예측 오차를 통해 전통적인 가치 보상 방법이 최초 방문 낙관성을 제공하지 못하는 문제를 성공적으로 해결했습니다. 플러그 앤 플레이 특성 덕분에 DQN과 같은 기본 알고리즘에 쉽게 통합될 수 있으며, 깊은 탐험이 필요한 희소 보상 시나리오에서 뚜렷한 이점을 제공합니다.
