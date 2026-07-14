---
$id: ent_paper_zhang_4d_vla_spatiotemporal_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration'
  zh: 4D-VLA
  ko: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration'
summary:
  en: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (4D-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, HUAWEI Noah''s Ark Lab, and published at NIPS25.'
  zh: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (4D-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, HUAWEI Noah''s Ark Lab, and published at NIPS25.'
  ko: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (4D-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, HUAWEI Noah''s Ark Lab, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 4d_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.22242v2.
sources:
- id: src_001
  type: paper
  title: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (arXiv)'
  url: https://arxiv.org/abs/2506.22242
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 4D-VLA source
  url: https://doi.org/10.48550/arXiv.2506.22242
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution-an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## 核心内容
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution-an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## 参考
- http://arxiv.org/abs/2506.22242v2

