---
$id: ent_paper_martinez_cantin_bayesian_optimization_with_ada_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bayesian Optimization with Adaptive Kernels for Robot Control
  zh: 用于机器人控制的自适应核贝叶斯优化
  ko: 로봇 제어를 위한 적응형 커널 베이지안 최적화
summary:
  en: This paper introduces Spartan Bayesian Optimization (SBO), a Gaussian-process Bayesian optimization method that uses
    an adaptive local/global Spartan kernel to model nonstationary cost functions without prior knowledge, and evaluates it
    on optimization benchmarks, reinforcement-learning control tasks, and UAV wing design.
  zh: 本文提出了斯巴达贝叶斯优化（SBO），一种利用自适应局部/全局斯巴达核在无需先验知识的情况下对非平稳成本函数进行建模的高斯过程贝叶斯优化方法，并在优化基准、强化学习控制任务和无人机机翼设计上进行了评估。
  ko: 본 논문은 사전 지식 없이 비정상 비용 함수를 모델링하기 위해 적응형 국소/전역 스파르탄 커널을 사용하는 가우시안 프로세스 베이지안 최적화 방법인 스파르탄 베이지안 최적화(SBO)를 제안하고, 최적화 벤치마크,
    강화학습 제어 작업, UAV 날개 설계에서 평가한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- bayesian_optimization
- policy_search
- reinforcement_learning
- gaussian_process
- nonstationary_modeling
- sample_efficient_optimization
- robot_control
- locomotion_control
- uav_wing_design
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.07021v1.
sources:
- id: src_001
  type: paper
  title: Bayesian Optimization with Adaptive Kernels for Robot Control
  url: https://arxiv.org/abs/2402.07021
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Active policy search combines the trial-and-error methodology from policy search with Bayesian optimization to actively find the optimal policy. First, policy search is a type of reinforcement learning which has become very popular for robot control, for its ability to deal with complex continuous state and action spaces. Second, Bayesian optimization is a sample efficient global optimization method that uses a surrogate model, like a Gaussian process, and optimal decision making to carefully select each sample during the optimization process. Sample efficiency is of paramount importance when each trial involves the real robot, expensive Monte Carlo runs, or a complex simulator. Black-box Bayesian optimization generally assumes a cost function from a stationary process, because nonstationary modeling is usually based on prior knowledge. However, many control problems are inherently nonstationary due to their failure conditions, terminal states and other abrupt effects. In this paper, we present a kernel function specially designed for Bayesian optimization, that allows nonstationary modeling without prior knowledge, using an adaptive local region. The new kernel results in an improved local search (exploitation), without penalizing the global search (exploration), as shown experimentally in well-known optimization benchmarks and robot control scenarios. We finally show its potential for the design of the wing shape of a UAV.

## 核心内容
Active policy search combines the trial-and-error methodology from policy search with Bayesian optimization to actively find the optimal policy. First, policy search is a type of reinforcement learning which has become very popular for robot control, for its ability to deal with complex continuous state and action spaces. Second, Bayesian optimization is a sample efficient global optimization method that uses a surrogate model, like a Gaussian process, and optimal decision making to carefully select each sample during the optimization process. Sample efficiency is of paramount importance when each trial involves the real robot, expensive Monte Carlo runs, or a complex simulator. Black-box Bayesian optimization generally assumes a cost function from a stationary process, because nonstationary modeling is usually based on prior knowledge. However, many control problems are inherently nonstationary due to their failure conditions, terminal states and other abrupt effects. In this paper, we present a kernel function specially designed for Bayesian optimization, that allows nonstationary modeling without prior knowledge, using an adaptive local region. The new kernel results in an improved local search (exploitation), without penalizing the global search (exploration), as shown experimentally in well-known optimization benchmarks and robot control scenarios. We finally show its potential for the design of the wing shape of a UAV.

## 参考
- http://arxiv.org/abs/2402.07021v1

