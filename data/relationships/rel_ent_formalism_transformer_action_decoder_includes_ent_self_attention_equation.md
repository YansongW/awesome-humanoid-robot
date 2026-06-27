---
$id: rel_ent_formalism_transformer_action_decoder_includes_ent_self_attention_equation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: includes
source:
  id: ent_formalism_transformer_action_decoder
  name:
    en: Transformer Action Decoder Formalism
target:
  id: ent_self_attention_equation
  name:
    en: Scaled Dot-Product Self-Attention
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: The Transformer action decoder includes scaled dot-product self-attention as a core equation.
  zh: Transformer 动作解码器包含缩放点积自注意力作为核心方程。
  ko: Transformer 액션 디코더는 핵심 방정식으로 스케일드 닷프로덕트 셀프 어텐션을 포함한다.
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
