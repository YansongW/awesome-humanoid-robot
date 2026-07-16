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
  zh: The invariant extended Kalman filter as a stable observer is a 2014 work on state estimation for humanoid robots.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1410.1465v4.
sources:
- id: src_001
  type: paper
  title: The invariant extended Kalman filter as a stable observer (arXiv)
  url: https://arxiv.org/abs/1410.1465
  date: '2014'
  accessed_at: '2026-07-01'
---
## 概述
We analyze the convergence aspects of the invariant extended Kalman filter (IEKF), when the latter is used as a deterministic non-linear observer on Lie groups, for continuous-time systems with discrete observations. One of the main features of invariant observers for left-invariant systems on Lie groups is that the estimation error is autonomous. In this paper we first generalize this result by characterizing the (much broader) class of systems for which this property holds. Then, we leverage the result to prove for those systems the local stability of the IEKF around any trajectory, under the standard conditions of the linear case. One mobile robotics example and one inertial navigation example illustrate the interest of the approach. Simulations evidence the fact that the EKF is capable of diverging in some challenging situations, where the IEKF with identical tuning keeps converging.

## 核心内容
We analyze the convergence aspects of the invariant extended Kalman filter (IEKF), when the latter is used as a deterministic non-linear observer on Lie groups, for continuous-time systems with discrete observations. One of the main features of invariant observers for left-invariant systems on Lie groups is that the estimation error is autonomous. In this paper we first generalize this result by characterizing the (much broader) class of systems for which this property holds. Then, we leverage the result to prove for those systems the local stability of the IEKF around any trajectory, under the standard conditions of the linear case. One mobile robotics example and one inertial navigation example illustrate the interest of the approach. Simulations evidence the fact that the EKF is capable of diverging in some challenging situations, where the IEKF with identical tuning keeps converging.

## 参考
- http://arxiv.org/abs/1410.1465v4

## Overview
We analyze the convergence aspects of the invariant extended Kalman filter (IEKF), when the latter is used as a deterministic non-linear observer on Lie groups, for continuous-time systems with discrete observations. One of the main features of invariant observers for left-invariant systems on Lie groups is that the estimation error is autonomous. In this paper we first generalize this result by characterizing the (much broader) class of systems for which this property holds. Then, we leverage the result to prove for those systems the local stability of the IEKF around any trajectory, under the standard conditions of the linear case. One mobile robotics example and one inertial navigation example illustrate the interest of the approach. Simulations evidence the fact that the EKF is capable of diverging in some challenging situations, where the IEKF with identical tuning keeps converging.

## Content
We analyze the convergence aspects of the invariant extended Kalman filter (IEKF), when the latter is used as a deterministic non-linear observer on Lie groups, for continuous-time systems with discrete observations. One of the main features of invariant observers for left-invariant systems on Lie groups is that the estimation error is autonomous. In this paper we first generalize this result by characterizing the (much broader) class of systems for which this property holds. Then, we leverage the result to prove for those systems the local stability of the IEKF around any trajectory, under the standard conditions of the linear case. One mobile robotics example and one inertial navigation example illustrate the interest of the approach. Simulations evidence the fact that the EKF is capable of diverging in some challenging situations, where the IEKF with identical tuning keeps converging.

## 개요
본 논문에서는 불변 확장 칼만 필터(IEKF)를 리 군(Lie groups) 상의 결정론적 비선형 관측기로 사용할 때, 이산 관측을 갖는 연속 시간 시스템에 대한 수렴 측면을 분석합니다. 리 군 상의 좌불변 시스템에 대한 불변 관측기의 주요 특징 중 하나는 추정 오차가 자율적(autonomous)이라는 점입니다. 본 논문에서는 먼저 이 결과를 일반화하여 이 속성이 성립하는 (훨씬 더 광범위한) 시스템 클래스를 특성화합니다. 그런 다음, 이 결과를 활용하여 선형 경우의 표준 조건 하에서 해당 시스템들에 대해 임의의 궤적 주변에서 IEKF의 국소 안정성을 증명합니다. 하나의 모바일 로봇 예제와 하나의 관성 항법 예제를 통해 이 접근법의 유용성을 설명합니다. 시뮬레이션은 동일한 튜닝을 가진 IEKF가 계속 수렴하는 까다로운 상황에서 EKF가 발산할 수 있다는 사실을 입증합니다.

## 핵심 내용
본 논문에서는 불변 확장 칼만 필터(IEKF)를 리 군(Lie groups) 상의 결정론적 비선형 관측기로 사용할 때, 이산 관측을 갖는 연속 시간 시스템에 대한 수렴 측면을 분석합니다. 리 군 상의 좌불변 시스템에 대한 불변 관측기의 주요 특징 중 하나는 추정 오차가 자율적(autonomous)이라는 점입니다. 본 논문에서는 먼저 이 결과를 일반화하여 이 속성이 성립하는 (훨씬 더 광범위한) 시스템 클래스를 특성화합니다. 그런 다음, 이 결과를 활용하여 선형 경우의 표준 조건 하에서 해당 시스템들에 대해 임의의 궤적 주변에서 IEKF의 국소 안정성을 증명합니다. 하나의 모바일 로봇 예제와 하나의 관성 항법 예제를 통해 이 접근법의 유용성을 설명합니다. 시뮬레이션은 동일한 튜닝을 가진 IEKF가 계속 수렴하는 까다로운 상황에서 EKF가 발산할 수 있다는 사실을 입증합니다.
