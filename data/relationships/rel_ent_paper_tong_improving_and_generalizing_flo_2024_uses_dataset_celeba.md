---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_uses_dataset_celeba
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
  id: dataset_celeba
  name:
    en: CelebA
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: Used for unsupervised image-to-image translation between facial attributes in
    latent space.
  zh: 用于在潜在空间中进行面部属性之间的无监督图像到图像转换。
  ko: 잠재 공간에서 얼굴 속성 간의 비지도 이미지-대-이미지 변환에 사용된다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: We show how CFM can be used
    to learn a mapping between two unpaired datasets in high-dimensional space using
    the CelebA dataset (Liu et al., 2015; Sun et al., 2014).'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
