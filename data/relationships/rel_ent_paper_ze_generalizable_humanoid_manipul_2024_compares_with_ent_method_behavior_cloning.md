---
$id: rel_ent_paper_ze_generalizable_humanoid_manipul_2024_compares_with_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_paper_ze_generalizable_humanoid_manipul_2024
  name:
    en: Generalizable Humanoid Manipulation with 3D Diffusion Policies
    zh: 基于3D扩散策略的可泛化人形机器人操作
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Generalizable Humanoid Manipulation with 3D Diffusion Policies compares with Behavior Cloning.
  zh: 基于3D扩散策略的可泛化人形机器人操作compares_with行为克隆。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明iDP3与基线方法（如Behavior Cloning）进行比较，因此源与目标进行比较。
    | 证据: - **噪声鲁棒性**：iDP3算法有效抑制了遥操作数据中的抖动与轨迹偏差，相比基线方法（如Behavior Cloning）错误率降低40%。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_ze_generalizable_humanoid_manipul_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_ze_generalizable_humanoid_manipul_2024/
  accessed_at: '2026-07-31'
---
