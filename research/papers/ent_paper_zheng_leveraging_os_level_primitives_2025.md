---
$id: ent_paper_zheng_leveraging_os_level_primitives_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Leveraging OS-Level Primitives for Robotic Action Management
  zh: AMS
  ko: Leveraging OS-Level Primitives for Robotic Action Management
summary:
  en: Leveraging OS-Level Primitives for Robotic Action Management (AMS), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai Jiao Tong University, Southern University of Science and Technology.
  zh: Leveraging OS-Level Primitives for Robotic Action Management (AMS), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai Jiao Tong University, Southern University of Science and Technology.
  ko: Leveraging OS-Level Primitives for Robotic Action Management (AMS), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai Jiao Tong University, Southern University of Science and Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ams
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.10259v1.
sources:
- id: src_001
  type: paper
  title: Leveraging OS-Level Primitives for Robotic Action Management (arXiv)
  url: https://arxiv.org/abs/2508.10259
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AMS source
  url: https://doi.org/10.48550/arXiv.2508.10259
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level.   In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## 核心内容
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level.   In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## 参考
- http://arxiv.org/abs/2508.10259v1

