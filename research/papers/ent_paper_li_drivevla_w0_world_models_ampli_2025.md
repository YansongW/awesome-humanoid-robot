---
$id: ent_paper_li_drivevla_w0_world_models_ampli_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving'
  zh: DriveVLA-W0
  ko: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving'
summary:
  en: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving (DriveVLA-W0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Yinwang Intelligent Technology Co. Ltd., NLPR, Institute of Automation,
    Chinese Academy of Sciences (CASIA).'
  zh: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving (DriveVLA-W0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Yinwang Intelligent Technology Co. Ltd., NLPR, Institute of Automation,
    Chinese Academy of Sciences (CASIA).'
  ko: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving (DriveVLA-W0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Yinwang Intelligent Technology Co. Ltd., NLPR, Institute of Automation,
    Chinese Academy of Sciences (CASIA).'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- drivevla_w0
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12796v2.
sources:
- id: src_001
  type: paper
  title: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2510.12796
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DriveVLA-W0 source
  url: https://doi.org/10.48550/arXiv.2510.12796
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Scaling Vision-Language-Action (VLA) models on large-scale data offers a promising path to achieving a more generalized driving intelligence. However, VLA models are limited by a ``supervision deficit'': the vast model capacity is supervised by sparse, low-dimensional actions, leaving much of their representational power underutilized. To remedy this, we propose \textbf{DriveVLA-W0}, a training paradigm that employs world modeling to predict future images. This task generates a dense, self-supervised signal that compels the model to learn the underlying dynamics of the driving environment. We showcase the paradigm's versatility by instantiating it for two dominant VLA archetypes: an autoregressive world model for VLAs that use discrete visual tokens, and a diffusion world model for those operating on continuous visual features. Building on the rich representations learned from world modeling, we introduce a lightweight action expert to address the inference latency for real-time deployment. Extensive experiments on the NAVSIM v1/v2 benchmark and a 680x larger in-house dataset demonstrate that DriveVLA-W0 significantly outperforms BEV and VLA baselines. Crucially, it amplifies the data scaling law, showing that performance gains accelerate as the training dataset size increases.

## 核心内容
Scaling Vision-Language-Action (VLA) models on large-scale data offers a promising path to achieving a more generalized driving intelligence. However, VLA models are limited by a ``supervision deficit'': the vast model capacity is supervised by sparse, low-dimensional actions, leaving much of their representational power underutilized. To remedy this, we propose \textbf{DriveVLA-W0}, a training paradigm that employs world modeling to predict future images. This task generates a dense, self-supervised signal that compels the model to learn the underlying dynamics of the driving environment. We showcase the paradigm's versatility by instantiating it for two dominant VLA archetypes: an autoregressive world model for VLAs that use discrete visual tokens, and a diffusion world model for those operating on continuous visual features. Building on the rich representations learned from world modeling, we introduce a lightweight action expert to address the inference latency for real-time deployment. Extensive experiments on the NAVSIM v1/v2 benchmark and a 680x larger in-house dataset demonstrate that DriveVLA-W0 significantly outperforms BEV and VLA baselines. Crucially, it amplifies the data scaling law, showing that performance gains accelerate as the training dataset size increases.

## 参考
- http://arxiv.org/abs/2510.12796v2

