---
$id: ent_paper_thananjeyan_safety_augmented_value_estimat_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Safety Augmented Value Estimation from Demonstrations (SAVED): Safe Deep Model-Based
    RL for Sparse Cost Robotic Tasks'
  zh: 基于演示的安全增强价值估计（SAVED）：面向稀疏代价机器人任务的安全深度模型强化学习
  ko: '시연으로부터의 안전 강화 가치 추정(SAVED): 희소 비용 로봇 작업을 위한 안전한 심층 모델 기반 강화학습'
summary:
  en: SAVED is a deep model-based reinforcement learning algorithm that uses sparse
    task-completion supervision and a modest set of suboptimal demonstrations, together
    with a learned value function, a kernel-density safe set, and probabilistic chance
    constraints over an ensemble dynamics model, to safely and efficiently learn robotic
    control tasks.
  zh: SAVED是一种深度模型强化学习算法，仅利用稀疏的任务完成监督信号和少量次优演示，结合学习到的价值函数、核密度安全集以及集成动力学模型上的概率机会约束，安全且高效地学习机器人控制任务。
  ko: SAVED는 희소한 작업 완료 감독 신호와 소량의 비최적 시연, 학습된 가치 함수, 커널 밀도 안전 집합, 그리고 앙상블 동역학 모델 기반
    확률적 기회 제약을 활용하여 로봇 제어 작업을 안전하고 효율적으로 학습하는 알고리즘이다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv/IEEE preprint PDF; requires human review before
    verification.
sources:
- id: src_001
  type: paper
  title: 'Safety Augmented Value Estimation from Demonstrations (SAVED): Safe Deep
    Model-Based RL for Sparse Cost Robotic Tasks'
  url: https://arxiv.org/abs/1905.13402
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

SAVED addresses two core difficulties in robotic reinforcement learning: the need for hand-engineered dense cost functions and the challenge of safe exploration under dynamical uncertainty. It assumes a finite-horizon MDP with a sparse indicator cost that only identifies task completion, a fixed start-state distribution, a known goal set, and a modest set of suboptimal but constraint-satisfying demonstrations. The algorithm combines deep model predictive control with a learned value function (to provide terminal-cost guidance in sparse-cost settings), a non-parametric kernel-density safe set initialized from demonstrations, and trajectory-level probabilistic chance constraints over an ensemble learned dynamics model. Planning is performed via the cross-entropy method (CEM), and the dynamics, value function, and safety density model are updated on-policy after each iteration.

The authors evaluate SAVED on six simulated continuous-control benchmarks and on a real surgical knot-tying task. Simulated tasks include four navigation domains with obstacles and channels, a torque-controlled PR2 Reacher task, and a position-controlled Fetch pick-and-place task. The physical experiments use the da Vinci Research Kit (dVRK), where SAVED optimizes one arm of a surgical knot-tying motion while keeping trajectories inside a 1 cm tube around demonstrations. Across tasks, SAVED is reported to achieve higher success rates, higher constraint-satisfaction rates, and substantially better sample efficiency than model-free and model-based baselines. On the real robot, SAVED reaches over 75% success in the first 50 training iterations while baselines succeed less than 5% of the time, and the full training run takes about one hour.

SAVED is positioned as a practical algorithm for safely learning dynamic manipulation skills when only sparse completion feedback is available. By constraining exploration to regions where the agent has previously reached the goal and by using ensemble uncertainty to enforce state-space constraints, it reduces the need for dense reward shaping and improves safety during learning.

## Key Contributions

- A deep model-based RL algorithm that learns from sparse task-completion supervision and a small set of suboptimal demonstrations, avoiding the need for hand-engineered dense cost functions.
- Constrained exploration through a sampled safe set represented by a kernel-density model, which guides planning toward states with high probability of task completion while still allowing policy improvement.
- Probabilistic chance constraints over an ensemble learned dynamics model that discard control sequences violating user-specified state-space constraints in more than a tunable fraction of sampled rollouts.
- Experimental evaluation on six simulated benchmarks and a real da Vinci surgical knot-tying task, demonstrating higher success rate, constraint satisfaction, and sample efficiency than model-free (SACfD, OEFD) and model-based (PETSfD, behavior cloning) baselines.

## Relevance to Humanoid Robotics

Humanoid robots must perform complex, dynamic manipulation tasks in unstructured environments where designing dense reward functions is labor-intensive and safety is paramount. SAVED directly addresses this setting by enabling sample-efficient, safe learning from sparse completion signals and suboptimal demonstrations, which matches how humanoid skills are often taught and deployed. Its combination of learned dynamics, value functions, safe sets, and chance constraints provides a template for training humanoid control policies for industrial assembly, logistics, or service tasks while limiting unsafe exploration. The real-robot results on the dVRK further show that the method is feasible on physical hardware with imprecise dynamics, an important consideration for humanoid platforms.
