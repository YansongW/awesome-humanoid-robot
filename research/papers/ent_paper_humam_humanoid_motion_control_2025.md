---
$id: ent_paper_humam_humanoid_motion_control_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba'
  zh: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba'
  ko: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba'
summary:
  en: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba is a 2025 work on locomotion for humanoid robots.'
  zh: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba is a 2025 work on locomotion for humanoid robots.'
  ko: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humam
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.18046v2.
sources:
- id: src_001
  type: paper
  title: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba (arXiv)'
  url: https://arxiv.org/abs/2509.18046
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
End-to-end reinforcement learning (RL) for humanoid locomotion is appealing for its compact perception-action mapping, yet practical policies often suffer from training instability, inefficient feature fusion, and high actuation cost. We present HuMam, a state-centric end-to-end RL framework that employs a single-layer Mamba encoder to fuse robot-centric states with oriented footstep targets and a continuous phase clock. The policy outputs joint position targets tracked by a low-level PD loop and is optimized with PPO. A concise six-term reward balances contact quality, swing smoothness, foot placement, posture, and body stability while implicitly promoting energy saving. On the JVRC-1 humanoid in mc-mujoco, HuMam consistently improves learning efficiency, training stability, and overall task performance over a strong feedforward baseline, while reducing power consumption and torque peaks. To our knowledge, this is the first end-to-end humanoid RL controller that adopts Mamba as the fusion backbone, demonstrating tangible gains in efficiency, stability, and control economy.

## 核心内容
End-to-end reinforcement learning (RL) for humanoid locomotion is appealing for its compact perception-action mapping, yet practical policies often suffer from training instability, inefficient feature fusion, and high actuation cost. We present HuMam, a state-centric end-to-end RL framework that employs a single-layer Mamba encoder to fuse robot-centric states with oriented footstep targets and a continuous phase clock. The policy outputs joint position targets tracked by a low-level PD loop and is optimized with PPO. A concise six-term reward balances contact quality, swing smoothness, foot placement, posture, and body stability while implicitly promoting energy saving. On the JVRC-1 humanoid in mc-mujoco, HuMam consistently improves learning efficiency, training stability, and overall task performance over a strong feedforward baseline, while reducing power consumption and torque peaks. To our knowledge, this is the first end-to-end humanoid RL controller that adopts Mamba as the fusion backbone, demonstrating tangible gains in efficiency, stability, and control economy.

## 参考
- http://arxiv.org/abs/2509.18046v2

