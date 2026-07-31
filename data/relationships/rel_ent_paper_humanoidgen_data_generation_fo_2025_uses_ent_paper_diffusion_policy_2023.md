---
$id: rel_ent_paper_humanoidgen_data_generation_fo_2025_uses_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_humanoidgen_data_generation_fo_2025
  name:
    en: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
    zh: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning uses Diffusion Policy.'
  zh: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning使用扩散策略。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文使用生成的演示数据训练扩散策略，即使用了扩散策略方法。 | 证据: - **策略评估**：使用生成的演示数据训练
    2D 与 3D 扩散策略（Diffusion Policy），在基准上测试成功率与泛化能力。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_humanoidgen_data_generation_fo_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_humanoidgen_data_generation_fo_2025/
  accessed_at: '2026-07-31'
---
