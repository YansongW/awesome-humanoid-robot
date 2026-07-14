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

