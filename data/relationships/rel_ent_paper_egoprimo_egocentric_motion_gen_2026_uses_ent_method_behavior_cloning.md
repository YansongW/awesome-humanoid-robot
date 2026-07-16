---
$id: rel_ent_paper_egoprimo_egocentric_motion_gen_2026_uses_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_egoprimo_egocentric_motion_gen_2026
  name:
    en: 'EgoPriMo: Egocentric Motion Generation for Interactive Humanoid Control'
    zh: EgoPriMo｜用于交互式人形控制的第一视角运动生成
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'EgoPriMo: Egocentric Motion Generation for Interactive Humanoid Control uses Behavior Cloning.'
  zh: EgoPriMo｜用于交互式人形控制的第一视角运动生成使用行为克隆。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: EgoPriMo在运动生成阶段使用了行为克隆（ACT）来提取运动模式。 | 证据: In
    the motion generation stage, EgoPriMo innovatively combines three technical pathways: a discriminator-generator framework
    based on Adversarial Motion Priors (AMP) to constrain motion naturalness, Behavior Cloning (ACT) to extract motion patterns
    f'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_egoprimo_egocentric_motion_gen_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_egoprimo_egocentric_motion_gen_2026/
  accessed_at: '2026-07-16'
---
