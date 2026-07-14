---
$id: ent_paper_sendai_leave_no_observation_behind_re_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks'
  zh: A2C2
  ko: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks'
summary:
  en: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks (A2C2), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The University of Tokyo.'
  zh: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks (A2C2), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The University of Tokyo.'
  ko: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks (A2C2), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The University of Tokyo.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a2c2
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23224v1.
sources:
- id: src_001
  type: paper
  title: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks (arXiv)'
  url: https://arxiv.org/abs/2509.23224
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: A2C2 source
  url: https://doi.org/10.48550/arXiv.2509.23224
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To improve efficiency and temporal coherence, Vision-Language-Action (VLA) models often predict action chunks; however, this action chunking harms reactivity under inference delay and long horizons. We introduce Asynchronous Action Chunk Correction (A2C2), which is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk. The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction. This preserves the base model's competence while restoring closed-loop responsiveness. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC). On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, our method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay. Since the correction head is small and fast, there is minimal overhead compared to the inference of large VLA models. These results indicate that A2C2 is an effective, plug-in mechanism for deploying high-capacity chunking policies in real-time control.

## 核心内容
To improve efficiency and temporal coherence, Vision-Language-Action (VLA) models often predict action chunks; however, this action chunking harms reactivity under inference delay and long horizons. We introduce Asynchronous Action Chunk Correction (A2C2), which is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk. The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction. This preserves the base model's competence while restoring closed-loop responsiveness. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC). On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, our method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay. Since the correction head is small and fast, there is minimal overhead compared to the inference of large VLA models. These results indicate that A2C2 is an effective, plug-in mechanism for deploying high-capacity chunking policies in real-time control.

## 参考
- http://arxiv.org/abs/2509.23224v1

