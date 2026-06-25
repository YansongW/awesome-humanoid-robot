---
$id: rel_ent_paper_chi_diffusion_policy_visuomotor_po_2023_evaluates_on_ent_franka_kitchen
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_chi_diffusion_policy_visuomotor_po_2023
  name:
    en: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
    zh: 扩散策略：通过动作扩散实现视觉运动策略学习
    ko: '디퓨전 정책: 행동 확산을 통한 시각운동 정책 학습'
target:
  id: ent_franka_kitchen
  name:
    en: Franka Kitchen
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: Diffusion Policy is evaluated on the Franka Kitchen demonstration dataset.
  zh: 扩散策略在Franka Kitchen示教数据集上进行了评估。
  ko: 디퓨전 정책은 Franka Kitchen 시연 데이터 세트에서 평가되었다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Metadata: benchmarks_used include
    ''Franka Kitchen''.'
sources:
- id: src_001
  type: paper
  title: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  url: https://arxiv.org/abs/2303.04137
  date: '2023'
  accessed_at: '2026-06-25'
---
