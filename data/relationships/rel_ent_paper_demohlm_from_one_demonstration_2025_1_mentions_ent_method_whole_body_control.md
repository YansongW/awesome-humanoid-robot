---
$id: rel_ent_paper_demohlm_from_one_demonstration_2025_1_mentions_ent_method_whole_body_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_demohlm_from_one_demonstration_2025_1
  name:
    en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation'
    zh: DemoHLM｜从单一示范到通用人形移动操作
target:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation mentions Whole-Body Control (WBC).'
  zh: DemoHLM｜从单一示范到通用人形移动操作提及全身控制（WBC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: DemoHLM mainly solves the closed-loop data problem:
    using camera images/multi-view observation, ontology state and joint sequence, teleoperation/exoskeleton data to collect
    human operation and robot state, and then through ACT/behavioral cloning imitation learning, whole-body controller/WBC/MPC,
    clo'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_demohlm_from_one_demonstration_2025_1
  url: https://kg.rounds-tech.com/entry/ent_paper_demohlm_from_one_demonstration_2025_1/
  accessed_at: '2026-07-16'
---
