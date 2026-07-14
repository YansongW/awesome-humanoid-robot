---
$id: ent_paper_toward_reliable_sim_to_real_pr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
  zh: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
  ko: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
summary:
  en: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion is a 2026 work on locomotion
    for humanoid robots.
  zh: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion is a 2026 work on locomotion
    for humanoid robots.
  ko: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion is a 2026 work on locomotion
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
- toward_reliable_sim_to_real_pr
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.00678v4.
sources:
- id: src_001
  type: paper
  title: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion (arXiv)
  url: https://arxiv.org/abs/2602.00678
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning has shown strong promise for quadrupedal agile locomotion, even with proprioception-only sensing. In practice, however, sim-to-real gap and reward overfitting in complex terrains can produce policies that fail to transfer, while physical validation remains risky and inefficient. To address these challenges, we introduce a unified framework encompassing a Mixture-of-Experts (MoE) locomotion policy for robust multi-terrain representation with RoboGauge, a predictive assessment suite that quantifies sim-to-real transferability. The MoE policy employs a gated set of specialist experts to decompose latent terrain and command modeling, achieving superior deployment robustness and generalization via proprioception alone. RoboGauge further provides multi-dimensional proprioception-based metrics via sim-to-sim tests over terrains, difficulty levels, and domain randomizations, enabling reliable MoE policy selection without extensive physical trials. Experiments on a Unitree Go2 demonstrate robust locomotion on unseen challenging terrains, including snow, sand, stairs, slopes, and 30 cm obstacles. In dedicated high-speed tests, the robot reaches 4 m/s and exhibits an emergent narrow-width gait associated with improved stability at high velocity.

## 核心内容
Reinforcement learning has shown strong promise for quadrupedal agile locomotion, even with proprioception-only sensing. In practice, however, sim-to-real gap and reward overfitting in complex terrains can produce policies that fail to transfer, while physical validation remains risky and inefficient. To address these challenges, we introduce a unified framework encompassing a Mixture-of-Experts (MoE) locomotion policy for robust multi-terrain representation with RoboGauge, a predictive assessment suite that quantifies sim-to-real transferability. The MoE policy employs a gated set of specialist experts to decompose latent terrain and command modeling, achieving superior deployment robustness and generalization via proprioception alone. RoboGauge further provides multi-dimensional proprioception-based metrics via sim-to-sim tests over terrains, difficulty levels, and domain randomizations, enabling reliable MoE policy selection without extensive physical trials. Experiments on a Unitree Go2 demonstrate robust locomotion on unseen challenging terrains, including snow, sand, stairs, slopes, and 30 cm obstacles. In dedicated high-speed tests, the robot reaches 4 m/s and exhibits an emergent narrow-width gait associated with improved stability at high velocity.

## 参考
- http://arxiv.org/abs/2602.00678v4

