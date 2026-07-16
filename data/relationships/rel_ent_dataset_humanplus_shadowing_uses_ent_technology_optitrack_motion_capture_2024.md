---
$id: rel_ent_dataset_humanplus_shadowing_uses_ent_technology_optitrack_motion_capture_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_dataset_humanplus_shadowing
  name:
    en: HumanPlus Shadowing Dataset
    zh: HumanPlus Shadowing数据集
target:
  id: ent_technology_optitrack_motion_capture_2024
  name:
    en: OptiTrack Motion Capture
    zh: OptiTrack 动作捕捉
domains:
  source_domain: 09_data_datasets
  target_domain: 09_data_datasets
description:
  en: HumanPlus Shadowing Dataset uses OptiTrack Motion Capture.
  zh: HumanPlus Shadowing数据集使用OptiTrack 动作捕捉。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 影子数据收集过程可能使用了OptiTrack运动捕捉技术。'
sources:
- id: src_001
  type: other
  title: KG body of ent_dataset_humanplus_shadowing
  url: https://kg.rounds-tech.com/entry/ent_dataset_humanplus_shadowing/
  accessed_at: '2026-07-16'
---
