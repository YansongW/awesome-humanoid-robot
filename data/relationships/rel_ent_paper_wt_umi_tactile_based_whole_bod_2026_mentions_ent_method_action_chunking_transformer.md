---
$id: rel_ent_paper_wt_umi_tactile_based_whole_bod_2026_mentions_ent_method_action_chunking_transformer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_wt_umi_tactile_based_whole_bod_2026
  name:
    en: 'WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning'
    zh: WT-UMI｜通过力监督接触感知规划进行基于触觉的全身操作
target:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
domains:
  source_domain: 09_data_datasets
  target_domain: 07_ai_models_algorithms
description:
  en: 'WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning mentions Action Chunking
    with Transformers (ACT).'
  zh: WT-UMI｜通过力监督接触感知规划进行基于触觉的全身操作提及动作分块变压器（ACT）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: WT-UMI mainly solves the data closed loop: using
    camera images/multi-view observation, teleoperation/exoskeleton data, contact force/tactile signals to collect human operation
    and robot state, and then through ACT/behavioral cloning imitation learning, diffusion strategy/flow matching to transform
    i'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_wt_umi_tactile_based_whole_bod_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_wt_umi_tactile_based_whole_bod_2026/
  accessed_at: '2026-07-16'
---
