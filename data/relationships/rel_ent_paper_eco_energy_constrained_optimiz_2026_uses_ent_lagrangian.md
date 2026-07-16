---
$id: rel_ent_paper_eco_energy_constrained_optimiz_2026_uses_ent_lagrangian
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_eco_energy_constrained_optimiz_2026
  name:
    en: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking'
    zh: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking'
target:
  id: ent_lagrangian
  name:
    en: Lagrangian
    zh: 拉格朗日量
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking uses Lagrangian.'
  zh: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking使用拉格朗日量。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: ECO使用拉格朗日方法来强制执行能量消耗和参考运动约束。 | 证据: ECO introduces
    dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable,
    symmetric, and energy-efficient walking for humanoid robots.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_eco_energy_constrained_optimiz_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_eco_energy_constrained_optimiz_2026/
  accessed_at: '2026-07-16'
---
