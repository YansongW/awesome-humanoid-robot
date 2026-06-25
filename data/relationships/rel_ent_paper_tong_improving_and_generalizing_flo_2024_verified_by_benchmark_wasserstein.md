---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_verified_by_benchmark_wasserstein
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
  id: benchmark_wasserstein
  name:
    en: Wasserstein Distance
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: 2-Wasserstein distance is used for low-density OT evaluation; earth mover's
    distance (1-Wasserstein) is used for single-cell interpolation error.
  zh: 2-Wasserstein距离用于低密度最优传输评估；推土机距离（1-Wasserstein）用于单细胞插值误差。
  ko: 2-Wasserstein 거리는 저밀도 OT 평가에 사용되며, earth mover's distance(1-Wasserstein)는 단세포
    보간 오차에 사용된다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Table 2 summarizes our results
    showing that OT-CFM flows generalize better to the test set and are very close
    to the dynamic OT paths as measured by normalized path energy. Table 4 shows the
    average earth mover''s distance (1-Wasserstein) on left-out timepoints for three
    datasets.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
