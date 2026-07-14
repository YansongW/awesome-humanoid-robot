---
$id: ent_paper_grover_enhancing_generalization_in_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations
  zh: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations
  ko: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations
summary:
  en: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (Enhancing Generalization
    in Vision-Language-Action Models by Preserving Pretrained Representations), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, Hillbot.
  zh: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (Enhancing Generalization
    in Vision-Language-Action Models by Preserving Pretrained Representations), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, Hillbot.
  ko: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (Enhancing Generalization
    in Vision-Language-Action Models by Preserving Pretrained Representations), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, Hillbot.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- enhancing_generalization_in_vi
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.11417v2.
sources:
- id: src_001
  type: paper
  title: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (arXiv)
  url: https://arxiv.org/abs/2509.11417
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations source
  url: https://doi.org/10.48550/arXiv.2509.11417
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization. We present a framework that better preserves pretrained features while adapting them for robot manipulation. Our approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances. Evaluations in simulation and on real robots show that our method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

## 核心内容
Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization. We present a framework that better preserves pretrained features while adapting them for robot manipulation. Our approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances. Evaluations in simulation and on real robots show that our method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

## 参考
- http://arxiv.org/abs/2509.11417v2

