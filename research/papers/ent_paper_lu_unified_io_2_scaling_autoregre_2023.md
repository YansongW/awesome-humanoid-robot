---
$id: ent_paper_lu_unified_io_2_scaling_autoregre_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action'
  zh: Unified-IO 2
  ko: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action'
summary:
  en: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action (Unified-IO 2), is
    a 2023 large vision-language-action model for robotic manipulation, introduced by Allen Institute for AI, University of
    Illinois Urbana-Champaign, University of Washington, and published at CVPR 2023.'
  zh: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action (Unified-IO 2), is
    a 2023 large vision-language-action model for robotic manipulation, introduced by Allen Institute for AI, University of
    Illinois Urbana-Champaign, University of Washington, and published at CVPR 2023.'
  ko: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action (Unified-IO 2), is
    a 2023 large vision-language-action model for robotic manipulation, introduced by Allen Institute for AI, University of
    Illinois Urbana-Champaign, University of Washington, and published at CVPR 2023.'
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
- unified_io_2
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.17172v1.
sources:
- id: src_001
  type: website
  title: Unified-IO 2 source
  url: https://doi.org/10.1109/CVPR52733.2024.02497
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

## 核心内容
We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

## 参考
- http://arxiv.org/abs/2312.17172v1

