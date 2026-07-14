---
$id: ent_paper_spectral_normalization_for_lip_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion
  zh: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion
  ko: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion
summary:
  en: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.
  zh: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.
  ko: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- spectral_normalization_for_lip
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.08246v1.
sources:
- id: src_001
  type: paper
  title: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2504.08246
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) has shown great potential in training agile and adaptable controllers for legged robots, enabling them to learn complex locomotion behaviors directly from experience. However, policies trained in simulation often fail to transfer to real-world robots due to unrealistic assumptions such as infinite actuator bandwidth and the absence of torque limits. These conditions allow policies to rely on abrupt, high-frequency torque changes, which are infeasible for real actuators with finite bandwidth.   Traditional methods address this issue by penalizing aggressive motions through regularization rewards, such as joint velocities, accelerations, and energy consumption, but they require extensive hyperparameter tuning. Alternatively, Lipschitz-Constrained Policies (LCP) enforce finite bandwidth action control by penalizing policy gradients, but their reliance on gradient calculations introduces significant GPU memory overhead. To overcome this limitation, this work proposes Spectral Normalization (SN) as an efficient replacement for enforcing Lipschitz continuity. By constraining the spectral norm of network weights, SN effectively limits high-frequency policy fluctuations while significantly reducing GPU memory usage. Experimental evaluations in both simulation and real-world humanoid robot show that SN achieves performance comparable to gradient penalty methods while enabling more efficient parallel training.

## 核心内容
Reinforcement learning (RL) has shown great potential in training agile and adaptable controllers for legged robots, enabling them to learn complex locomotion behaviors directly from experience. However, policies trained in simulation often fail to transfer to real-world robots due to unrealistic assumptions such as infinite actuator bandwidth and the absence of torque limits. These conditions allow policies to rely on abrupt, high-frequency torque changes, which are infeasible for real actuators with finite bandwidth.   Traditional methods address this issue by penalizing aggressive motions through regularization rewards, such as joint velocities, accelerations, and energy consumption, but they require extensive hyperparameter tuning. Alternatively, Lipschitz-Constrained Policies (LCP) enforce finite bandwidth action control by penalizing policy gradients, but their reliance on gradient calculations introduces significant GPU memory overhead. To overcome this limitation, this work proposes Spectral Normalization (SN) as an efficient replacement for enforcing Lipschitz continuity. By constraining the spectral norm of network weights, SN effectively limits high-frequency policy fluctuations while significantly reducing GPU memory usage. Experimental evaluations in both simulation and real-world humanoid robot show that SN achieves performance comparable to gradient penalty methods while enabling more efficient parallel training.

## 参考
- http://arxiv.org/abs/2504.08246v1

