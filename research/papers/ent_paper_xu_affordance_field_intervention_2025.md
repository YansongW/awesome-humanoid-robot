---
$id: ent_paper_xu_affordance_field_intervention_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation'
  zh: AFI
  ko: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation'
summary:
  en: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation (AFI), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The University of Sydney, John Hopcropt Center for
    Computer Science, Shanghai Jiao Tong University.'
  zh: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation (AFI), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The University of Sydney, John Hopcropt Center for
    Computer Science, Shanghai Jiao Tong University.'
  ko: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation (AFI), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The University of Sydney, John Hopcropt Center for
    Computer Science, Shanghai Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- afi
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07472v1.
sources:
- id: src_001
  type: paper
  title: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.07472
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AFI source
  url: https://doi.org/10.48550/arXiv.2512.07472
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown great performance in robotic manipulation by mapping visual observations and language instructions directly to actions. However, they remain brittle under distribution shifts: when test scenarios change, VLAs often reproduce memorized trajectories instead of adapting to the updated scene, which is a failure mode we refer to as the "Memory Trap". This limitation stems from the end-to-end design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments. To compensate for this missing spatial understanding, 3D Spatial Affordance Fields (SAFs) can provide a geometric representation that highlights where interactions are physically feasible, offering explicit cues about regions the robot should approach or avoid. We therefore introduce Affordance Field Intervention (AFI), a lightweight hybrid framework that uses SAFs as an on-demand plug-in to guide VLA behavior. Our system detects memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions. A SAF-based scorer then selects trajectories with the highest cumulative affordance. Extensive experiments demonstrate that our method achieves an average improvement of 23.5% across different VLA backbones ($π_{0}$ and $π_{0.5}$) under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark, validating its effectiveness in enhancing VLA robustness to distribution shifts.

## 核心内容
Vision-Language-Action (VLA) models have shown great performance in robotic manipulation by mapping visual observations and language instructions directly to actions. However, they remain brittle under distribution shifts: when test scenarios change, VLAs often reproduce memorized trajectories instead of adapting to the updated scene, which is a failure mode we refer to as the "Memory Trap". This limitation stems from the end-to-end design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments. To compensate for this missing spatial understanding, 3D Spatial Affordance Fields (SAFs) can provide a geometric representation that highlights where interactions are physically feasible, offering explicit cues about regions the robot should approach or avoid. We therefore introduce Affordance Field Intervention (AFI), a lightweight hybrid framework that uses SAFs as an on-demand plug-in to guide VLA behavior. Our system detects memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions. A SAF-based scorer then selects trajectories with the highest cumulative affordance. Extensive experiments demonstrate that our method achieves an average improvement of 23.5% across different VLA backbones ($π_{0}$ and $π_{0.5}$) under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark, validating its effectiveness in enhancing VLA robustness to distribution shifts.

## 参考
- http://arxiv.org/abs/2512.07472v1

