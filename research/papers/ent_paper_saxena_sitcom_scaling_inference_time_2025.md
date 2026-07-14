---
$id: ent_paper_saxena_sitcom_scaling_inference_time_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SITCOM: Scaling Inference-Time COMpute for VLAs'
  zh: SITCOM
  ko: 'SITCOM: Scaling Inference-Time COMpute for VLAs'
summary:
  en: 'SITCOM: Scaling Inference-Time COMpute for VLAs (SITCOM), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Carnegie Mellon University.'
  zh: 'SITCOM: Scaling Inference-Time COMpute for VLAs (SITCOM), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Carnegie Mellon University.'
  ko: 'SITCOM: Scaling Inference-Time COMpute for VLAs (SITCOM), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Carnegie Mellon University.'
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
- sitcom
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.04041v1.
sources:
- id: src_001
  type: paper
  title: 'SITCOM: Scaling Inference-Time COMpute for VLAs (arXiv)'
  url: https://arxiv.org/abs/2510.04041
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SITCOM source
  url: https://doi.org/10.48550/arXiv.2510.04041
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning robust robotic control policies remains a major challenge due to the high cost of collecting labeled data, limited generalization to unseen environments, and difficulties in planning over long horizons. While Vision-Language-Action (VLA) models offer a promising solution by grounding natural language instructions into single-step control commands, they often lack mechanisms for lookahead and struggle with compounding errors in dynamic tasks. In this project, we introduce Scaling Inference-Time COMpute for VLAs (SITCOM), a framework that augments any pretrained VLA with model-based rollouts and reward-based trajectory selection, inspired by Model Predictive Control algorithm. SITCOM leverages a learned dynamics model to simulate multi-step action rollouts to select the best candidate plan for real-world execution, transforming one-shot VLAs into robust long-horizon planners. We develop an efficient transformer-based dynamics model trained on large-scale BridgeV2 data and fine-tuned on SIMPLER environments to bridge the Real2Sim gap, and score candidate rollouts using rewards from simulator. Through comprehensive evaluation across multiple tasks and settings in the SIMPLER environment, we demonstrate that SITCOM when combined with a good reward function can significantly improve task completion rate from 48% to 72% using trained dynamics model.

## 核心内容
Learning robust robotic control policies remains a major challenge due to the high cost of collecting labeled data, limited generalization to unseen environments, and difficulties in planning over long horizons. While Vision-Language-Action (VLA) models offer a promising solution by grounding natural language instructions into single-step control commands, they often lack mechanisms for lookahead and struggle with compounding errors in dynamic tasks. In this project, we introduce Scaling Inference-Time COMpute for VLAs (SITCOM), a framework that augments any pretrained VLA with model-based rollouts and reward-based trajectory selection, inspired by Model Predictive Control algorithm. SITCOM leverages a learned dynamics model to simulate multi-step action rollouts to select the best candidate plan for real-world execution, transforming one-shot VLAs into robust long-horizon planners. We develop an efficient transformer-based dynamics model trained on large-scale BridgeV2 data and fine-tuned on SIMPLER environments to bridge the Real2Sim gap, and score candidate rollouts using rewards from simulator. Through comprehensive evaluation across multiple tasks and settings in the SIMPLER environment, we demonstrate that SITCOM when combined with a good reward function can significantly improve task completion rate from 48% to 72% using trained dynamics model.

## 参考
- http://arxiv.org/abs/2510.04041v1

