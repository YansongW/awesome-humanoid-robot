---
$id: ent_paper_li_qdepth_vla_quantized_depth_pre_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models'
  zh: QDepth-VLA
  ko: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models'
summary:
  en: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models (QDepth-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, University
    of the Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Science, Beijing Zhongke Huiling Robot
    Technology Co.'
  zh: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models (QDepth-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, University
    of the Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Science, Beijing Zhongke Huiling Robot
    Technology Co.'
  ko: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models (QDepth-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, University
    of the Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Science, Beijing Zhongke Huiling Robot
    Technology Co.'
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
- qdepth_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14836v3.
sources:
- id: src_001
  type: paper
  title: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.14836
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: QDepth-VLA source
  url: https://doi.org/10.48550/arXiv.2510.14836
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Spatial perception and reasoning are crucial for Vision-Language-Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. To address this limitation, we propose QDepth-VLA, a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues. Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

## 核心内容
Spatial perception and reasoning are crucial for Vision-Language-Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. To address this limitation, we propose QDepth-VLA, a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues. Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

## 参考
- http://arxiv.org/abs/2510.14836v3

