---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_extends_entity_schrodinger_bridge
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: extends
source:
  id: ent_paper_tong_improving_and_generalizing_flo_2024
  name:
    en: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
      Transport
    zh: 基于小批量最优传输的流式生成模型改进与泛化
    ko: 미니배치 최적 수송을 활용한 플로우 기반 생성 모델의 개선 및 일반화
target:
  id: entity_schrodinger_bridge
  name:
    en: Schrödinger Bridge
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: SB-CFM, an entropic variant of OT-CFM, approximates Schrödinger bridge probability
    flows without simulation.
  zh: OT-CFM的熵变体SB-CFM无需模拟即可近似薛定谔桥概率流。
  ko: OT-CFM의 엔트로피 변형인 SB-CFM은 시뮬레이션 없이 슈뢰딩거 브리지 확률 흐름을 근사한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Furthermore, an entropic variant
    of OT-CFM can be used to efficiently train a CNF to match the probability flow
    of a Schrödinger bridge.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
