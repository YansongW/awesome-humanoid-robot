---
$id: rel_ent_paper_tong_improving_and_generalizing_flo_2024_uses_dataset_citeseq_multiome_embryoid
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
  id: dataset_citeseq_multiome_embryoid
  name:
    en: CITE-seq, Multiome, and Embryoid body single-cell datasets
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: Used for single-cell trajectory interpolation with leave-one-out validation
    over timepoints.
  zh: 用于单细胞轨迹插值，通过时间点留一法进行验证。
  ko: 시간점에 대한 leave-one-out 검증을 사용한 단세포 궤적 보간에 사용된다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Following Huguet et al. (2022b),
    we repurpose the CITE-seq and Multiome datasets from a recent NeurIPS competition
    for this task (Burkhardt et al., 2022). We also include the Embryoid body data
    from Moon et al. (2019); Tong et al. (2020).'
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
---
