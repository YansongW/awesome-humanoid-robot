---
$id: rel_ent_paper_imitation_bc_dagger_diffusion_compares_with_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_paper_imitation_bc_dagger_diffusion
  name:
    en: Imitation Learning（BC / DAgger / Diffusion）
    zh: Imitation Learning（BC / DAgger / Diffusion）
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Imitation Learning（BC / DAgger / Diffusion） compares with Diffusion Policy.
  zh: Imitation Learning（BC / DAgger / Diffusion）compares_with扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文将自身方法与Diffusion Policy进行对比。 | 证据: - 相比 Diffusion
    Policy：论文未提及扩散模型，方法属于迭代优化框架，而非生成式建模。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_imitation_bc_dagger_diffusion
  url: https://kg.rounds-tech.com/entry/ent_paper_imitation_bc_dagger_diffusion/
  accessed_at: '2026-08-06'
---
