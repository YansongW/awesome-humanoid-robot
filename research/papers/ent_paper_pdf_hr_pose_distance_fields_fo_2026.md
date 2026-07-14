---
$id: ent_paper_pdf_hr_pose_distance_fields_fo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PDF-HR: Pose Distance Fields for Humanoid Robots'
  zh: 'PDF-HR: Pose Distance Fields for Humanoid Robots'
  ko: 'PDF-HR: Pose Distance Fields for Humanoid Robots'
summary:
  en: 'PDF-HR: Pose Distance Fields for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  zh: 'PDF-HR: Pose Distance Fields for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  ko: 'PDF-HR: Pose Distance Fields for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control for humanoid
    robots.'
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
- loco_manipulation
- pdf_hr
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04851v1.
sources:
- id: src_001
  type: paper
  title: 'PDF-HR: Pose Distance Fields for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2602.04851
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Pose and motion priors play a crucial role in humanoid robotics. Although such priors have been widely studied in human motion recovery (HMR) domain with a range of models, their adoption for humanoid robots remains limited, largely due to the scarcity of high-quality humanoid motion data. In this work, we introduce Pose Distance Fields for Humanoid Robots (PDF-HR), a lightweight prior that represents the robot pose distribution as a continuous and differentiable manifold. Given an arbitrary pose, PDF-HR predicts its distance to a large corpus of retargeted robot poses, yielding a smooth measure of pose plausibility that is well suited for optimization and control. PDF-HR can be integrated as a reward shaping term, a regularizer, or a standalone plausibility scorer across diverse pipelines. We evaluate PDF-HR on various humanoid tasks, including single-trajectory motion tracking, general motion tracking, style-based motion mimicry, and general motion retargeting. Experiments show that this plug-and-play prior consistently and substantially strengthens strong baselines. Code and models will be released.

## 核心内容
Pose and motion priors play a crucial role in humanoid robotics. Although such priors have been widely studied in human motion recovery (HMR) domain with a range of models, their adoption for humanoid robots remains limited, largely due to the scarcity of high-quality humanoid motion data. In this work, we introduce Pose Distance Fields for Humanoid Robots (PDF-HR), a lightweight prior that represents the robot pose distribution as a continuous and differentiable manifold. Given an arbitrary pose, PDF-HR predicts its distance to a large corpus of retargeted robot poses, yielding a smooth measure of pose plausibility that is well suited for optimization and control. PDF-HR can be integrated as a reward shaping term, a regularizer, or a standalone plausibility scorer across diverse pipelines. We evaluate PDF-HR on various humanoid tasks, including single-trajectory motion tracking, general motion tracking, style-based motion mimicry, and general motion retargeting. Experiments show that this plug-and-play prior consistently and substantially strengthens strong baselines. Code and models will be released.

## 参考
- http://arxiv.org/abs/2602.04851v1

