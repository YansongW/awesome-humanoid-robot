---
$id: ent_paper_ye_latent_action_pretraining_from_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latent Action Pretraining from Videos
  zh: LAPA
  ko: Latent Action Pretraining from Videos
summary:
  en: Latent Action Pretraining from Videos (LAPA), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by KAIST, University of Washington, Microsoft Research, NVIDIA, Allen Institute for AI, and published at ICLR
    2024.
  zh: Latent Action Pretraining from Videos (LAPA), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by KAIST, University of Washington, Microsoft Research, NVIDIA, Allen Institute for AI, and published at ICLR
    2024.
  ko: Latent Action Pretraining from Videos (LAPA), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by KAIST, University of Washington, Microsoft Research, NVIDIA, Allen Institute for AI, and published at ICLR
    2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- lapa
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.11758v2.
sources:
- id: src_001
  type: paper
  title: LAPA source
  url: https://openreview.net/forum?id=VYOe2eBQeh
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model.

## 核心内容
We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model.

## 参考
- http://arxiv.org/abs/2410.11758v2

