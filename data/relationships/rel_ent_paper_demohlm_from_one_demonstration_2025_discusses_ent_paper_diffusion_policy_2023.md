---
$id: rel_ent_paper_demohlm_from_one_demonstration_2025_discusses_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: discusses
source:
  id: ent_paper_demohlm_from_one_demonstration_2025
  name:
    en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation'
    zh: DemoHLM｜从单一示范到通用人形移动操作
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation is evaluated on Diffusion Policy.'
  zh: DemoHLM｜从单一示范到通用人形移动操作评测于扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明源论文评估了Diffusion Policy架构，因此Diffusion Policy是被评估的对象。
    | 证据: 评估三种架构：MLP（动作分块）、ACT（CVAE 式 transformer）、Diffusion Policy。 | WP2.3 2026-08-06: type retyped evaluates_on->discusses
    after DeepSeek review. Reason: 目标是方法非基准. Original file rel_ent_paper_demohlm_from_one_demonstration_2025_evaluates_on_ent_paper_diffusion_policy_2023.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_demohlm_from_one_demonstration_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_demohlm_from_one_demonstration_2025/
  accessed_at: '2026-08-06'
---
