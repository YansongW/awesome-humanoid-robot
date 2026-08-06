---
$id: rel_ent_paper_open_aoe_open_egocentric_manipulation_da_2026_mentions_ent_dataset_droid
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_open_aoe_open_egocentric_manipulation_da_2026
  name:
    en: 'Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning'
    zh: 'Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning'
target:
  id: ent_dataset_droid
  name:
    en: DROID
    zh: DROID 机器人操作数据集
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: 'Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning mentions DROID.'
  zh: 'Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning提及DROID 机器人操作数据集。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: **重建与标注**：相机姿态由 DROID-W 恢复，鲁棒核针对手持和穿戴采集重新调参保持
    6-DoF 轨迹稳定；手部重建从双手检测器开始（在 AoE 收集的大规模第一人称数据上训练），HaWoR 恢复 3D MANO 网格，通过 SLAM 进行度量尺度对齐，全局束调整联合优化手部网格和相机轨迹于单一世界坐标系；视频分割为语义连贯的原子片段并用英文标注，人工审核纠正模型幻觉。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_open_aoe_open_egocentric_manipulation_da_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_open_aoe_open_egocentric_manipulation_da_2026/
  accessed_at: '2026-08-06'
---
