---
$id: rel_ent_paper_reasoning_double_edged_sword_architectur_2026_evaluates_on_ent_benchmark_libero_plus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_reasoning_double_edged_sword_architectur_2026
  name:
    en: 'Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models'
    zh: 'Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models'
target:
  id: ent_benchmark_libero_plus
  name:
    en: LIBERO-Plus
    zh: LIBERO-Plus
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models is evaluated
    on LIBERO-Plus.'
  zh: 'Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models评测于LIBERO-Plus。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在LIBERO-Plus基准上评估其方法，并指出该基准只报告整体性能下降。 | 证据:
    此前LIBERO-Plus等基准只报告整体性能下降，无法回答扰动在视觉编码、推理、动作解码各阶段如何传播。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_reasoning_double_edged_sword_architectur_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_reasoning_double_edged_sword_architectur_2026/
  accessed_at: '2026-08-06'
---
