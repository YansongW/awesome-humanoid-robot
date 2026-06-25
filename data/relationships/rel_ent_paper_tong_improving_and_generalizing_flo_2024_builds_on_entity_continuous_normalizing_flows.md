---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_builds_on_entity_continuous_normalizing_flows
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_paper_tong_improving_and_generalizing_flo_2024
  name:
    en: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
      Transport
    zh: 基于小批量最优传输的流式生成模型改进与泛化
    ko: 미니배치 최적 수송을 활용한 플로우 기반 생성 모델의 개선 및 일반화
target:
  id: entity_continuous_normalizing_flows
  name:
    en: Continuous Normalizing Flows
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: CFM provides a simulation-free regression objective that avoids the costly maximum-likelihood
    training of CNFs.
  zh: CFM提供了免模拟的回归目标，避免了CNF昂贵的最大似然训练。
  ko: CFM은 시뮬레이션 없는 회귀 목적함수를 제공하여 CNF의 비용이 큰 최대 우도 학습을 피한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: We introduce the generalized
    conditional flow matching (CFM) technique, a family of simulation-free training
    objectives for CNFs.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
