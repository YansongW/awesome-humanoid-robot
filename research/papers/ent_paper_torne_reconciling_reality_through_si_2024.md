---
$id: ent_paper_torne_reconciling_reality_through_si_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for
    Robust Manipulation'
  zh: 通过仿真调和现实：面向稳健操作的实到仿再到实方法
  ko: '시뮬레이션을 통한 현실 조화: 견고한 조작을 위한 Real-to-Sim-to-Real 접근법'
summary:
  en: RialTo builds on-the-fly digital-twin simulations from real-world scans and
    transfers real-world demonstrations into simulation via a novel inverse-distillation
    procedure, then uses reinforcement learning to robustify imitation-learning policies
    with minimal human supervision.
  zh: RialTo 从真实世界扫描即时构建数字孪生仿真环境，通过一种新颖的逆蒸馏过程将真实世界演示迁移到仿真中，并利用强化学习在最小人类监督下增强模仿学习策略的鲁棒性。
  ko: RialTo는 실제 세계 스캔에서 즉석에서 디지털 트윈 시뮬레이션을 구축하고, 새로운 역증류 절차를 통해 실제 세계 시연을 시뮬레이션으로
    전달한 다음, 최소한의 인간 감독으로 모방 학습 정책을 강화하기 위해 강화 학습을 사용합니다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- digital_twin
- real_to_sim_to_real
- sim_to_real
- inverse_distillation
- imitation_learning
- reinforcement_learning
- visuomotor_policy
- robust_manipulation
- isaac_sim
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review needed
    to confirm exact section citations, related work, and experimental details.
sources:
- id: src_001
  type: paper
  title: 'Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for
    Robust Manipulation'
  url: https://arxiv.org/abs/2403.03949
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

RialTo is a real-to-sim-to-real system designed to robustify real-world imitation-learning policies while avoiding the high human-supervision costs of pure imitation learning and the unsafe, impractical data collection of pure real-world reinforcement learning. The system first provides a GUI for rapidly scanning and reconstructing articulated digital-twin scenes from a small amount of real-world data. It then transfers real-world observation-action demonstrations into privileged-state simulation trajectories through a procedure called inverse distillation, enabling efficient fine-tuning with reinforcement learning inside simulation. Finally, the robustified policy is distilled back into a visuomotor student policy that is co-trained on real-world data, producing a controller that can be deployed back on the real robot.

The pipeline addresses three simultaneous robustness challenges: changes in object poses, physical disturbances, and visual distractors. By training in a digital twin whose parameters and layout are derived from the target deployment environment, RialTo can expose policies to a broader distribution of perturbations than is practical to collect by hand. The authors report robustness improvements exceeding 67% across eight real-world manipulation tasks, including stacking dishes on a rack and placing books on a shelf, without requiring extensive additional human demonstrations.

## Key Contributions

- A real-to-sim-to-real pipeline that robustifies imitation policies while minimizing human effort and unsafe real-world data collection.
- An inverse-distillation algorithm that converts real-world observation-action demonstrations into privileged-state trajectories suitable for simulation-based reinforcement learning.
- An intuitive GUI for rapidly scanning and constructing articulated digital-twin scenes from real-world sensor data.
- Extensive real-world experiments demonstrating large robustness gains across diverse manipulation tasks, including dish stacking, book shelving, and six additional tasks.

## Relevance to Humanoid Robotics

Although RialTo is evaluated on a Franka Panda arm, its core components are directly transferable to humanoid robots that must perform robust visuomotor manipulation in unstructured, deployment-specific environments. Humanoid platforms face the same object-pose variability, physical disturbances, and visual distractors addressed by RialTo, and they typically cannot afford large volumes of unsafe real-world rollouts. The digital-twin construction, inverse-distillation demonstration transfer, and sim-to-real robustification pipeline therefore provide a reusable methodology for humanoid manipulation. Because the system also outputs a visuomotor policy, it is compatible with the camera-based perception stacks common on humanoid robots.
