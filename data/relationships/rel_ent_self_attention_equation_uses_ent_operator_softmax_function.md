---
$id: rel_ent_self_attention_equation_uses_ent_operator_softmax_function
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_self_attention_equation
  name:
    en: Scaled Dot-Product Self-Attention
    ko: ''
target:
  id: ent_operator_softmax_function
  name:
    en: Softmax Function
    ko: ''
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: The self-attention equation uses the softmax operator to normalize query-key scores.
  zh: 自注意力方程使用 softmax 算子对 query-key 分数进行归一化。
  ko: 셀프 어텐션 방정식은 query-key 점수를 정규화하기 위해 소프트맥스 연산자를 사용한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the VLA knowledge-chain demonstration.
sources:
- id: src_vaswani_2017
  type: paper
  title: Vaswani et al., Attention Is All You Need, NeurIPS 2017
  url: https://arxiv.org/abs/1706.03762
  date: '2017-06-12'
  accessed_at: '2026-06-26'
---
