---
$id: rel_ent_paper_axis_growable_community_driven_data_engi_2026_evaluates_on_ent_benchmark_libero_plus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_axis_growable_community_driven_data_engi_2026
  name:
    en: 'AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation'
    zh: 'AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation'
target:
  id: ent_benchmark_libero_plus
  name:
    en: LIBERO-Plus
    zh: LIBERO-Plus
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation is evaluated on LIBERO-Plus.'
  zh: 'AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation评测于LIBERO-Plus。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据明确说明在LIBERO-Plus鲁棒性套件上进行评估。 | 证据: 评估在 LIBERO-Plus
    鲁棒性套件上进行，沿七个扰动轴（Camera、Light、Sensor Noise、Background、Layout、Language、Robot），每个（任务、扰动轴）对固定回滚预算为常数 K。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_axis_growable_community_driven_data_engi_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_axis_growable_community_driven_data_engi_2026/
  accessed_at: '2026-08-06'
---
