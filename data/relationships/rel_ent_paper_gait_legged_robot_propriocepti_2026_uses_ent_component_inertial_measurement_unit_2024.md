---
$id: rel_ent_paper_gait_legged_robot_propriocepti_2026_uses_ent_component_inertial_measurement_unit_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_gait_legged_robot_propriocepti_2026
  name:
    en: 'GAIT: Legged Robot Proprioceptive State Estimation with Attention over Inertial-Leg Tokens'
    zh: GAIT：用「惯性-腿部」分词与注意力做足式机器人本体感知状态估计
target:
  id: ent_component_inertial_measurement_unit_2024
  name:
    en: Inertial Measurement Unit
    zh: 惯性测量单元
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'GAIT: Legged Robot Proprioceptive State Estimation with Attention over Inertial-Leg Tokens uses Inertial Measurement
    Unit.'
  zh: GAIT：用「惯性-腿部」分词与注意力做足式机器人本体感知状态估计使用惯性测量单元。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用惯性测量单元（IMU）的时间序列数据作为输入。 | 证据: The method
    innovatively models the time-series data from an Inertial Measurement Unit (IMU) and leg joint encoders as an "inertial-leg"
    token sequence, and utilizes an attention mechanism to fuse multimodal information, thereby achieving high-precisi'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_gait_legged_robot_propriocepti_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_gait_legged_robot_propriocepti_2026/
  accessed_at: '2026-07-16'
---
