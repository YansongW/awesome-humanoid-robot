---
$id: ent_paper_h2_compact_human_humanoid_co_m_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies'
  zh: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies'
  ko: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies'
summary:
  en: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- h2_compact
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.17627v1.
sources:
- id: src_001
  type: website
  title: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies project page'
  url: https://h2compact.github.io/h2compact/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present a hierarchical policy-learning framework that enables a legged humanoid to cooperatively carry extended loads with a human partner using only haptic cues for intent inference. At the upper tier, a lightweight behavior-cloning network consumes six-axis force/torque streams from dual wrist-mounted sensors and outputs whole-body planar velocity commands that capture the leader's applied forces. At the lower tier, a deep-reinforcement-learning policy, trained under randomized payloads (0-3 kg) and friction conditions in Isaac Gym and validated in MuJoCo and on a real Unitree G1, maps these high-level twists to stable, under-load joint trajectories. By decoupling intent interpretation (force -> velocity) from legged locomotion (velocity -> joints), our method combines intuitive responsiveness to human inputs with robust, load-adaptive walking. We collect training data without motion-capture or markers, only synchronized RGB video and F/T readings, employing SAM2 and WHAM to extract 3D human pose and velocity. In real-world trials, our humanoid achieves cooperative carry-and-move performance (completion time, trajectory deviation, velocity synchrony, and follower-force) on par with a blindfolded human-follower baseline. This work is the first to demonstrate learned haptic guidance fused with full-body legged control for fluid human-humanoid co-manipulation. Code and videos are available on the H2-COMPACT website.

## 核心内容
We present a hierarchical policy-learning framework that enables a legged humanoid to cooperatively carry extended loads with a human partner using only haptic cues for intent inference. At the upper tier, a lightweight behavior-cloning network consumes six-axis force/torque streams from dual wrist-mounted sensors and outputs whole-body planar velocity commands that capture the leader's applied forces. At the lower tier, a deep-reinforcement-learning policy, trained under randomized payloads (0-3 kg) and friction conditions in Isaac Gym and validated in MuJoCo and on a real Unitree G1, maps these high-level twists to stable, under-load joint trajectories. By decoupling intent interpretation (force -> velocity) from legged locomotion (velocity -> joints), our method combines intuitive responsiveness to human inputs with robust, load-adaptive walking. We collect training data without motion-capture or markers, only synchronized RGB video and F/T readings, employing SAM2 and WHAM to extract 3D human pose and velocity. In real-world trials, our humanoid achieves cooperative carry-and-move performance (completion time, trajectory deviation, velocity synchrony, and follower-force) on par with a blindfolded human-follower baseline. This work is the first to demonstrate learned haptic guidance fused with full-body legged control for fluid human-humanoid co-manipulation. Code and videos are available on the H2-COMPACT website.

## 参考
- http://arxiv.org/abs/2505.17627v1

