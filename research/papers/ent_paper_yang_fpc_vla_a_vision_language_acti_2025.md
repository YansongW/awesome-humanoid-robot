---
$id: ent_paper_yang_fpc_vla_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction'
  zh: FPC-VLA
  ko: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction'
summary:
  en: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction (FPC-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nankai University, Xiaomi EV, Northeastern
    University Shenyang, University of Macau.'
  zh: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction (FPC-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nankai University, Xiaomi EV, Northeastern
    University Shenyang, University of Macau.'
  ko: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction (FPC-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nankai University, Xiaomi EV, Northeastern
    University Shenyang, University of Macau.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fpc_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.04018v2.
sources:
- id: src_001
  type: paper
  title: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction (arXiv)'
  url: https://arxiv.org/abs/2509.04018
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FPC-VLA source
  url: https://doi.org/10.48550/arXiv.2509.04018
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robotic manipulation is a fundamental component of automation. However, traditional perception-planning pipelines often fall short in open-ended tasks due to limited flexibility, while the architecture of a single end-to-end Vision-Language-Action (VLA) offers promising capabilities but lacks crucial mechanisms for anticipating and recovering from failure. To address these challenges, we propose FPC-VLA, a dual-model framework that integrates VLA with a supervisor for failure prediction and correction. The supervisor evaluates action viability through vision-language queries and generates corrective strategies when risks arise, trained efficiently without manual labeling. A dual-stream fusion module further refines actions by leveraging past predictions. Evaluation results on multiple simulation platforms (SIMPLER and LIBERO) and robot embodiments (WidowX, Google Robot, Franka) show that FPC-VLA outperforms state-of-the-art models in both zero-shot and fine-tuned settings. Successful real-world deployments on diverse, long-horizon tasks confirm FPC-VLA's strong generalization and practical utility for building more reliable autonomous systems.

## 核心内容
Robotic manipulation is a fundamental component of automation. However, traditional perception-planning pipelines often fall short in open-ended tasks due to limited flexibility, while the architecture of a single end-to-end Vision-Language-Action (VLA) offers promising capabilities but lacks crucial mechanisms for anticipating and recovering from failure. To address these challenges, we propose FPC-VLA, a dual-model framework that integrates VLA with a supervisor for failure prediction and correction. The supervisor evaluates action viability through vision-language queries and generates corrective strategies when risks arise, trained efficiently without manual labeling. A dual-stream fusion module further refines actions by leveraging past predictions. Evaluation results on multiple simulation platforms (SIMPLER and LIBERO) and robot embodiments (WidowX, Google Robot, Franka) show that FPC-VLA outperforms state-of-the-art models in both zero-shot and fine-tuned settings. Successful real-world deployments on diverse, long-horizon tasks confirm FPC-VLA's strong generalization and practical utility for building more reliable autonomous systems.

## 参考
- http://arxiv.org/abs/2509.04018v2

