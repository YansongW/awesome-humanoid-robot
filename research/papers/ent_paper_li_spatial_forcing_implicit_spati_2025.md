---
$id: ent_paper_li_spatial_forcing_implicit_spati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model'
  zh: Spatial Forcing
  ko: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model'
summary:
  en: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (Spatial Forcing), is a
    2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and
    Technology (Guangzhou), Tsinghua University, Westlake University, Zhejiang University, South China University of Technology.'
  zh: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (Spatial Forcing), is a
    2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and
    Technology (Guangzhou), Tsinghua University, Westlake University, Zhejiang University, South China University of Technology.'
  ko: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (Spatial Forcing), is a
    2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and
    Technology (Guangzhou), Tsinghua University, Westlake University, Zhejiang University, South China University of Technology.'
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
- spatial_forcing
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12276v2.
sources:
- id: src_001
  type: paper
  title: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (arXiv)'
  url: https://arxiv.org/abs/2510.12276
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Spatial Forcing source
  url: https://doi.org/10.48550/arXiv.2510.12276
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions. However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in the 3D physical world. Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets. Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators. We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs or depth estimators. SF aligns intermediate visual embeddings of VLAs with geometric representations produced by pretrained 3D foundation models. By enforcing alignment at intermediate layers, SF guides VLAs to encode richer spatial representations that enhance action precision. Extensive experiments in simulation and real-world environments demonstrate that SF achieves state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further accelerates training by up to 3.8x and improves data efficiency across diverse robotic tasks. Project page is at https://spatial-forcing.github.io/

## 核心内容
Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions. However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in the 3D physical world. Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets. Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators. We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs or depth estimators. SF aligns intermediate visual embeddings of VLAs with geometric representations produced by pretrained 3D foundation models. By enforcing alignment at intermediate layers, SF guides VLAs to encode richer spatial representations that enhance action precision. Extensive experiments in simulation and real-world environments demonstrate that SF achieves state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further accelerates training by up to 3.8x and improves data efficiency across diverse robotic tasks. Project page is at https://spatial-forcing.github.io/

## 参考
- http://arxiv.org/abs/2510.12276v2

