---
$id: ent_paper_deng_graspvla_a_grasping_foundation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data'
  zh: GraspVLA
  ko: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data'
summary:
  en: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (GraspVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong
    Kong, Beijing Academy of Artificial Intelligence, and published at CoRL25.'
  zh: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (GraspVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong
    Kong, Beijing Academy of Artificial Intelligence, and published at CoRL25.'
  ko: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (GraspVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong
    Kong, Beijing Academy of Artificial Intelligence, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- graspvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03233v3.
sources:
- id: src_001
  type: paper
  title: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (arXiv)'
  url: https://arxiv.org/abs/2505.03233
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GraspVLA source
  url: https://doi.org/10.48550/arXiv.2505.03233
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training. However, existing models rely heavily on real-world data, which is costly and labor-intensive to collect. Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. To bridge this gap, we explore the feasibility of training Vision-Language-Action models entirely with large-scale synthetic action data. We curate SynGrasp-1B, a billion-frame robotic grasping dataset generated in simulation with photorealistic rendering and extensive domain randomization. Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks. GraspVLA integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chain-of-Thought process, enabling joint training on synthetic action data and Internet semantics data. This design helps mitigate sim-to-real gaps and facilitates the transfer of learned actions to a broader range of Internet-covered objects, achieving open-vocabulary generalization in grasping. Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA's advanced zero-shot generalizability and few-shot adaptability to specific human preferences. We will release SynGrasp-1B dataset and pre-trained weights to benefit the community.

## 核心内容
Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training. However, existing models rely heavily on real-world data, which is costly and labor-intensive to collect. Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. To bridge this gap, we explore the feasibility of training Vision-Language-Action models entirely with large-scale synthetic action data. We curate SynGrasp-1B, a billion-frame robotic grasping dataset generated in simulation with photorealistic rendering and extensive domain randomization. Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks. GraspVLA integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chain-of-Thought process, enabling joint training on synthetic action data and Internet semantics data. This design helps mitigate sim-to-real gaps and facilitates the transfer of learned actions to a broader range of Internet-covered objects, achieving open-vocabulary generalization in grasping. Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA's advanced zero-shot generalizability and few-shot adaptability to specific human preferences. We will release SynGrasp-1B dataset and pre-trained weights to benefit the community.

## 参考
- http://arxiv.org/abs/2505.03233v3

