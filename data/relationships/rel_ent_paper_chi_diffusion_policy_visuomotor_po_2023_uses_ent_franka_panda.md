---
$id: rel_ent_paper_chi_diffusion_policy_visuomotor_po_2023_uses_ent_franka_panda
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_chi_diffusion_policy_visuomotor_po_2023
  name:
    en: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
    zh: 扩散策略：通过动作扩散实现视觉运动策略学习
    ko: '디퓨전 정책: 행동 확산을 통한 시각운동 정책 학습'
target:
  id: ent_franka_panda
  name:
    en: Franka Panda robot arms
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: Diffusion Policy uses Franka Panda robot arms in real-world experiments, including
    bimanual tasks.
  zh: 扩散策略在真实世界实验中使用了Franka Panda机械臂，包括双手任务。
  ko: 디퓨전 정책은 양손 작업을 포함한 실제 실험에서 Franka Panda 로봇 팔을 사용하였다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Metadata: components_or_materials
    include ''Franka Panda robot arms''.'
sources:
- id: src_001
  type: paper
  title: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  url: https://arxiv.org/abs/2303.04137
  date: '2023'
  accessed_at: '2026-06-25'
---
