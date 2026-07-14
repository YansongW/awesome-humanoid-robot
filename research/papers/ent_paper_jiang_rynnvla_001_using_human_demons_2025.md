---
$id: ent_paper_jiang_rynnvla_001_using_human_demons_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation'
  zh: RynnVLA-001
  ko: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation'
summary:
  en: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation (RynnVLA-001), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
  zh: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation (RynnVLA-001), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
  ko: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation (RynnVLA-001), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
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
- rynnvla_001
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15212v1.
sources:
- id: src_001
  type: paper
  title: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.15212
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RynnVLA-001 source
  url: https://doi.org/10.48550/arXiv.2509.15212
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents RynnVLA-001, a vision-language-action(VLA) model built upon large-scale video generative pretraining from human demonstrations. We propose a novel two-stage pretraining methodology. The first stage, Ego-Centric Video Generative Pretraining, trains an Image-to-Video model on 12M ego-centric manipulation videos to predict future frames conditioned on an initial frame and a language instruction. The second stage, Human-Centric Trajectory-Aware Modeling, extends this by jointly predicting future keypoint trajectories, thereby effectively bridging visual frame prediction with action prediction. Furthermore, to enhance action representation, we propose ActionVAE, a variational autoencoder that compresses sequences of actions into compact latent embeddings, reducing the complexity of the VLA output space. When finetuned on the same downstream robotics datasets, RynnVLA-001 achieves superior performance over state-of-the-art baselines, demonstrating that the proposed pretraining strategy provides a more effective initialization for VLA models.

## 核心内容
This paper presents RynnVLA-001, a vision-language-action(VLA) model built upon large-scale video generative pretraining from human demonstrations. We propose a novel two-stage pretraining methodology. The first stage, Ego-Centric Video Generative Pretraining, trains an Image-to-Video model on 12M ego-centric manipulation videos to predict future frames conditioned on an initial frame and a language instruction. The second stage, Human-Centric Trajectory-Aware Modeling, extends this by jointly predicting future keypoint trajectories, thereby effectively bridging visual frame prediction with action prediction. Furthermore, to enhance action representation, we propose ActionVAE, a variational autoencoder that compresses sequences of actions into compact latent embeddings, reducing the complexity of the VLA output space. When finetuned on the same downstream robotics datasets, RynnVLA-001 achieves superior performance over state-of-the-art baselines, demonstrating that the proposed pretraining strategy provides a more effective initialization for VLA models.

## 参考
- http://arxiv.org/abs/2509.15212v1

