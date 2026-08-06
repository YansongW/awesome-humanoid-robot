---
$id: rel_ent_paper_pi0_2024_mentions_ent_dataset_droid
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_pi0_2024
  name:
    en: 'π0: A Vision-Language-Action Flow Model for General Robot Control'
    zh: π0：用于通用机器人控制的视觉-语言-动作流模型
target:
  id: ent_dataset_droid
  name:
    en: DROID
    zh: DROID 机器人操作数据集
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: 'π0: A Vision-Language-Action Flow Model for General Robot Control mentions DROID.'
  zh: π0：用于通用机器人控制的视觉-语言-动作流模型提及DROID 机器人操作数据集。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 1% 开源数据（OXE、Bridge v2、DROID）+ 自有 903M 时间步（106M
    单臂 + 797M 双臂），68 个任务、7 种机器人配置；每个任务-机器人组合按 n^0.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_pi0_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_pi0_2024/
  accessed_at: '2026-08-06'
---
