---
$id: ent_paper_xu_wam_flow_parallel_coarse_to_fi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving'
  zh: WAM-Flow
  ko: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving'
summary:
  en: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (WAM-Flow), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Fudan University, Yinwang Intelligent
    Technology Co., Ltd..'
  zh: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (WAM-Flow), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Fudan University, Yinwang Intelligent
    Technology Co., Ltd..'
  ko: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (WAM-Flow), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Fudan University, Yinwang Intelligent
    Technology Co., Ltd..'
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
- vision_language_action
- vla
- wam_flow
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.06112v2.
sources:
- id: src_001
  type: paper
  title: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2512.06112
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WAM-Flow source
  url: https://doi.org/10.48550/arXiv.2512.06112
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

## 核心内容
We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

## 参考
- http://arxiv.org/abs/2512.06112v2

