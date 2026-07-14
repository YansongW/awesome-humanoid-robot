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
  zh: 本文提出了一种名为VBE（集成误差价值奖励）的即插即用探索方法，通过维护一组随机动作价值函数并使用其最大预测误差作为附加价值奖励，为强化学习提供首次访问乐观性和深度探索能力。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.12375v1.
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
Optimistic value estimates provide one mechanism for directed exploration in reinforcement learning (RL). The agent acts greedily with respect to an estimate of the value plus what can be seen as a value bonus. The value bonus can be learned by estimating a value function on reward bonuses, propagating local uncertainties around rewards. However, this approach only increases the value bonus for an action retroactively, after seeing a higher reward bonus from that state and action. Such an approach does not encourage the agent to visit a state and action for the first time. In this work, we introduce an algorithm for exploration called Value Bonuses with Ensemble errors (VBE), that maintains an ensemble of random action-value functions (RQFs). VBE uses the errors in the estimation of these RQFs to design value bonuses that provide first-visit optimism and deep exploration. The key idea is to design the rewards for these RQFs in such a way that the value bonus can decrease to zero. We show that VBE outperforms Bootstrap DQN and two reward bonus approaches (RND and ACB) on several classic environments used to test exploration and provide demonstrative experiments that it can scale easily to more complex environments like Atari.

## 核心内容
Optimistic value estimates provide one mechanism for directed exploration in reinforcement learning (RL). The agent acts greedily with respect to an estimate of the value plus what can be seen as a value bonus. The value bonus can be learned by estimating a value function on reward bonuses, propagating local uncertainties around rewards. However, this approach only increases the value bonus for an action retroactively, after seeing a higher reward bonus from that state and action. Such an approach does not encourage the agent to visit a state and action for the first time. In this work, we introduce an algorithm for exploration called Value Bonuses with Ensemble errors (VBE), that maintains an ensemble of random action-value functions (RQFs). VBE uses the errors in the estimation of these RQFs to design value bonuses that provide first-visit optimism and deep exploration. The key idea is to design the rewards for these RQFs in such a way that the value bonus can decrease to zero. We show that VBE outperforms Bootstrap DQN and two reward bonus approaches (RND and ACB) on several classic environments used to test exploration and provide demonstrative experiments that it can scale easily to more complex environments like Atari.

## 参考
- http://arxiv.org/abs/2602.12375v1

