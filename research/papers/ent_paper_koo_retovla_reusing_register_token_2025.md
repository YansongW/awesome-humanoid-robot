---
$id: ent_paper_koo_retovla_reusing_register_token_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models'
  zh: RetoVLA
  ko: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models'
summary:
  en: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (RetoVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by School of Computing, Gachon University.'
  zh: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (RetoVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by School of Computing, Gachon University.'
  ko: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (RetoVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by School of Computing, Gachon University.'
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
- retovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21243v2.
sources:
- id: src_001
  type: paper
  title: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2509.21243
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RetoVLA source
  url: https://doi.org/10.48550/arXiv.2509.21243
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens-learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg

## 核心内容
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens-learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg

## 参考
- http://arxiv.org/abs/2509.21243v2

