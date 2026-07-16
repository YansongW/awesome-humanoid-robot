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
  en: This paper introduces EIC2, a constrained Bayesian optimization framework for robot learning with crash constraints,
    where failed experiments yield no data; it models constraints with a Gaussian process for classified regression (GPCR)
    that combines discrete failure/success labels with continuous observations and learns the constraint threshold as a hyperparameter.
  zh: 本文提出了EIC2，一种用于具有碰撞约束的机器人学习的约束贝叶斯优化框架：失败实验不产生数据；它使用高斯过程分类回归（GPCR）对约束建模，将离散的成功/失败标签与连续观测结合，并将约束阈值作为超参数学习。
  ko: 본 논문은 충돌 제약 조건이 있는 로봇 학습을 위한 제약 베이지안 최적화 프레임워크인 EIC2를 제안한다. 실패한 실험에서는 데이터를 얻을 수 없으며, GPCR(분류 회귀를 위한 가우시안 프로세스)을 사용하여
    이산적 성공/실패 레이블과 연속적 관측을 결합하고 제약 임계값을 하이퍼파라미터로 학습한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.08669v3.
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
## 概述
In the past decade, numerous machine learning algorithms have been shown to successfully learn optimal policies to control real robotic systems. However, it is common to encounter failing behaviors as the learning loop progresses. Specifically, in robot applications where failing is undesired but not catastrophic, many algorithms struggle with leveraging data obtained from failures. This is usually caused by (i) the failed experiment ending prematurely, or (ii) the acquired data being scarce or corrupted. Both complicate the design of proper reward functions to penalize failures. In this paper, we propose a framework that addresses those issues. We consider failing behaviors as those that violate a constraint and address the problem of learning with crash constraints, where no data is obtained upon constraint violation. The no-data case is addressed by a novel GP model (GPCR) for the constraint that combines discrete events (failure/success) with continuous observations (only obtained upon success). We demonstrate the effectiveness of our framework on simulated benchmarks and on a real jumping quadruped, where the constraint threshold is unknown a priori. Experimental data is collected, by means of constrained Bayesian optimization, directly on the real robot. Our results outperform manual tuning and GPCR proves useful on estimating the constraint threshold.

## 核心内容
In the past decade, numerous machine learning algorithms have been shown to successfully learn optimal policies to control real robotic systems. However, it is common to encounter failing behaviors as the learning loop progresses. Specifically, in robot applications where failing is undesired but not catastrophic, many algorithms struggle with leveraging data obtained from failures. This is usually caused by (i) the failed experiment ending prematurely, or (ii) the acquired data being scarce or corrupted. Both complicate the design of proper reward functions to penalize failures. In this paper, we propose a framework that addresses those issues. We consider failing behaviors as those that violate a constraint and address the problem of learning with crash constraints, where no data is obtained upon constraint violation. The no-data case is addressed by a novel GP model (GPCR) for the constraint that combines discrete events (failure/success) with continuous observations (only obtained upon success). We demonstrate the effectiveness of our framework on simulated benchmarks and on a real jumping quadruped, where the constraint threshold is unknown a priori. Experimental data is collected, by means of constrained Bayesian optimization, directly on the real robot. Our results outperform manual tuning and GPCR proves useful on estimating the constraint threshold.

## 参考
- http://arxiv.org/abs/2010.08669v3

## Overview
In the past decade, numerous machine learning algorithms have been shown to successfully learn optimal policies to control real robotic systems. However, it is common to encounter failing behaviors as the learning loop progresses. Specifically, in robot applications where failing is undesired but not catastrophic, many algorithms struggle with leveraging data obtained from failures. This is usually caused by (i) the failed experiment ending prematurely, or (ii) the acquired data being scarce or corrupted. Both complicate the design of proper reward functions to penalize failures. In this paper, we propose a framework that addresses those issues. We consider failing behaviors as those that violate a constraint and address the problem of learning with crash constraints, where no data is obtained upon constraint violation. The no-data case is addressed by a novel GP model (GPCR) for the constraint that combines discrete events (failure/success) with continuous observations (only obtained upon success). We demonstrate the effectiveness of our framework on simulated benchmarks and on a real jumping quadruped, where the constraint threshold is unknown a priori. Experimental data is collected, by means of constrained Bayesian optimization, directly on the real robot. Our results outperform manual tuning and GPCR proves useful on estimating the constraint threshold.

## Content
In the past decade, numerous machine learning algorithms have been shown to successfully learn optimal policies to control real robotic systems. However, it is common to encounter failing behaviors as the learning loop progresses. Specifically, in robot applications where failing is undesired but not catastrophic, many algorithms struggle with leveraging data obtained from failures. This is usually caused by (i) the failed experiment ending prematurely, or (ii) the acquired data being scarce or corrupted. Both complicate the design of proper reward functions to penalize failures. In this paper, we propose a framework that addresses those issues. We consider failing behaviors as those that violate a constraint and address the problem of learning with crash constraints, where no data is obtained upon constraint violation. The no-data case is addressed by a novel GP model (GPCR) for the constraint that combines discrete events (failure/success) with continuous observations (only obtained upon success). We demonstrate the effectiveness of our framework on simulated benchmarks and on a real jumping quadruped, where the constraint threshold is unknown a priori. Experimental data is collected, by means of constrained Bayesian optimization, directly on the real robot. Our results outperform manual tuning and GPCR proves useful on estimating the constraint threshold.

## 개요
지난 10년간, 수많은 머신러닝 알고리즘이 실제 로봇 시스템을 제어하기 위한 최적의 정책을 성공적으로 학습하는 것으로 입증되었습니다. 그러나 학습 루프가 진행됨에 따라 실패 동작이 발생하는 것은 흔한 일입니다. 특히, 실패가 바람직하지 않지만 치명적이지 않은 로봇 애플리케이션에서는 많은 알고리즘이 실패로부터 얻은 데이터를 활용하는 데 어려움을 겪습니다. 이는 일반적으로 (i) 실패한 실험이 조기에 종료되거나, (ii) 획득한 데이터가 부족하거나 손상되었기 때문에 발생합니다. 두 경우 모두 실패를 처벌하기 위한 적절한 보상 함수 설계를 복잡하게 만듭니다. 본 논문에서는 이러한 문제를 해결하는 프레임워크를 제안합니다. 우리는 실패 동작을 제약 조건을 위반하는 것으로 간주하고, 제약 조건 위반 시 데이터를 얻을 수 없는 충돌 제약 조건 하에서의 학습 문제를 다룹니다. 데이터가 없는 경우는 이산적 사건(실패/성공)과 연속적 관측(성공 시에만 획득)을 결합한 새로운 GP 모델(GPCR)을 통해 해결합니다. 우리는 시뮬레이션 벤치마크와 제약 조건 임계값이 사전에 알려지지 않은 실제 점프 사족 로봇에서 프레임워크의 효과를 입증합니다. 실험 데이터는 제약 조건이 있는 베이지안 최적화를 통해 실제 로봇에서 직접 수집됩니다. 우리의 결과는 수동 튜닝을 능가하며, GPCR은 제약 조건 임계값 추정에 유용함을 입증합니다.

## 핵심 내용
지난 10년간, 수많은 머신러닝 알고리즘이 실제 로봇 시스템을 제어하기 위한 최적의 정책을 성공적으로 학습하는 것으로 입증되었습니다. 그러나 학습 루프가 진행됨에 따라 실패 동작이 발생하는 것은 흔한 일입니다. 특히, 실패가 바람직하지 않지만 치명적이지 않은 로봇 애플리케이션에서는 많은 알고리즘이 실패로부터 얻은 데이터를 활용하는 데 어려움을 겪습니다. 이는 일반적으로 (i) 실패한 실험이 조기에 종료되거나, (ii) 획득한 데이터가 부족하거나 손상되었기 때문에 발생합니다. 두 경우 모두 실패를 처벌하기 위한 적절한 보상 함수 설계를 복잡하게 만듭니다. 본 논문에서는 이러한 문제를 해결하는 프레임워크를 제안합니다. 우리는 실패 동작을 제약 조건을 위반하는 것으로 간주하고, 제약 조건 위반 시 데이터를 얻을 수 없는 충돌 제약 조건 하에서의 학습 문제를 다룹니다. 데이터가 없는 경우는 이산적 사건(실패/성공)과 연속적 관측(성공 시에만 획득)을 결합한 새로운 GP 모델(GPCR)을 통해 해결합니다. 우리는 시뮬레이션 벤치마크와 제약 조건 임계값이 사전에 알려지지 않은 실제 점프 사족 로봇에서 프레임워크의 효과를 입증합니다. 실험 데이터는 제약 조건이 있는 베이지안 최적화를 통해 실제 로봇에서 직접 수집됩니다. 우리의 결과는 수동 튜닝을 능가하며, GPCR은 제약 조건 임계값 추정에 유용함을 입증합니다.
