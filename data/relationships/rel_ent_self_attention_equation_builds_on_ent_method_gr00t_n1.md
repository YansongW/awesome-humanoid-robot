---
$id: rel_ent_self_attention_equation_builds_on_ent_method_gr00t_n1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_self_attention_equation
  name:
    en: Scaled Dot-Product Self-Attention
    zh: 缩放点积自注意力
target:
  id: ent_method_gr00t_n1
  name:
    en: GR00T N1
    zh: GR00T N1
domains:
  source_domain: 00_foundations
  target_domain: 07_ai_models_algorithms
description:
  en: Scaled Dot-Product Self-Attention builds on GR00T N1.
  zh: 缩放点积自注意力builds_onGR00T N1。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Scaled Dot-Product Self-Attention建立在VLA基础模型（如GR00T
    N1）之上。 | 证据: - `builds_on` → VLA foundation models（GR00T N1, OpenVLA, π0 等）'
sources:
- id: src_001
  type: other
  title: KG body of ent_self_attention_equation
  url: https://kg.rounds-tech.com/entry/ent_self_attention_equation/
  accessed_at: '2026-07-16'
---
