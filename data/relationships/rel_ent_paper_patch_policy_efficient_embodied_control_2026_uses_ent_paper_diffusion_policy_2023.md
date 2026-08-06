---
$id: rel_ent_paper_patch_policy_efficient_embodied_control_2026_uses_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_patch_policy_efficient_embodied_control_2026
  name:
    en: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations'
    zh: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations'
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations is evaluated on Diffusion Policy.'
  zh: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations评测于扩散策略。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文评估了Diffusion Policy作为动作头之一。 | 证据: - 动作头在每帧最后一个
    patch token 处输出动作块（action chunk）；公式与动作头架构无关，评估了 VQ-BeT（混合分类-回归）与 Diffusion Policy（去噪）两种头。 | WP2.3 2026-08-06: type retyped
    evaluates_on->uses after DeepSeek review. Reason: 证据句表明论文评估了Diffusion Policy作为动作头，但Diffusion Policy是方法而非数据集，故evaluates_on类型错配，应改为uses。.
    Original file rel_ent_paper_patch_policy_efficient_embodied_control_2026_evaluates_on_ent_paper_diffusion_policy_2023.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_patch_policy_efficient_embodied_control_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_patch_policy_efficient_embodied_control_2026/
  accessed_at: '2026-08-06'
---
