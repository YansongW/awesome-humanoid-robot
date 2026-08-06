---
$id: rel_ent_paper_cosmos_policy_fine_tuning_video_models_2026_compares_with_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_paper_cosmos_policy_fine_tuning_video_models_2026
  name:
    en: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning'
    zh: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning'
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning compares with Diffusion Policy.'
  zh: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planningcompares_with扩散策略。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据将Cosmos Policy与Diffusion Policy进行对比，指出其从零训练动作扩散模型的缺点。
    | 证据: 此前主流方案要么像 Diffusion Policy 那样从零训练动作扩散模型，浪费了视频生成模型已习得的物理与时空先验；要么像 UVA/UWM 那样设计自定义统一架构，但无法直接加载预训练权重。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_cosmos_policy_fine_tuning_video_models_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_cosmos_policy_fine_tuning_video_models_2026/
  accessed_at: '2026-08-06'
---
