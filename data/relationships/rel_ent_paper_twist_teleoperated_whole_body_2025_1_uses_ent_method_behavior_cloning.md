---
$id: rel_ent_paper_twist_teleoperated_whole_body_2025_1_uses_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_twist_teleoperated_whole_body_2025_1
  name:
    en: 'TWIST: Teleoperated Whole-Body Imitation System'
    zh: TWIST｜遥控全身模仿系统
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 09_data_datasets
  target_domain: 07_ai_models_algorithms
description:
  en: 'TWIST: Teleoperated Whole-Body Imitation System uses Behavior Cloning.'
  zh: TWIST｜遥控全身模仿系统使用行为克隆。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: TWIST系统通过行为克隆（Behavior Cloning）对动作序列进行精细化调整。
    | 证据: On this basis, the system employs Proximal Policy Optimization (PPO) and Reinforcement Learning (RL) strategies
    for initial training, followed by fine-tuning action sequences through Behavior Cloning (ACT) and imitation learning,
    ultimately outputtin'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_twist_teleoperated_whole_body_2025_1
  url: https://kg.rounds-tech.com/entry/ent_paper_twist_teleoperated_whole_body_2025_1/
  accessed_at: '2026-07-16'
---
