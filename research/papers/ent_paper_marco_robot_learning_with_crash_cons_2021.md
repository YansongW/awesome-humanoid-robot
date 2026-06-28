---
$id: ent_paper_marco_robot_learning_with_crash_cons_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robot Learning with Crash Constraints
  zh: 具有碰撞约束的机器人学习
  ko: 충돌 제약 조건을 갖는 로봇 학습
summary:
  en: This paper introduces EIC2, a constrained Bayesian optimization framework for
    robot learning with crash constraints, where failed experiments yield no data;
    it models constraints with a Gaussian process for classified regression (GPCR)
    that combines discrete failure/success labels with continuous observations and
    learns the constraint threshold as a hyperparameter.
  zh: 本文提出了EIC2，一种用于具有碰撞约束的机器人学习的约束贝叶斯优化框架：失败实验不产生数据；它使用高斯过程分类回归（GPCR）对约束建模，将离散的成功/失败标签与连续观测结合，并将约束阈值作为超参数学习。
  ko: 본 논문은 충돌 제약 조건이 있는 로봇 학습을 위한 제약 베이지안 최적화 프레임워크인 EIC2를 제안한다. 실패한 실험에서는 데이터를 얻을
    수 없으며, GPCR(분류 회귀를 위한 가우시안 프로세스)을 사용하여 이산적 성공/실패 레이블과 연속적 관측을 결합하고 제약 임계값을 하이퍼파라미터로
    학습한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 10_evaluation_benchmarks
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- constrained_bayesian_optimization
- crash_constraints
- eic2
- gpcr
- gaussian_process
- robot_learning
- constraint_threshold_learning
- quadruped_robot
- solo_robot
- jumping_robot
- safe_learning
- motor_current_constraint
- expectation_propagation
- hyperparameter_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from arXiv full text (arXiv:2010.08669v3, accepted January 2021);
    requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Robot Learning with Crash Constraints
  url: https://arxiv.org/abs/2010.08669
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Many robot learning algorithms encounter failing behaviors during the search for optimal controller parameters. When failures are undesired but not catastrophic, they often end the experiment prematurely or produce scarce or corrupted measurements, making it hard to design reward functions that properly penalize failures. This paper frames this situation as the problem of learning with crash constraints (LCC): a reward is observed upon successful execution, but only a discrete failure label is available when the robot crashes. The authors address LCC with constrained Bayesian optimization (BOC) and propose the EIC2 framework, which stands for expected improvement with crash constraints.

The key modeling contribution is the Gaussian process for classified regression (GPCR). Unlike a standard GP regressor or classifier, GPCR combines two observation types in a single-output GP: a discrete label indicating failure or success, and a continuous constraint value that is only observed when the constraint is satisfied. This allows EIC2 to exploit failure information without hand-crafted penalty terms in the objective, while also modeling the objective cost with a standard GP. In addition, GPCR treats the constraint threshold as a hyperparameter and estimates it from data via maximum a posteriori (MAP), reducing the need for expert knowledge that is typically required to set this threshold.

The effectiveness of EIC2 is demonstrated in two settings. First, numerical benchmarks for global minimization—Michalewicz 10D, Hartman 6D, and Egg Crate 2D—are used to compare EIC2 against heuristic penalty strategies and against baseline constrained BO methods such as EIC, PIBU, and SAFEOPT. Second, and most importantly, EIC2 is validated on a real jumping quadruped, the Solo robot. Using a kinodynamic planner, a PD controller with variable gains, and a 200 Hz motion capture system, EIC2 automatically tunes four controller gains to maximize jump height while keeping the total motor current below an unknown threshold. The learned controller achieved a jump height of 0.784 m, about 34% higher than the 0.65 m obtained with manual tuning, and GPCR estimated the current threshold at 112.34 A.

## Key Contributions

- EIC2: a constrained Bayesian optimization framework that explicitly addresses learning with crash constraints (LCC), where no objective or constraint data is obtained upon failure.
- GPCR: a single-output Gaussian process model that jointly handles discrete failure/success labels and continuous constraint observations.
- Constraint threshold treated as a learnable hyperparameter via MAP estimation, reducing reliance on expert knowledge and ad hoc choices.
- First real-system solution to LCC, validated on a jumping Solo quadruped robot, with learned jumps about 34% higher than manual tuning.

## Relevance to Humanoid Robotics

Humanoid robots are complex, high-dimensional systems where controller tuning for locomotion, balance, and manipulation is expensive, time-consuming, and failure-prone. The EIC2/GPCR framework is directly relevant because it automates sample-efficient controller tuning under safety constraints directly on hardware, without requiring a pre-specified constraint threshold or hand-designed failure penalties. This can reduce the expert labor currently needed to tune gaits, balance controllers, and whole-body policies, and it provides a principled way to learn safe operating regions from crash events.

More broadly, the ability to learn from crash constraints supports the scalability and mass deployment of humanoid platforms. As manufacturers move from one-off prototypes to larger fleets, automated, safe learning methods that minimize hardware damage and manual intervention become critical. EIC2's combination of constrained Bayesian optimization, hybrid discrete/continuous GP modeling, and threshold learning offers a reusable building block for safe learning pipelines in humanoid locomotion and beyond.
