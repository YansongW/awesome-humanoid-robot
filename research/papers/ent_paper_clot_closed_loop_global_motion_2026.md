---
$id: ent_paper_clot_closed_loop_global_motion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
  zh: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
  ko: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
summary:
  en: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation is a 2026 work on teleoperation for
    humanoid robots.'
  zh: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation is a 2026 work on teleoperation for
    humanoid robots.'
  ko: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation is a 2026 work on teleoperation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- clot
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.15060v2.
sources:
- id: src_001
  type: paper
  title: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2602.15060
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long timehorizons. However, directly imposing global tracking rewards in reinforcement learning, often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found in our website.

## 核心内容
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long timehorizons. However, directly imposing global tracking rewards in reinforcement learning, often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found in our website.

## 参考
- http://arxiv.org/abs/2602.15060v2

