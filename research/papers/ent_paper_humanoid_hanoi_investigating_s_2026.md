---
$id: ent_paper_humanoid_hanoi_investigating_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement'
  zh: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement'
  ko: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement'
summary:
  en: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement is a 2026 work on loco-manipulation
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
- humanoid_hanoi
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.13850v3.
sources:
- id: src_001
  type: paper
  title: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement (arXiv)'
  url: https://arxiv.org/abs/2602.13850
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We investigate a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level. In our architecture, all skills execute through a shared, task-agnostic whole-body controller (WBC), providing a consistent closed-loop interface for skill composition, in contrast to non-shared designs that use separate low-level controllers per skill. We find that naively reusing the same pretrained WBC can reduce robustness over long horizons, as new skills and their compositions induce shifted state and command distributions. We address this with a simple data aggregation procedure that augments shared-WBC training with rollouts from closed-loop skill execution under domain randomization. To evaluate the approach, we introduce Humanoid Hanoi, a long-horizon Tower-of-Hanoi box rearrangement benchmark, and report results in simulation and on the Digit V3 humanoid robot, demonstrating fully autonomous rearrangement over extended horizons and quantifying the benefits of the shared-WBC approach over non-shared baselines. Project page: https://osudrl.github.io/Humanoid_Hanoi/

## 核心内容
We investigate a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level. In our architecture, all skills execute through a shared, task-agnostic whole-body controller (WBC), providing a consistent closed-loop interface for skill composition, in contrast to non-shared designs that use separate low-level controllers per skill. We find that naively reusing the same pretrained WBC can reduce robustness over long horizons, as new skills and their compositions induce shifted state and command distributions. We address this with a simple data aggregation procedure that augments shared-WBC training with rollouts from closed-loop skill execution under domain randomization. To evaluate the approach, we introduce Humanoid Hanoi, a long-horizon Tower-of-Hanoi box rearrangement benchmark, and report results in simulation and on the Digit V3 humanoid robot, demonstrating fully autonomous rearrangement over extended horizons and quantifying the benefits of the shared-WBC approach over non-shared baselines. Project page: https://osudrl.github.io/Humanoid_Hanoi/

## 参考
- http://arxiv.org/abs/2602.13850v3

