---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_verified_by_benchmark_mmd
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: verified_by
source:
  id: ent_paper_tong_improving_and_generalizing_flo_2024
  name:
    en: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
      Transport
    zh: 基于小批量最优传输的流式生成模型改进与泛化
    ko: 미니배치 최적 수송을 활용한 플로우 기반 생성 모델의 개선 및 일반화
target:
  id: benchmark_mmd
  name:
    en: Maximum Mean Discrepancy
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: Used to measure divergence between translated and target CelebA latent vectors
    in unsupervised image translation.
  zh: 用于在无监督图像转换中测量转换后和目标CelebA潜在向量之间的差异。
  ko: 비지도 이미지 변환에서 변환된 CelebA 잠재 벡터와 타겟 벡터 간의 발산을 측정하는 데 사용된다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: As a metric of divergence, we
    use maximum mean discrepancy (MMD) with a broad Gaussian kernel (exp(−||x−y||^2/(2·128))).
    The results aggregated over all attributes are shown in Table 6.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
