---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_uses_entity_optimal_transport
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_tong_improving_and_generalizing_flo_2024
  name:
    en: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
      Transport
    zh: 基于小批量最优传输的流式生成模型改进与泛化
    ko: 미니배치 최적 수송을 활용한 플로우 기반 생성 모델의 개선 및 일반화
target:
  id: entity_optimal_transport
  name:
    en: Optimal Transport
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: OT-CFM uses minibatch optimal transport couplings to approximate dynamic optimal
    transport and produce straighter flows.
  zh: OT-CFM使用小批量最优传输耦合来近似动态最优传输并生成更直的流。
  ko: OT-CFM은 미니배치 최적 수송 결합을 사용하여 동적 최적 수송을 근사하고 더 직선적인 플로우를 생성한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: We consider a special case of
    CFM that draws source and target samples according to an optimal transport plan,
    allowing us to solve the dynamic OT and Schrödinger bridge problems in a simulation-free
    way, using only static OT maps between marginal distributions.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
