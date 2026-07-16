---
$id: rel_ent_oem_figure_ai_mentions_ent_component_manufacturer_nvidia
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_oem_figure_ai
  name:
    en: Figure AI
    zh: Figure AI
target:
  id: ent_component_manufacturer_nvidia
  name:
    en: NVIDIA
    zh: 英伟达
domains:
  source_domain: 06_design_engineering
  target_domain: 02_components
description:
  en: Figure AI mentions NVIDIA.
  zh: Figure AI提及英伟达。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: | 接口/通信 | 双 NVIDIA GPU 计算、6×RGB 相机、语音交互 | 公开资料
    |'
sources:
- id: src_001
  type: other
  title: KG body of ent_oem_figure_ai
  url: https://kg.rounds-tech.com/entry/ent_oem_figure_ai/
  accessed_at: '2026-07-16'
---
