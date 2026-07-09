---
$id: ent_paper_athena_wbc_capability_aligned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body
    Control'
  zh: 'Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body
    Control'
  ko: ''
summary:
  en: "arXiv:2607.04837v1 Announce Type: new \nAbstract: Large-scale humanoid motion-tracking\
    \ controllers are commonly improved by reallocating training effort: difficult\
    \ motions are sampled more often, isolated into smaller subsets, or assigned to\
    \ specialized experts. We show that this view is incomplete. In strong whole-body-control\
    \ baselines, a residual set of feasible training clips remains unsolved even under\
    \ targeted training, especially for high-dynamic transitions and balance-critical\
    \ motions. These failures arise not only from insufficient exposure, but from\
    \ a mismatch between the motion demands and the effective capability induced by\
    \ the default training recipe. We propose Athena-WBC, a compact teacher-student\
    \ pipeline with capability-aligned policy experts for long-tail humanoid whole-body\
    \ control. Dynamic experts use a tracking-focused, constraint-aware objective\
    \ that removes conservative effort and temporal-control penalties while preserving\
    \ physical feasibility constraints; balance experts use a gravity curriculum to\
    \ improve early-training survivability. The resulting privileged teachers are\
    \ motion-routed for DAgger distillation and then compressed into a single controller\
    \ with deployable observations followed by RL fine-tuning. Experiments on a full-size\
    \ humanoid show improved recovery of training-set long-tail motions and better\
    \ held-out tracking than a strong SONIC-recipe baseline, using only a small number\
    \ of experts."
  zh: "arXiv:2607.04837v1 Announce Type: new \nAbstract: Large-scale humanoid motion-tracking\
    \ controllers are commonly improved by reallocating training effort: difficult\
    \ motions are sampled more often, isolated into smaller subsets, or assigned to\
    \ specialized experts. We show that this view is incomplete. In strong whole-body-control\
    \ baselines, a residual set of feasible training clips remains unsolved even under\
    \ targeted training, especially for high-dynamic transitions and balance-critical\
    \ motions. These failures arise not only from insufficient exposure, but from\
    \ a mismatch between the motion demands and the effective capability induced by\
    \ the default training recipe. We propose Athena-WBC, a compact teacher-student\
    \ pipeline with capability-aligned policy experts for long-tail humanoid whole-body\
    \ control. Dynamic experts use a tracking-focused, constraint-aware objective\
    \ that removes conservative effort and temporal-control penalties while preserving\
    \ physical feasibility constraints; balance experts use a gravity curriculum to\
    \ improve early-training survivability. The resulting privileged teachers are\
    \ motion-routed for DAgger distillation and then compressed into a single controller\
    \ with deployable observations followed by RL fine-tuning. Experiments on a full-size\
    \ humanoid show improved recovery of training-set long-tail motions and better\
    \ held-out tracking than a strong SONIC-recipe baseline, using only a small number\
    \ of experts."
  ko: ''
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
- robotics
- athena_wbc
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body
    Control (arXiv)'
  url: https://arxiv.org/abs/2607.04837
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.04837v1 Announce Type: new 
Abstract: Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused, constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.
