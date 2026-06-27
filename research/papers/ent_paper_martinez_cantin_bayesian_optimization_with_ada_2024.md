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
  en: This paper introduces Spartan Bayesian Optimization (SBO), a Gaussian-process
    Bayesian optimization method that uses an adaptive local/global Spartan kernel
    to model nonstationary cost functions without prior knowledge, and evaluates it
    on optimization benchmarks, reinforcement-learning control tasks, and UAV wing
    design.
  zh: 本文提出了斯巴达贝叶斯优化（SBO），一种利用自适应局部/全局斯巴达核在无需先验知识的情况下对非平稳成本函数进行建模的高斯过程贝叶斯优化方法，并在优化基准、强化学习控制任务和无人机机翼设计上进行了评估。
  ko: 본 논문은 사전 지식 없이 비정상 비용 함수를 모델링하기 위해 적응형 국소/전역 스파르탄 커널을 사용하는 가우시안 프로세스 베이지안 최적화
    방법인 스파르탄 베이지안 최적화(SBO)를 제안하고, 최적화 벤치마크, 강화학습 제어 작업, UAV 날개 설계에서 평가한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; requires human review
    against the full arXiv text before full verification.
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

## Overview

The paper addresses the problem that standard Bayesian optimization typically assumes a stationary cost function, whereas many robot control tasks are nonstationary because of failure conditions, terminal states, and abrupt transitions. To handle this mismatch, the authors propose Spartan Bayesian Optimization (SBO). SBO maintains both a local kernel and a global kernel and adaptively weights them with multivariate-normal functions centered on the current optimum, allowing the model to become more flexible near promising regions without requiring prior knowledge of the nonstationary structure.

The adaptive kernel, referred to as the Spartan kernel, is integrated into a Gaussian-process Bayesian optimization loop. Because the weighting functions are learned jointly with the other hyperparameters, the method can automatically shrink or expand the local region as optimization progresses. The paper compares SBO against standard Bayesian optimization and other baselines on synthetic functions and on reinforcement-learning control tasks such as a 3-limb walker, mountain car, and helicopter hovering. It also demonstrates the method on a UAV wing-shape design problem parameterized by Bezier curves.

A trade-off of the approach is increased computational cost: the hyperparameter space is enlarged (3d parameters versus d for a single Matérn kernel) and each kernel evaluation requires combining the local and global components. The authors note that the local weight variance must be fixed or regularized to keep the problem well posed.

## Key Contributions

- Introduces the Spartan kernel, an adaptive local/global kernel for Gaussian-process Bayesian optimization.
- Enables nonstationary modeling without requiring prior knowledge of the function structure.
- Improves local exploitation while preserving global exploration capabilities.
- Provides extensive empirical evaluation on optimization benchmarks (Gramacy, Branin-Hoo, Hartmann 6D, Michalewicz), reinforcement-learning robot control tasks (3-limb walker, mountain car, helicopter hovering), and a UAV wing-design case study.

## Relevance to Humanoid Robotics

Although the experiments in the paper are not focused exclusively on humanoid robots, the method is directly relevant to humanoid robotics. Bipedal locomotion and whole-body control involve highly nonstationary cost landscapes: falls, joint limits, and contact changes create abrupt regions where standard stationary Bayesian optimization can perform poorly. Sample-efficient policy tuning is especially important for humanoid hardware, where each physical trial is expensive and time-consuming.

By improving local exploitation without sacrificing global exploration, SBO could be used to tune gait parameters, feedback gains, or learned policies for humanoid platforms, supporting both prototyping and mass-production calibration workflows. The emphasis on sample efficiency aligns with the need to reduce robot-hours during controller development and fleet-wide parameter adaptation.
