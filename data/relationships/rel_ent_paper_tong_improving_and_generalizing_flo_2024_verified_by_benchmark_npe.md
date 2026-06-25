---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_verified_by_benchmark_npe
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
  id: benchmark_npe
  name:
    en: Normalized Path Energy
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: Used to measure how well learned flows approximate dynamic optimal transport
    paths on 2D datasets.
  zh: 用于衡量学习到的流在二维数据集上近似动态最优传输路径的程度。
  ko: 2D 데이터셋에서 학습된 플로우가 동적 최적 수송 경로를 얼마나 잘 근사하는지 측정하는 데 사용된다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: To measure how well a model
    solves the OT problem we use normalized path energy (NPE), defined via the 2-Wasserstein
    distance as NPE(vθ) = |PE(vθ) − W_2^2(q0, q1)| / W_2^2(q0, q1).'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
