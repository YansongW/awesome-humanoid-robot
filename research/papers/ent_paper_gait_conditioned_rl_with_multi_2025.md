---
$id: ent_paper_gait_conditioned_rl_with_multi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion
  zh: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion
  ko: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion
summary:
  en: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  zh: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  ko: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gait_conditioned_rl_with_multi
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.20619v3.
sources:
- id: src_001
  type: paper
  title: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2505.20619
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present a unified gait-conditioned reinforcement learning framework that enables humanoid robots to perform standing, walking, running, and smooth transitions within a single recurrent policy. A compact reward routing mechanism dynamically activates gait-specific objectives based on a one-hot gait ID, mitigating reward interference and supporting stable multi-gait learning. Human-inspired reward terms promote biomechanically natural motions, such as straight-knee stance and coordinated arm-leg swing, without requiring motion capture data. A structured curriculum progressively introduces gait complexity and expands command space over multiple phases. In simulation, the policy successfully achieves robust standing, walking, running, and gait transitions. On the real Unitree G1 humanoid, we validate standing, walking, and walk-to-stand transitions, demonstrating stable and coordinated locomotion. This work provides a scalable, reference-free solution toward versatile and naturalistic humanoid control across diverse modes and environments.

## 核心内容
We present a unified gait-conditioned reinforcement learning framework that enables humanoid robots to perform standing, walking, running, and smooth transitions within a single recurrent policy. A compact reward routing mechanism dynamically activates gait-specific objectives based on a one-hot gait ID, mitigating reward interference and supporting stable multi-gait learning. Human-inspired reward terms promote biomechanically natural motions, such as straight-knee stance and coordinated arm-leg swing, without requiring motion capture data. A structured curriculum progressively introduces gait complexity and expands command space over multiple phases. In simulation, the policy successfully achieves robust standing, walking, running, and gait transitions. On the real Unitree G1 humanoid, we validate standing, walking, and walk-to-stand transitions, demonstrating stable and coordinated locomotion. This work provides a scalable, reference-free solution toward versatile and naturalistic humanoid control across diverse modes and environments.

## 参考
- http://arxiv.org/abs/2505.20619v3

