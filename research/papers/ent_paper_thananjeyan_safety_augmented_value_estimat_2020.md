---
$id: ent_paper_thananjeyan_safety_augmented_value_estimat_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Safety Augmented Value Estimation from Demonstrations (SAVED): Safe Deep Model-Based RL for Sparse Cost Robotic Tasks'
  zh: 基于演示的安全增强价值估计（SAVED）：面向稀疏代价机器人任务的安全深度模型强化学习
  ko: '시연으로부터의 안전 강화 가치 추정(SAVED): 희소 비용 로봇 작업을 위한 안전한 심층 모델 기반 강화학습'
summary:
  en: SAVED is a deep model-based reinforcement learning algorithm that uses sparse task-completion supervision and a modest
    set of suboptimal demonstrations, together with a learned value function, a kernel-density safe set, and probabilistic
    chance constraints over an ensemble dynamics model, to safely and efficiently learn robotic control tasks.
  zh: SAVED是一种深度模型强化学习算法，仅利用稀疏的任务完成监督信号和少量次优演示，结合学习到的价值函数、核密度安全集以及集成动力学模型上的概率机会约束，安全且高效地学习机器人控制任务。
  ko: SAVED는 희소한 작업 완료 감독 신호와 소량의 비최적 시연, 학습된 가치 함수, 커널 밀도 안전 집합, 그리고 앙상블 동역학 모델 기반 확률적 기회 제약을 활용하여 로봇 제어 작업을 안전하고 효율적으로 학습하는
    알고리즘이다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- safe_reinforcement_learning
- model_based_rl
- deep_model_predictive_control
- sparse_rewards
- chance_constraints
- safe_set
- kernel_density_estimation
- demonstration_guided_learning
- sample_efficient_rl
- robotic_manipulation
- surgical_robotics
- da_vinci_research_kit
- pr2_robot
- fetch_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1905.13402v8.
sources:
- id: src_001
  type: paper
  title: 'Safety Augmented Value Estimation from Demonstrations (SAVED): Safe Deep Model-Based RL for Sparse Cost Robotic
    Tasks'
  url: https://arxiv.org/abs/1905.13402
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Reinforcement learning (RL) for robotics is challenging due to the difficulty in hand-engineering a dense cost function, which can lead to unintended behavior, and dynamical uncertainty, which makes exploration and constraint satisfaction challenging. We address these issues with a new model-based reinforcement learning algorithm, Safety Augmented Value Estimation from Demonstrations (SAVED), which uses supervision that only identifies task completion and a modest set of suboptimal demonstrations to constrain exploration and learn efficiently while handling complex constraints. We then compare SAVED with 3 state-of-the-art model-based and model-free RL algorithms on 6 standard simulation benchmarks involving navigation and manipulation and a physical knot-tying task on the da Vinci surgical robot. Results suggest that SAVED outperforms prior methods in terms of success rate, constraint satisfaction, and sample efficiency, making it feasible to safely learn a control policy directly on a real robot in less than an hour. For tasks on the robot, baselines succeed less than 5% of the time while SAVED has a success rate of over 75% in the first 50 training iterations. Code and supplementary material is available at https://tinyurl.com/saved-rl.

## 核心内容
Reinforcement learning (RL) for robotics is challenging due to the difficulty in hand-engineering a dense cost function, which can lead to unintended behavior, and dynamical uncertainty, which makes exploration and constraint satisfaction challenging. We address these issues with a new model-based reinforcement learning algorithm, Safety Augmented Value Estimation from Demonstrations (SAVED), which uses supervision that only identifies task completion and a modest set of suboptimal demonstrations to constrain exploration and learn efficiently while handling complex constraints. We then compare SAVED with 3 state-of-the-art model-based and model-free RL algorithms on 6 standard simulation benchmarks involving navigation and manipulation and a physical knot-tying task on the da Vinci surgical robot. Results suggest that SAVED outperforms prior methods in terms of success rate, constraint satisfaction, and sample efficiency, making it feasible to safely learn a control policy directly on a real robot in less than an hour. For tasks on the robot, baselines succeed less than 5% of the time while SAVED has a success rate of over 75% in the first 50 training iterations. Code and supplementary material is available at https://tinyurl.com/saved-rl.

## 参考
- http://arxiv.org/abs/1905.13402v8

