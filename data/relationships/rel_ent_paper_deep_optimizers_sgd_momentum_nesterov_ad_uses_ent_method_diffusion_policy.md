---
$id: rel_ent_paper_deep_optimizers_sgd_momentum_nesterov_ad_uses_ent_method_diffusion_policy
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_deep_optimizers_sgd_momentum_nesterov_ad
  name:
    en: Deep Learning Optimizers — SGD / Momentum / Nesterov / Adagrad / RMSProp / Adadelta / Adam / AdamW / Lion
    zh: Deep Learning Optimizers — SGD / Momentum / Nesterov / Adagrad / RMSProp / Adadelta / Adam / AdamW / Lion
target:
  id: ent_method_diffusion_policy
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Deep Learning Optimizers — SGD / Momentum / Nesterov / Adagrad / RMSProp / Adadelta / Adam / AdamW / Lion uses Diffusion
    Policy.
  zh: Deep Learning Optimizers — SGD / Momentum / Nesterov / Adagrad / RMSProp / Adadelta / Adam / AdamW / Lion使用扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 扩散策略等生成模型的训练也依赖这些优化器。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_deep_optimizers_sgd_momentum_nesterov_ad
  url: https://kg.rounds-tech.com/entry/ent_paper_deep_optimizers_sgd_momentum_nesterov_ad/
  accessed_at: '2026-07-31'
---
