---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_uses_dataset_cifar10
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
  id: dataset_cifar10
  name:
    en: CIFAR-10
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: Used for unconditional image generation experiments to evaluate training speed
    and inference cost.
  zh: 用于无条件图像生成实验，以评估训练速度和推理成本。
  ko: 학습 속도 및 추론 비용을 평가하기 위한 무조건 이미지 생성 실험에 사용된다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: We perform an experiment on
    unconditional CIFAR-10 generation from a Gaussian source to examine how OT-CFM
    performs in the high-dimensional image setting.'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
