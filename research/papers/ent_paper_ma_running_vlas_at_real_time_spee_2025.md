---
$id: ent_paper_ma_running_vlas_at_real_time_spee_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Running VLAs at Real-time Speed
  zh: Running VLAs at Real-time Speed
  ko: Running VLAs at Real-time Speed
summary:
  en: Running VLAs at Real-time Speed (Running VLAs at Real-time Speed), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Dexmal, StepFun.
  zh: Running VLAs at Real-time Speed (Running VLAs at Real-time Speed), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Dexmal, StepFun.
  ko: Running VLAs at Real-time Speed (Running VLAs at Real-time Speed), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Dexmal, StepFun.
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
- running_vlas_at_real_time_spee
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26742v1.
sources:
- id: src_001
  type: paper
  title: Running VLAs at Real-time Speed (arXiv)
  url: https://arxiv.org/abs/2510.26742
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Running VLAs at Real-time Speed source
  url: https://doi.org/10.48550/arXiv.2510.26742
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we show how to run pi0-level multi-view VLA at 30Hz frame rate and at most 480Hz trajectory frequency using a single consumer GPU. This enables dynamic and real-time tasks that were previously believed to be unattainable by large VLA models. To achieve it, we introduce a bag of strategies to eliminate the overheads in model inference. The real-world experiment shows that the pi0 policy with our strategy achieves a 100% success rate in grasping a falling pen task. Based on the results, we further propose a full streaming inference framework for real-time robot control of VLA. Code is available at https://github.com/Dexmal/realtime-vla.

## 核心内容
In this paper, we show how to run pi0-level multi-view VLA at 30Hz frame rate and at most 480Hz trajectory frequency using a single consumer GPU. This enables dynamic and real-time tasks that were previously believed to be unattainable by large VLA models. To achieve it, we introduce a bag of strategies to eliminate the overheads in model inference. The real-world experiment shows that the pi0 policy with our strategy achieves a 100% success rate in grasping a falling pen task. Based on the results, we further propose a full streaming inference framework for real-time robot control of VLA. Code is available at https://github.com/Dexmal/realtime-vla.

## 参考
- http://arxiv.org/abs/2510.26742v1

