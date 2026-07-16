---
$id: rel_ent_method_pid_control_mentions_ent_method_impedance_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_method_pid_control
  name:
    en: PID Control
    zh: PID控制
target:
  id: ent_method_impedance_control
  name:
    en: Impedance Control
    zh: 阻抗控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: PID Control mentions Impedance Control.
  zh: PID控制提及阻抗控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: PID 控制调节位置或速度；阻抗控制进一步调节与环境的动态交互力。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_method_pid_control
  url: https://kg.rounds-tech.com/entry/ent_method_pid_control/
  accessed_at: '2026-07-16'
---
