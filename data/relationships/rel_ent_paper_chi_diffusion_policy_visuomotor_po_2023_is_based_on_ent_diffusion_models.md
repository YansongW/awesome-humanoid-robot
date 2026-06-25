---
$id: rel_ent_paper_chi_diffusion_policy_visuomotor_po_2023_is_based_on_ent_diffusion_models
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_paper_chi_diffusion_policy_visuomotor_po_2023
  name:
    en: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
    zh: 扩散策略：通过动作扩散实现视觉运动策略学习
    ko: '디퓨전 정책: 행동 확산을 통한 시각운동 정책 학습'
target:
  id: ent_diffusion_models
  name:
    en: Denoising diffusion models
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Diffusion Policy builds on denoising diffusion models by representing a visuomotor
    policy as a conditional denoising diffusion process.
  zh: 扩散策略基于去噪扩散模型，将视觉运动策略表示为条件去噪扩散过程。
  ko: 디퓨전 정책은 시각운동 정책을 조건부 노이즈 제거 확산 과정으로 모델링하여 노이즈 제거 확산 모델을 기반으로 한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Abstract: ''This paper introduces
    Diffusion Policy, a new way of generating robot behavior by representing a robot''s
    visuomotor policy as a conditional denoising diffusion process.'''
sources:
- id: src_001
  type: paper
  title: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  url: https://arxiv.org/abs/2303.04137
  date: '2023'
  accessed_at: '2026-06-25'
---
