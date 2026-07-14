---
$id: ent_paper_contrastive_representation_lea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
  zh: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
  ko: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
summary:
  en: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion is a 2025 work on
    sim-to-real for humanoid robots.
  zh: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion is a 2025 work on
    sim-to-real for humanoid robots.
  ko: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion is a 2025 work on
    sim-to-real for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- contrastive_representation_lea
- humanoid
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.12858v1.
sources:
- id: src_001
  type: paper
  title: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2509.12858
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning has produced remarkable advances in humanoid locomotion, yet a fundamental dilemma persists for real-world deployment: policies must choose between the robustness of reactive proprioceptive control or the proactivity of complex, fragile perception-driven systems. This paper resolves this dilemma by introducing a paradigm that imbues a purely proprioceptive policy with proactive capabilities, achieving the foresight of perception without its deployment-time costs. Our core contribution is a contrastive learning framework that compels the actor's latent state to encode privileged environmental information from simulation. Crucially, this ``distilled awareness" empowers an adaptive gait clock, allowing the policy to proactively adjust its rhythm based on an inferred understanding of the terrain. This synergy resolves the classic trade-off between rigid, clocked gaits and unstable clock-free policies. We validate our approach with zero-shot sim-to-real transfer to a full-sized humanoid, demonstrating highly robust locomotion over challenging terrains, including 30 cm high steps and 26.5° slopes, proving the effectiveness of our method. Website: https://lu-yidan.github.io/cra-loco.

## 核心内容
Reinforcement learning has produced remarkable advances in humanoid locomotion, yet a fundamental dilemma persists for real-world deployment: policies must choose between the robustness of reactive proprioceptive control or the proactivity of complex, fragile perception-driven systems. This paper resolves this dilemma by introducing a paradigm that imbues a purely proprioceptive policy with proactive capabilities, achieving the foresight of perception without its deployment-time costs. Our core contribution is a contrastive learning framework that compels the actor's latent state to encode privileged environmental information from simulation. Crucially, this ``distilled awareness" empowers an adaptive gait clock, allowing the policy to proactively adjust its rhythm based on an inferred understanding of the terrain. This synergy resolves the classic trade-off between rigid, clocked gaits and unstable clock-free policies. We validate our approach with zero-shot sim-to-real transfer to a full-sized humanoid, demonstrating highly robust locomotion over challenging terrains, including 30 cm high steps and 26.5° slopes, proving the effectiveness of our method. Website: https://lu-yidan.github.io/cra-loco.

## 参考
- http://arxiv.org/abs/2509.12858v1

