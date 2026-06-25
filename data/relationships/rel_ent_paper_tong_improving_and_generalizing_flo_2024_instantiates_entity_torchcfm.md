---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_instantiates_entity_torchcfm
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: instantiates
source:
  id: ent_paper_tong_improving_and_generalizing_flo_2024
  name:
    en: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
      Transport
    zh: 基于小批量最优传输的流式生成模型改进与泛化
    ko: 미니배치 최적 수송을 활용한 플로우 기반 생성 모델의 개선 및 일반화
target:
  id: entity_torchcfm
  name:
    en: torchcfm
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: The authors release torchcfm, a Python package unifying CFM, OT-CFM, and related
    flow-based algorithms.
  zh: 作者发布了torchcfm，一个统一CFM、OT-CFM及相关基于流的算法的Python包。
  ko: 저자들은 CFM, OT-CFM 및 관련 플로우 기반 알고리즘을 통합하는 Python 패키지인 torchcfm을 공개한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: We release a Python package,
    torchcfm, that unifies new and existing algorithms for training flow-based generative
    models under a shared interface and provides implementations of our main experiments.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
