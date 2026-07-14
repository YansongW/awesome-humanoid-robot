---
$id: ent_paper_bi_motus_a_unified_latent_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Motus: A Unified Latent Action World Model'
  zh: Motus
  ko: 'Motus: A Unified Latent Action World Model'
summary:
  en: 'Motus: A Unified Latent Action World Model (Motus), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Bosch, Tsinghua University, Peking University, Horizon Robotics.'
  zh: 'Motus: A Unified Latent Action World Model (Motus), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Bosch, Tsinghua University, Peking University, Horizon Robotics.'
  ko: 'Motus: A Unified Latent Action World Model (Motus), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Bosch, Tsinghua University, Peking University, Horizon Robotics.'
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
- motus
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13030v2.
sources:
- id: src_001
  type: paper
  title: 'Motus: A Unified Latent Action World Model (arXiv)'
  url: https://arxiv.org/abs/2512.13030
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Motus source
  url: https://doi.org/10.48550/arXiv.2512.13030
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios(improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## 核心内容
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios(improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## 参考
- http://arxiv.org/abs/2512.13030v2

