---
$id: rel_ent_paper_homie_humanoid_loco_manipulati_2025_1_mentions_ent_method_whole_body_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_homie_humanoid_loco_manipulati_2025_1
  name:
    en: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit'
    zh: HOMIE｜具有同构外骨骼驾驶舱的人形移动操作
target:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
domains:
  source_domain: 09_data_datasets
  target_domain: 07_ai_models_algorithms
description:
  en: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit mentions Whole-Body Control (WBC).'
  zh: HOMIE｜具有同构外骨骼驾驶舱的人形移动操作提及全身控制（WBC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: HOMIE mainly solves the data closed loop: it
    uses ontology state and joint sequence, teleoperation/exoskeleton data, and simulation interaction data to collect human
    operation and robot state, and then converts it into trainable and reusable terrain/scene representation through PPO/RL
    strategy train'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_homie_humanoid_loco_manipulati_2025_1
  url: https://kg.rounds-tech.com/entry/ent_paper_homie_humanoid_loco_manipulati_2025_1/
  accessed_at: '2026-07-16'
---
