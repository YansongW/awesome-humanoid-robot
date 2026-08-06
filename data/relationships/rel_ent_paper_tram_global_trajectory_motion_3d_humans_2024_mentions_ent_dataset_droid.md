---
$id: rel_ent_paper_tram_global_trajectory_motion_3d_humans_2024_mentions_ent_dataset_droid
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_tram_global_trajectory_motion_3d_humans_2024
  name:
    en: 'TRAM: Global Trajectory and Motion of 3D Humans from in-the-wild Videos'
    zh: 野外视频中的全局人体轨迹与动作恢复
target:
  id: ent_dataset_droid
  name:
    en: DROID
    zh: DROID 机器人操作数据集
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: 'TRAM: Global Trajectory and Motion of 3D Humans from in-the-wild Videos mentions DROID.'
  zh: 野外视频中的全局人体轨迹与动作恢复提及DROID 机器人操作数据集。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 核心贡献在于将鲁棒且度量尺度的 Masked DROID-SLAM 与视频 Transformer
    人体运动回归器 VIMO 结合，在 EMDB 上实现根轨迹误差（RTE）3.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_tram_global_trajectory_motion_3d_humans_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_tram_global_trajectory_motion_3d_humans_2024/
  accessed_at: '2026-08-06'
---
