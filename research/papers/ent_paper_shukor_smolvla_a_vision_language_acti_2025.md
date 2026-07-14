---
$id: ent_paper_shukor_smolvla_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics'
  zh: SmolVLA
  ko: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics'
summary:
  en: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (SmolVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay.'
  zh: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (SmolVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay.'
  ko: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (SmolVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay.'
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
- smolvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01844v1.
sources:
- id: src_001
  type: paper
  title: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv)'
  url: https://arxiv.org/abs/2506.01844
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SmolVLA source
  url: https://doi.org/10.48550/arXiv.2506.01844
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive--often with billions of parameters--leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## 核心内容
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive--often with billions of parameters--leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## 参考
- http://arxiv.org/abs/2506.01844v1

