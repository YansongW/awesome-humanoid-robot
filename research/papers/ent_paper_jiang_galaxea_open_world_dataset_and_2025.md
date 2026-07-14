---
$id: ent_paper_jiang_galaxea_open_world_dataset_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Galaxea Open-World Dataset and G0 Dual-System VLA Model
  zh: G0
  ko: Galaxea Open-World Dataset and G0 Dual-System VLA Model
summary:
  en: Galaxea Open-World Dataset and G0 Dual-System VLA Model (G0), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Galaxea.
  zh: Galaxea Open-World Dataset and G0 Dual-System VLA Model (G0), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Galaxea.
  ko: Galaxea Open-World Dataset and G0 Dual-System VLA Model (G0), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Galaxea.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- g0
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.00576v1.
sources:
- id: src_001
  type: paper
  title: Galaxea Open-World Dataset and G0 Dual-System VLA Model (arXiv)
  url: https://arxiv.org/abs/2509.00576
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: G0 source
  url: https://doi.org/10.48550/arXiv.2509.00576
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present Galaxea Open-World Dataset, a large-scale, diverse collection of robot behaviors recorded in authentic human living and working environments. All demonstrations are gathered using a consistent robotic embodiment, paired with precise subtask-level language annotations to facilitate both training and evaluation. Building on this dataset, we introduce G0, a dual-system framework that couples a Vision-Language Model (VLM) for multimodal planning with a Vision-Language-Action (VLA) model for fine-grained execution. G0 is trained using a three-stage curriculum: cross-embodiment pre-training, single-embodiment pre-training, and task-specific post-training. A comprehensive benchmark spanning tabletop manipulation, few-shot learning, and long-horizon mobile manipulation, demonstrates the effectiveness of our approach. In particular, we find that the single-embodiment pre-training stage, together with the Galaxea Open-World Dataset, plays a critical role in achieving strong performance.

## 核心内容
We present Galaxea Open-World Dataset, a large-scale, diverse collection of robot behaviors recorded in authentic human living and working environments. All demonstrations are gathered using a consistent robotic embodiment, paired with precise subtask-level language annotations to facilitate both training and evaluation. Building on this dataset, we introduce G0, a dual-system framework that couples a Vision-Language Model (VLM) for multimodal planning with a Vision-Language-Action (VLA) model for fine-grained execution. G0 is trained using a three-stage curriculum: cross-embodiment pre-training, single-embodiment pre-training, and task-specific post-training. A comprehensive benchmark spanning tabletop manipulation, few-shot learning, and long-horizon mobile manipulation, demonstrates the effectiveness of our approach. In particular, we find that the single-embodiment pre-training stage, together with the Galaxea Open-World Dataset, plays a critical role in achieving strong performance.

## 参考
- http://arxiv.org/abs/2509.00576v1

