---
$id: rel_ent_paper_kaidanov_the_role_of_domain_randomizati_2024_uses_ent_method_domain_randomization
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_kaidanov_the_role_of_domain_randomizati_2024
  name:
    en: The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control
    zh: 领域随机化在训练全身人形机器人控制扩散策略中的作用
target:
  id: ent_method_domain_randomization
  name:
    en: Domain Randomization
    zh: 域随机化
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control uses Domain Randomization.
  zh: 领域随机化在训练全身人形机器人控制扩散策略中的作用使用域随机化。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在IsaacGym仿真中使用了域随机化条件来生成合成演示。 | 证据: In a simulated
    IsaacGym environment, we generate synthetic demonstrations by training Adversarial Motion Prior (AMP) agents under various
    Domain Randomization (DR) conditions, and we compare DPs fitted to datasets of different size and diversity.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_kaidanov_the_role_of_domain_randomizati_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_kaidanov_the_role_of_domain_randomizati_2024/
  accessed_at: '2026-07-16'
---
