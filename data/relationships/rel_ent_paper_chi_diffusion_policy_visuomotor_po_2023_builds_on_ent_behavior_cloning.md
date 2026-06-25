---
$id: rel_ent_paper_chi_diffusion_policy_visuomotor_po_2023_builds_on_ent_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_paper_chi_diffusion_policy_visuomotor_po_2023
  name:
    en: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
    zh: 扩散策略：通过动作扩散实现视觉运动策略学习
    ko: '디퓨전 정책: 행동 확산을 통한 시각운동 정책 학습'
target:
  id: ent_behavior_cloning
  name:
    en: Behavior cloning
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Diffusion Policy is an imitation-learning method that builds on behavior cloning
    while addressing multimodality and high-dimensional action distributions.
  zh: 扩散策略是一种模仿学习方法，在行为克隆的基础上解决了多模态和高维动作分布问题。
  ko: 디퓨전 정책은 다중 모드 및 고차원 행동 분포를 다루는 행동 복제를 기반으로 한 모방 학습 방법이다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Limitations: ''Inherits behavior
    cloning limitations, including suboptimal performance with insufficient or low-quality
    demonstrations.'''
sources:
- id: src_001
  type: paper
  title: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  url: https://arxiv.org/abs/2303.04137
  date: '2023'
  accessed_at: '2026-06-25'
---
