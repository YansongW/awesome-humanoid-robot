---
$id: ent_paper_learning_soccer_skills_for_hum_2026_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
  zh: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
  ko: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
summary:
  en: 'Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework is a 2026 work on loco-manipulation
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
- humanoid
- learning_soccer_skills_for_hum
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.05310v1.
sources:
- id: src_001
  type: paper
  title: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework (arXiv)'
  url: https://arxiv.org/abs/2602.05310
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions-including static or rolling balls, various positions, and disturbances-while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## 核心内容
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions-including static or rolling balls, various positions, and disturbances-while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## 参考
- http://arxiv.org/abs/2602.05310v1

