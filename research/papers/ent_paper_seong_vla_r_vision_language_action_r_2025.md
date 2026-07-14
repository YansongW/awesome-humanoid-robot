---
$id: ent_paper_seong_vla_r_vision_language_action_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving'
  zh: VLA-R
  ko: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving'
summary:
  en: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving (VLA-R), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST.'
  zh: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving (VLA-R), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST.'
  ko: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving (VLA-R), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST.'
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
- vla_r
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.12405v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.12405
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-R source
  url: https://doi.org/10.48550/arXiv.2511.12405
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Exploring open-world situations in an end-to-end manner is a promising yet challenging task due to the need for strong generalization capabilities. In particular, end-to-end autonomous driving in unstructured outdoor environments often encounters conditions that were unfamiliar during training. In this work, we present Vision-Language Action Retrieval (VLA-R), an open-world end-to-end autonomous driving (OW-E2EAD) framework that integrates open-world perception with a novel vision-action retrieval paradigm. We leverage a frozen vision-language model for open-world detection and segmentation to obtain multi-scale, prompt-guided, and interpretable perception features without domain-specific tuning. A Q-Former bottleneck aggregates fine-grained visual representations with language-aligned visual features, bridging perception and action domains. To learn transferable driving behaviors, we introduce a vision-action contrastive learning scheme that aligns vision-language and action embeddings for effective open-world reasoning and action retrieval. Our experiments on a real-world robotic platform demonstrate strong generalization and exploratory performance in unstructured, unseen environments, even with limited data. Demo videos are provided in the supplementary material.

## 核心内容
Exploring open-world situations in an end-to-end manner is a promising yet challenging task due to the need for strong generalization capabilities. In particular, end-to-end autonomous driving in unstructured outdoor environments often encounters conditions that were unfamiliar during training. In this work, we present Vision-Language Action Retrieval (VLA-R), an open-world end-to-end autonomous driving (OW-E2EAD) framework that integrates open-world perception with a novel vision-action retrieval paradigm. We leverage a frozen vision-language model for open-world detection and segmentation to obtain multi-scale, prompt-guided, and interpretable perception features without domain-specific tuning. A Q-Former bottleneck aggregates fine-grained visual representations with language-aligned visual features, bridging perception and action domains. To learn transferable driving behaviors, we introduce a vision-action contrastive learning scheme that aligns vision-language and action embeddings for effective open-world reasoning and action retrieval. Our experiments on a real-world robotic platform demonstrate strong generalization and exploratory performance in unstructured, unseen environments, even with limited data. Demo videos are provided in the supplementary material.

## 参考
- http://arxiv.org/abs/2511.12405v1

