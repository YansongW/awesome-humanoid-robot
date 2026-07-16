---
$id: rel_ent_paper_hmc_learning_heterogeneous_met_2025_uses_ent_paper_action_chunking_with_transform_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_hmc_learning_heterogeneous_met_2025
  name:
    en: 'HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation'
    zh: HMC｜学习异构元控制以实现接触丰富的移动操作
target:
  id: ent_paper_action_chunking_with_transform_2023
  name:
    en: Action Chunking with Transformers
    zh: 基于Transformer的动作分块
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation uses Action Chunking with Transformers.'
  zh: HMC｜学习异构元控制以实现接触丰富的移动操作使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: HMC论文中明确提到使用ACT（Action Chunking with Transformers）的行为克隆模仿学习模块。
    | 证据: 这些多模态数据随后被送入一个基于ACT（Action Chunking with Transformers）的行为克隆模仿学习模块，该模块能够将原始的人类操作轨迹转化为可训练的关节位置/力矩命令、全身运动序列以及低层控制器的目标值。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_hmc_learning_heterogeneous_met_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_hmc_learning_heterogeneous_met_2025/
  accessed_at: '2026-07-16'
---
