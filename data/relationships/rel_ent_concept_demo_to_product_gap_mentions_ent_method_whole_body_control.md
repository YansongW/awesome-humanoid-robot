---
$id: rel_ent_concept_demo_to_product_gap_mentions_ent_method_whole_body_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_concept_demo_to_product_gap
  name:
    en: Demo-to-Product Gap
    zh: 演示指标与产品指标的鸿沟
target:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
domains:
  source_domain: 11_applications_markets
  target_domain: 07_ai_models_algorithms
description:
  en: Demo-to-Product Gap mentions Whole-Body Control (WBC).
  zh: 演示指标与产品指标的鸿沟提及全身控制（WBC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: ->|MPC+WBC| C1[ASIMO 2000]'
sources:
- id: src_001
  type: other
  title: KG body of ent_concept_demo_to_product_gap
  url: https://kg.rounds-tech.com/entry/ent_concept_demo_to_product_gap/
  accessed_at: '2026-07-16'
---
