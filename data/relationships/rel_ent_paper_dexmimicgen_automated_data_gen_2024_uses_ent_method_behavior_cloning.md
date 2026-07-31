---
$id: rel_ent_paper_dexmimicgen_automated_data_gen_2024_uses_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_dexmimicgen_automated_data_gen_2024
  name:
    en: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
    zh: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning uses Behavior Cloning.'
  zh: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning使用行为克隆。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: DexMimicGen采用行为克隆方法训练策略。 | 证据: - **策略学习**：采用行为克隆（Behavior
    Cloning）方法训练策略，并对比了不同数据量（如 500、1000、2000 条轨迹）对成功率的影响。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_dexmimicgen_automated_data_gen_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_dexmimicgen_automated_data_gen_2024/
  accessed_at: '2026-07-31'
---
