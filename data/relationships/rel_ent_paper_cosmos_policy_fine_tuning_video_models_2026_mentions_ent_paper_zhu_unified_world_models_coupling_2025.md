---
$id: rel_ent_paper_cosmos_policy_fine_tuning_video_models_2026_mentions_ent_paper_zhu_unified_world_models_coupling_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_cosmos_policy_fine_tuning_video_models_2026
  name:
    en: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning'
    zh: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning'
target:
  id: ent_paper_zhu_unified_world_models_coupling_2025
  name:
    en: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets'
    zh: UWM
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning mentions Unified World Models: Coupling
    Video and Action Diffusion for Pretraining on Large Robotic Datasets.'
  zh: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning提及UWM。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 此前主流方案要么像 Diffusion Policy 那样从零训练动作扩散模型，浪费了视频生成模型已习得的物理与时空先验；要么像
    UVA/UWM 那样设计自定义统一架构，但无法直接加载预训练权重。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_cosmos_policy_fine_tuning_video_models_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_cosmos_policy_fine_tuning_video_models_2026/
  accessed_at: '2026-08-06'
---
