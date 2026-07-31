---
$id: rel_ent_paper_wen_tinyvla_towards_fast_data_effi_2024_uses_ent_method_diffusion_policy
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_wen_tinyvla_towards_fast_data_effi_2024
  name:
    en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
    zh: TinyVLA
target:
  id: ent_method_diffusion_policy
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation uses Diffusion Policy.'
  zh: TinyVLA使用扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据明确说明TinyVLA在微调阶段集成扩散策略（Diffusion Policy），即TinyVLA使用Diffusion
    Policy作为解码器。 | 证据: - **扩散策略解码器**：在微调阶段集成扩散策略（Diffusion Policy），将视觉-语言特征映射为连续动作序列，增强动作生成的精确性与平滑性。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_wen_tinyvla_towards_fast_data_effi_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_wen_tinyvla_towards_fast_data_effi_2024/
  accessed_at: '2026-07-31'
---
