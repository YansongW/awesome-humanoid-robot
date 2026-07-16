---
$id: rel_ent_paper_interaction_dynamics_for_dexte_2026_uses_ent_component_leap_hand
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_interaction_dynamics_for_dexte_2026
  name:
    en: Interaction Dynamics for Dexterous Manipulation
    zh: Interaction Dynamics for Dexterous Manipulation
target:
  id: ent_component_leap_hand
  name:
    en: LEAP Hand
    zh: LEAP 灵巧手
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: Interaction Dynamics for Dexterous Manipulation uses LEAP Hand.
  zh: Interaction Dynamics for Dexterous Manipulation使用LEAP 灵巧手。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文提到架构扩展到16自由度的LEAP Hand MuJoCo模型，表明论文使用了LEAP
    Hand。 | 证据: The realized first-move stiffness (18$\to$323\,Nm/rad with update rate) is independently verified, and the
    architecture scales to a 16-DOF LEAP Hand MuJoCo model, recovering from 2.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_interaction_dynamics_for_dexte_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_interaction_dynamics_for_dexte_2026/
  accessed_at: '2026-07-16'
---
