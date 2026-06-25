---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_is_alternative_to_entity_diffusion_models
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_alternative_to
source:
  id: ent_paper_tong_improving_and_generalizing_flo_2024
  name:
    en: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
      Transport
    zh: 基于小批量最优传输的流式生成模型改进与泛化
    ko: 미니배치 최적 수송을 활용한 플로우 기반 생성 모델의 개선 및 일반화
target:
  id: entity_diffusion_models
  name:
    en: Diffusion Models
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: CFM uses a stable regression objective like diffusion models but retains the
    efficient deterministic inference of flow models and does not require a Gaussian
    source.
  zh: CFM像扩散模型一样使用稳定的回归目标，但保留了流模型高效的确定性推理，且不需要高斯源分布。
  ko: CFM은 확산 모델처럼 안정적인 회귀 목적함수를 사용하지만, 플로우 모델의 효율적인 확정론적 추론을 유지하고 가우시안 소스 분포를 필요로
    하지 않는다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: CFM features a stable regression
    objective like that used to train the stochastic flow in diffusion models but
    enjoys the efficient inference of deterministic flow models. In contrast to both
    diffusion models and prior CNF training algorithms, CFM does not require the source
    distribution to be Gaussian or require evaluation of its density.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
