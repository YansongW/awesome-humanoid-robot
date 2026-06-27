---
$id: rel_ent_self_attention_equation_derived_from_ent_principle_maximum_likelihood_estimation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: derived_from
source:
  id: ent_self_attention_equation
  name:
    en: Scaled Dot-Product Self-Attention
target:
  id: ent_principle_maximum_likelihood_estimation
  name:
    en: Maximum Likelihood Estimation
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: The self-attention equation is trained using objectives derived from maximum likelihood estimation.
  zh: 自注意力方程使用源自最大似然估计的目标函数进行训练。
  ko: 셀프 어텐션 방정식은 최대우도추정에서 유래한 목적 함수를 사용하여 학습된다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the VLA knowledge-chain demonstration.
sources:
- id: src_vaswani_2017
  type: paper
  title: 'Vaswani et al., Attention Is All You Need, NeurIPS 2017'
  url: https://arxiv.org/abs/1706.03762
  date: '2017-06-12'
  accessed_at: '2026-06-26'
---
