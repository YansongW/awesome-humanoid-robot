---
$id: rel_ent_paper_green_vla_staged_vision_language_action_2026_mentions_ent_paper_qu_eo_1_interleaved_vision_text_a_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_green_vla_staged_vision_language_action_2026
  name:
    en: 'Green-VLA: Staged Vision-Language-Action Model for Generalist Robots'
    zh: 'Green-VLA: Staged Vision-Language-Action Model for Generalist Robots'
target:
  id: ent_paper_qu_eo_1_interleaved_vision_text_a_2025
  name:
    en: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control'
    zh: EO-1
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Green-VLA: Staged Vision-Language-Action Model for Generalist Robots mentions EO-1: Interleaved Vision-Text-Action
    Pretraining for General Robot Control.'
  zh: 'Green-VLA: Staged Vision-Language-Action Model for Generalist Robots提及EO-1。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 现有显式推理 VLA（如 EO-1、WALL-OSS）依赖自回归循环，延迟高；Green-VLA
    用流匹配动作专家 + SDPA 注意力内核 + 减少去噪步数，在保持高成功率的同时压缩推理开销。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_green_vla_staged_vision_language_action_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_green_vla_staged_vision_language_action_2026/
  accessed_at: '2026-08-06'
---
