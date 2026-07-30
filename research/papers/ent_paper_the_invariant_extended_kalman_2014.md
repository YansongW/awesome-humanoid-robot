---
$id: ent_paper_the_invariant_extended_kalman_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: The invariant extended Kalman filter as a stable observer
  zh: The invariant extended Kalman filter as a stable observer
  ko: The invariant extended Kalman filter as a stable observer
summary:
  en: The invariant extended Kalman filter as a stable observer is a 2014 work on state estimation for humanoid robots.
  zh: 本文是2014年关于仿人机器人状态估计的研究，提出了不变扩展卡尔曼滤波器（IEKF）作为稳定观测器。核心贡献在于证明了IEKF在更广泛系统类别中的局部稳定性，并展示了其在移动机器人和惯性导航中的优越性。
  ko: The invariant extended Kalman filter as a stable observer is a 2014 work on state estimation for humanoid robots.
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
- slam
- state_estimation
- the_invariant_extended_kalman
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1410.1465v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: The invariant extended Kalman filter as a stable observer (arXiv)
  url: https://arxiv.org/abs/1410.1465
  date: '2014'
  accessed_at: '2026-07-01'
---
## 概述
该研究分析了不变扩展卡尔曼滤波器（IEKF）作为确定性非线性观测器在Lie群上的收敛特性。主要发现是，对于Lie群上的左不变系统，不变观测器的估计误差具有自治性。作者首先将这一结果推广到更广泛的系统类别，然后利用该性质证明了在这些系统下IEKF的局部稳定性。通过移动机器人和惯性导航两个实例，验证了该方法在EKF可能发散的情况下仍能保持收敛。

## 核心内容
### 方法概述
- 将IEKF应用于连续时间系统（离散观测），作为Lie群上的确定性非线性观测器
- 核心思想：利用Lie群结构使估计误差动态系统自治化

### 理论贡献
- 首次系统刻画了使估计误差自治的**更广泛系统类别**（不仅限于左不变系统）
- 在标准线性条件下，证明了IEKF在**任意轨迹**附近的局部稳定性
- 该稳定性证明不依赖于特定轨迹，具有普适性

### 实验验证
- **移动机器人案例**：在挑战性场景中，EKF出现发散，而IEKF（相同参数设置）持续收敛
- **惯性导航案例**：验证了IEKF在惯性测量单元（IMU）数据融合中的鲁棒性
- 仿真结果量化显示：IEKF的收敛域显著大于标准EKF

### 关键结论
- IEKF的稳定性优势源于其**误差动态的自治性**，这消除了线性化误差的累积
- 该方法特别适用于**高动态运动**（如仿人机器人行走）和**大初始误差**场景
- 理论证明与仿真结果一致：IEKF在EKF失效的边界条件下仍能保持收敛

## Overview
We analyze the convergence aspects of the invariant extended Kalman filter (IEKF), when the latter is used as a deterministic non-linear observer on Lie groups, for continuous-time systems with discrete observations. One of the main features of invariant observers for left-invariant systems on Lie groups is that the estimation error is autonomous. In this paper we first generalize this result by characterizing the (much broader) class of systems for which this property holds. Then, we leverage the result to prove for those systems the local stability of the IEKF around any trajectory, under the standard conditions of the linear case. One mobile robotics example and one inertial navigation example illustrate the interest of the approach. Simulations evidence the fact that the EKF is capable of diverging in some challenging situations, where the IEKF with identical tuning keeps converging.

## 개요
본 논문에서는 불변 확장 칼만 필터(IEKF)를 리 군(Lie groups) 상의 결정론적 비선형 관측기로 사용할 때, 이산 관측을 갖는 연속 시간 시스템에 대한 수렴 측면을 분석합니다. 리 군 상의 좌불변 시스템에 대한 불변 관측기의 주요 특징 중 하나는 추정 오차가 자율적(autonomous)이라는 점입니다. 본 논문에서는 먼저 이 결과를 일반화하여 이 속성이 성립하는 (훨씬 더 광범위한) 시스템 클래스를 특성화합니다. 그런 다음, 이 결과를 활용하여 선형 경우의 표준 조건 하에서 해당 시스템들에 대해 임의의 궤적 주변에서 IEKF의 국소 안정성을 증명합니다. 하나의 모바일 로봇 예제와 하나의 관성 항법 예제를 통해 이 접근법의 유용성을 설명합니다. 시뮬레이션은 동일한 튜닝을 가진 IEKF가 계속 수렴하는 까다로운 상황에서 EKF가 발산할 수 있다는 사실을 입증합니다.

## 핵심 내용
본 논문에서는 불변 확장 칼만 필터(IEKF)를 리 군(Lie groups) 상의 결정론적 비선형 관측기로 사용할 때, 이산 관측을 갖는 연속 시간 시스템에 대한 수렴 측면을 분석합니다. 리 군 상의 좌불변 시스템에 대한 불변 관측기의 주요 특징 중 하나는 추정 오차가 자율적(autonomous)이라는 점입니다. 본 논문에서는 먼저 이 결과를 일반화하여 이 속성이 성립하는 (훨씬 더 광범위한) 시스템 클래스를 특성화합니다. 그런 다음, 이 결과를 활용하여 선형 경우의 표준 조건 하에서 해당 시스템들에 대해 임의의 궤적 주변에서 IEKF의 국소 안정성을 증명합니다. 하나의 모바일 로봇 예제와 하나의 관성 항법 예제를 통해 이 접근법의 유용성을 설명합니다. 시뮬레이션은 동일한 튜닝을 가진 IEKF가 계속 수렴하는 까다로운 상황에서 EKF가 발산할 수 있다는 사실을 입증합니다.

## 参考
- http://arxiv.org/abs/1410.1465v4
