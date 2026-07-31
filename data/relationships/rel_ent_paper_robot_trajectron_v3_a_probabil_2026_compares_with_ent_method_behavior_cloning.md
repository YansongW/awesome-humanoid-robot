---
$id: rel_ent_paper_robot_trajectron_v3_a_probabil_2026_compares_with_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_paper_robot_trajectron_v3_a_probabil_2026
  name:
    en: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation'
    zh: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation'
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation compares with Behavior Cloning.'
  zh: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulationcompares_with行为克隆。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文将行为克隆作为基线方法进行比较。 | 证据: - **轨迹预测精度**：在仿真环境中，RT-V3
    在轨迹预测任务上达到高精度，其平均位移误差（ADE）与最终位移误差（FDE）均优于基线方法（如 Behavior Cloning、Conditional VAE）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_robot_trajectron_v3_a_probabil_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_robot_trajectron_v3_a_probabil_2026/
  accessed_at: '2026-07-31'
---
