---
$id: ent_paper_sim_to_real_of_humanoid_locomo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection
  zh: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection
  ko: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection
summary:
  en: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection is a 2025 work on sim-to-real
    for humanoid robots.
  zh: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection is a 2025 work on sim-to-real
    for humanoid robots.
  ko: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection is a 2025 work on sim-to-real
    for humanoid robots.
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
- sim_to_real
- sim_to_real_of_humanoid_locomo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.06585v2.
sources:
- id: src_001
  type: paper
  title: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection (arXiv)
  url: https://arxiv.org/abs/2504.06585
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Prior sim-to-real methods for legged robots mostly rely on the domain randomization approach, where a fixed finite set of simulation parameters is randomized during training. Instead, our method adds state-dependent perturbations to the input joint torque used for forward simulation during the training phase. These state-dependent perturbations are designed to simulate a broader range of reality gaps than those captured by randomizing a fixed set of simulation parameters. Experimental results show that our method enables humanoid locomotion policies that achieve greater robustness against complex reality gaps unseen in the training domain.

## 核心内容
This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Prior sim-to-real methods for legged robots mostly rely on the domain randomization approach, where a fixed finite set of simulation parameters is randomized during training. Instead, our method adds state-dependent perturbations to the input joint torque used for forward simulation during the training phase. These state-dependent perturbations are designed to simulate a broader range of reality gaps than those captured by randomizing a fixed set of simulation parameters. Experimental results show that our method enables humanoid locomotion policies that achieve greater robustness against complex reality gaps unseen in the training domain.

## 参考
- http://arxiv.org/abs/2504.06585v2

