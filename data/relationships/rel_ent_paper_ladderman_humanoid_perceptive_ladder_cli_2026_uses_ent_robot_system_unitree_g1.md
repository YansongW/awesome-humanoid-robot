---
$id: rel_ent_paper_ladderman_humanoid_perceptive_ladder_cli_2026_uses_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_ladderman_humanoid_perceptive_ladder_cli_2026
  name:
    en: 'LadderMan: Learning Humanoid Perceptive Ladder Climbing'
    zh: 人形机器人感知式爬梯与梯上操作
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 Humanoid Robot
    zh: Unitree G1 人形机器人
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'LadderMan: Learning Humanoid Perceptive Ladder Climbing uses Unitree G1 Humanoid Robot.'
  zh: 人形机器人感知式爬梯与梯上操作使用Unitree G1 人形机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: LadderMan使用Unitree G1人形机器人进行梯子攀爬实验。 | 证据: LadderMan
    提出了一套两阶段学习流水线，使 Unitree G1 人形机器人在零样本 sim-to-real 条件下，仅凭单一参考动作即可稳健攀爬多种几何构型的梯子，并支持在梯上进行遥操作任务。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_ladderman_humanoid_perceptive_ladder_cli_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_ladderman_humanoid_perceptive_ladder_cli_2026/
  accessed_at: '2026-08-06'
---
