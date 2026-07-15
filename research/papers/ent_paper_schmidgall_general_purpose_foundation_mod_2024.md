---
$id: ent_paper_schmidgall_general_purpose_foundation_mod_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: General-purpose foundation models for increased autonomy in robot-assisted surgery
  zh: RT-RAS
  ko: General-purpose foundation models for increased autonomy in robot-assisted surgery
summary:
  en: General-purpose foundation models for increased autonomy in robot-assisted surgery (RT-RAS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Johns Hopkins University, University of Utah, and published at Nat. Mac.
    Intell. 2024.
  zh: General-purpose foundation models for increased autonomy in robot-assisted surgery (RT-RAS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Johns Hopkins University, University of Utah, and published at Nat. Mac.
    Intell. 2024.
  ko: General-purpose foundation models for increased autonomy in robot-assisted surgery (RT-RAS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Johns Hopkins University, University of Utah, and published at Nat. Mac.
    Intell. 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- rt_ras
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.00678v1.
sources:
- id: src_001
  type: website
  title: RT-RAS source
  url: https://doi.org/10.1038/s42256-024-00917-4
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The dominant paradigm for end-to-end robot learning focuses on optimizing task-specific objectives that solve a single robotic problem such as picking up an object or reaching a target position. However, recent work on high-capacity models in robotics has shown promise toward being trained on large collections of diverse and task-agnostic datasets of video demonstrations. These models have shown impressive levels of generalization to unseen circumstances, especially as the amount of data and the model complexity scale. Surgical robot systems that learn from data have struggled to advance as quickly as other fields of robot learning for a few reasons: (1) there is a lack of existing large-scale open-source data to train models, (2) it is challenging to model the soft-body deformations that these robots work with during surgery because simulation cannot match the physical and visual complexity of biological tissue, and (3) surgical robots risk harming patients when tested in clinical trials and require more extensive safety measures. This perspective article aims to provide a path toward increasing robot autonomy in robot-assisted surgery through the development of a multi-modal, multi-task, vision-language-action model for surgical robots. Ultimately, we argue that surgical robots are uniquely positioned to benefit from general-purpose models and provide three guiding actions toward increased autonomy in robot-assisted surgery.

## 核心内容
The dominant paradigm for end-to-end robot learning focuses on optimizing task-specific objectives that solve a single robotic problem such as picking up an object or reaching a target position. However, recent work on high-capacity models in robotics has shown promise toward being trained on large collections of diverse and task-agnostic datasets of video demonstrations. These models have shown impressive levels of generalization to unseen circumstances, especially as the amount of data and the model complexity scale. Surgical robot systems that learn from data have struggled to advance as quickly as other fields of robot learning for a few reasons: (1) there is a lack of existing large-scale open-source data to train models, (2) it is challenging to model the soft-body deformations that these robots work with during surgery because simulation cannot match the physical and visual complexity of biological tissue, and (3) surgical robots risk harming patients when tested in clinical trials and require more extensive safety measures. This perspective article aims to provide a path toward increasing robot autonomy in robot-assisted surgery through the development of a multi-modal, multi-task, vision-language-action model for surgical robots. Ultimately, we argue that surgical robots are uniquely positioned to benefit from general-purpose models and provide three guiding actions toward increased autonomy in robot-assisted surgery.

## 参考
- http://arxiv.org/abs/2401.00678v1

