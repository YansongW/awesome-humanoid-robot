---
$id: rel_ent_paper_capvector_transferable_capability_vector_2026_uses_ent_paper_li_spatial_forcing_implicit_spati_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_capvector_transferable_capability_vector_2026
  name:
    en: 'CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models'
    zh: 'CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models'
target:
  id: ent_paper_li_spatial_forcing_implicit_spati_2025
  name:
    en: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model'
    zh: Spatial Forcing
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models uses Spatial
    Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model.'
  zh: 'CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models使用Spatial
    Forcing。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: CapVector 使用 Spatial Forcing 作为辅助目标 SFT 来提取能力向量。
    | 证据: CapVector 提出一种在参数空间中提取、合并“能力向量”的方法，将辅助目标 SFT（如 Spatial Forcing）带来的通用能力增益迁移到预训练 VLA 模型，使下游仅用标准 SFT 即可获得接近辅助训练的性能与效率，且额外开销可忽略。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_capvector_transferable_capability_vector_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_capvector_transferable_capability_vector_2026/
  accessed_at: '2026-08-06'
---
