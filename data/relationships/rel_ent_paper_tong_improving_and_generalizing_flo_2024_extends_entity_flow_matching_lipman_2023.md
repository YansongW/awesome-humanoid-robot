---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_extends_entity_flow_matching_lipman_2023
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
  id: entity_flow_matching_lipman_2023
  name:
    en: Flow Matching for Generative Modeling
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: CFM generalizes flow matching to arbitrary source-target couplings, recovering
    FM as a special case.
  zh: CFM将流匹配推广到任意源-目标耦合，并将FM作为特例恢复。
  ko: CFM은 플로우 매칭을 임의의 소스-타겟 결합으로 일반화하며 FM을 특수한 경우로 포함한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: The first main contribution
    of the present paper is to propose a unifying conditional flow matching (CFM)
    framework for FM models with arbitrary transport maps, generalizing existing FM
    and diffusion modeling approaches (Table 1).'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
