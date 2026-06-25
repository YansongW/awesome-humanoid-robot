---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_verified_by_benchmark_fid
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
  id: benchmark_fid
  name:
    en: Fréchet Inception Distance
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: Used to evaluate image quality on CIFAR-10 for different training steps and
    ODE solvers.
  zh: 用于在不同训练步长和ODE求解器下评估CIFAR-10的图像质量。
  ko: 다양한 학습 단계 및 ODE 솔버에서 CIFAR-10의 이미지 품질을 평가하는 데 사용된다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: We train our OT-CFM, as well
    as I-CFM and the original FM, with this new training procedure and report the
    Fréchet inception distance (FID) in Table 5.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
