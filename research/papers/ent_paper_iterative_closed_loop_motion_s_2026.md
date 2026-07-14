---
$id: ent_paper_iterative_closed_loop_motion_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
  zh: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
  ko: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
summary:
  en: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control is a 2026 work on physics-based
    character animation for humanoid robots.
  zh: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control is a 2026 work on physics-based
    character animation for humanoid robots.
  ko: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control is a 2026 work on physics-based
    character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- iterative_closed_loop_motion_s
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.21599v2.
sources:
- id: src_001
  type: paper
  title: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control (arXiv)
  url: https://arxiv.org/abs/2602.21599
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Physics-based humanoid control relies on training with motion datasets that have diverse data distributions. However, the fixed difficulty distribution of datasets limits the performance ceiling of the trained control policies. Additionally, the method of acquiring high-quality data through professional motion capture systems is constrained by costs, making it difficult to achieve large-scale scalability. To address these issues, we propose a closed-loop automated motion data generation and iterative framework. It can generate high-quality motion data with rich action semantics, including martial arts, dance, combat, sports, gymnastics, and more. Furthermore, our framework enables difficulty iteration of policies and data through physical metrics and objective evaluations, allowing the trained tracker to break through its original difficulty limits. On the PHC single-primitive tracker, using only approximately 1/10 of the AMASS dataset size, the average failure rate on the test set (2201 clips) is reduced by 45% compared to the baseline. Finally, we conduct comprehensive ablation and comparative experiments to highlight the rationality and advantages of our framework.

## 核心内容
Physics-based humanoid control relies on training with motion datasets that have diverse data distributions. However, the fixed difficulty distribution of datasets limits the performance ceiling of the trained control policies. Additionally, the method of acquiring high-quality data through professional motion capture systems is constrained by costs, making it difficult to achieve large-scale scalability. To address these issues, we propose a closed-loop automated motion data generation and iterative framework. It can generate high-quality motion data with rich action semantics, including martial arts, dance, combat, sports, gymnastics, and more. Furthermore, our framework enables difficulty iteration of policies and data through physical metrics and objective evaluations, allowing the trained tracker to break through its original difficulty limits. On the PHC single-primitive tracker, using only approximately 1/10 of the AMASS dataset size, the average failure rate on the test set (2201 clips) is reduced by 45% compared to the baseline. Finally, we conduct comprehensive ablation and comparative experiments to highlight the rationality and advantages of our framework.

## 参考
- http://arxiv.org/abs/2602.21599v2

