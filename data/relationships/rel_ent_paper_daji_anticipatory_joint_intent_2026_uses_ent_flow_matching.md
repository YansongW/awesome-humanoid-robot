---
$id: rel_ent_paper_daji_anticipatory_joint_intent_2026_uses_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_daji_anticipatory_joint_intent_2026
  name:
    en: 'Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control'
    zh: 'Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control'
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: 'Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control uses Flow matching.'
  zh: 'Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control使用流匹配。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据描述了Flow matching的路径和损失函数，表明源论文使用了Flow matching方法。
    | 证据: Flow matching path X_s = (1-s)ε + sX_0, loss L_Flow = E[‖v_θ(X_s, s, C) - (X_0 - ε)‖²₂], time sampling s = 0.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_daji_anticipatory_joint_intent_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_daji_anticipatory_joint_intent_2026/
  accessed_at: '2026-08-06'
---
