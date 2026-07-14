---
$id: ent_paper_physics_informed_neural_networ_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation
  zh: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation
  ko: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation
summary:
  en: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation is a 2025 work
    on state estimation for humanoid robots.
  zh: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation is a 2025 work
    on state estimation for humanoid robots.
  ko: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation is a 2025 work
    on state estimation for humanoid robots.
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
- physics_informed_neural_networ
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.10105v1.
sources:
- id: src_001
  type: paper
  title: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation (arXiv)
  url: https://arxiv.org/abs/2507.10105
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents a novel framework for whole-body torque control of humanoid robots without joint torque sensors, designed for systems with electric motors and high-ratio harmonic drives. The approach integrates Physics-Informed Neural Networks (PINNs) for friction modeling and Unscented Kalman Filtering (UKF) for joint torque estimation, within a real-time torque control architecture. PINNs estimate nonlinear static and dynamic friction from joint and motor velocity readings, capturing effects like motor actuation without joint movement. The UKF utilizes PINN-based friction estimates as direct measurement inputs, improving torque estimation robustness. Experimental validation on the ergoCub humanoid robot demonstrates improved torque tracking accuracy, enhanced energy efficiency, and superior disturbance rejection compared to the state-of-the-art Recursive Newton-Euler Algorithm (RNEA), using a dynamic balancing experiment. The framework's scalability is shown by consistent performance across robots with similar hardware but different friction characteristics, without re-identification. Furthermore, a comparative analysis with position control highlights the advantages of the proposed torque control approach. The results establish the method as a scalable and practical solution for sensorless torque control in humanoid robots, ensuring torque tracking, adaptability, and stability in dynamic environments.

## 核心内容
This paper presents a novel framework for whole-body torque control of humanoid robots without joint torque sensors, designed for systems with electric motors and high-ratio harmonic drives. The approach integrates Physics-Informed Neural Networks (PINNs) for friction modeling and Unscented Kalman Filtering (UKF) for joint torque estimation, within a real-time torque control architecture. PINNs estimate nonlinear static and dynamic friction from joint and motor velocity readings, capturing effects like motor actuation without joint movement. The UKF utilizes PINN-based friction estimates as direct measurement inputs, improving torque estimation robustness. Experimental validation on the ergoCub humanoid robot demonstrates improved torque tracking accuracy, enhanced energy efficiency, and superior disturbance rejection compared to the state-of-the-art Recursive Newton-Euler Algorithm (RNEA), using a dynamic balancing experiment. The framework's scalability is shown by consistent performance across robots with similar hardware but different friction characteristics, without re-identification. Furthermore, a comparative analysis with position control highlights the advantages of the proposed torque control approach. The results establish the method as a scalable and practical solution for sensorless torque control in humanoid robots, ensuring torque tracking, adaptability, and stability in dynamic environments.

## 参考
- http://arxiv.org/abs/2507.10105v1

