---
$id: ent_paper_control_of_humanoid_robots_wit_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
  zh: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
  ko: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
summary:
  en: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models is a 2025 work on hardware design
    for humanoid robots.
  zh: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models is a 2025 work on hardware design
    for humanoid robots.
  ko: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models is a 2025 work on hardware design
    for humanoid robots.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- control_of_humanoid_robots_wit
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22459v2.
sources:
- id: src_001
  type: paper
  title: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models (arXiv)
  url: https://arxiv.org/abs/2503.22459
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Several recently released humanoid robots, inspired by the mechanical design of Cassie, employ actuator configurations in which the motors are displaced from the joints to reduce leg inertia. While studies accounting for the full kinematic complexity have demonstrated the benefits of these designs, the associated loop-closure constraints greatly increase computational cost and limit their use in control and learning. As a result, the non-linear transmission is often approximated by a constant reduction ratio, preventing exploitation of the mechanism's full capabilities. This paper introduces a compact analytical formulation for the two standard knee and ankle mechanisms that captures the exact non-linear transmission while remaining computationally efficient. The model is fully differentiable up to second order with a minimal formulation, enabling low-cost evaluation of dynamic derivatives for trajectory optimization and of the apparent transmission impedance for reinforcement learning. We integrate this formulation into trajectory optimization and locomotion policy learning, and compare it against simplified constant-ratio approaches. Hardware experiments demonstrate improved accuracy and robustness, showing that the proposed method provides a practical means to incorporate parallel actuation into modern control algorithms.

## 核心内容
Several recently released humanoid robots, inspired by the mechanical design of Cassie, employ actuator configurations in which the motors are displaced from the joints to reduce leg inertia. While studies accounting for the full kinematic complexity have demonstrated the benefits of these designs, the associated loop-closure constraints greatly increase computational cost and limit their use in control and learning. As a result, the non-linear transmission is often approximated by a constant reduction ratio, preventing exploitation of the mechanism's full capabilities. This paper introduces a compact analytical formulation for the two standard knee and ankle mechanisms that captures the exact non-linear transmission while remaining computationally efficient. The model is fully differentiable up to second order with a minimal formulation, enabling low-cost evaluation of dynamic derivatives for trajectory optimization and of the apparent transmission impedance for reinforcement learning. We integrate this formulation into trajectory optimization and locomotion policy learning, and compare it against simplified constant-ratio approaches. Hardware experiments demonstrate improved accuracy and robustness, showing that the proposed method provides a practical means to incorporate parallel actuation into modern control algorithms.

## 参考
- http://arxiv.org/abs/2503.22459v2

