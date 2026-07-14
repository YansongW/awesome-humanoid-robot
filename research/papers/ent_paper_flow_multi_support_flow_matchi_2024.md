---
$id: ent_paper_flow_multi_support_flow_matchi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation'
  zh: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation'
  ko: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation'
summary:
  en: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation is a 2024 work on loco-manipulation
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
- flow_multi_support
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.12381v2.
sources:
- id: src_001
  type: paper
  title: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation (arXiv)'
  url: https://arxiv.org/abs/2407.12381
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation project page'
  url: https://www.youtube.com/watch?v=OyXojqRasHU
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots could benefit from using their upper bodies for support contacts, enhancing their workspace, stability, and ability to perform contact-rich and pushing tasks. In this paper, we propose a unified approach that combines an optimization-based multi-contact whole-body controller with Flow Matching, a recently introduced method capable of generating multi-modal trajectory distributions for imitation learning. In simulation, we show that Flow Matching is more appropriate for robotics than Diffusion and traditional behavior cloning. On a real full-size humanoid robot (Talos), we demonstrate that our approach can learn a whole-body non-prehensile box-pushing task and that the robot can close dishwasher drawers by adding contacts with its free hand when needed for balance. We also introduce a shared autonomy mode for assisted teleoperation, providing automatic contact placement for tasks not covered in the demonstrations. Full experimental videos are available at: https://hucebot.github.io/flow_multisupport_website/

## 核心内容
Humanoid robots could benefit from using their upper bodies for support contacts, enhancing their workspace, stability, and ability to perform contact-rich and pushing tasks. In this paper, we propose a unified approach that combines an optimization-based multi-contact whole-body controller with Flow Matching, a recently introduced method capable of generating multi-modal trajectory distributions for imitation learning. In simulation, we show that Flow Matching is more appropriate for robotics than Diffusion and traditional behavior cloning. On a real full-size humanoid robot (Talos), we demonstrate that our approach can learn a whole-body non-prehensile box-pushing task and that the robot can close dishwasher drawers by adding contacts with its free hand when needed for balance. We also introduce a shared autonomy mode for assisted teleoperation, providing automatic contact placement for tasks not covered in the demonstrations. Full experimental videos are available at: https://hucebot.github.io/flow_multisupport_website/

## 参考
- http://arxiv.org/abs/2407.12381v2

