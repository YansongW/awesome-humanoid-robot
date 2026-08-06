---
$id: rel_ent_paper_chasing_autonomy_dynamic_retargeting_con_2026_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_chasing_autonomy_dynamic_retargeting_con_2026
  name:
    en: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running'
    zh: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running'
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running uses Pinocchio.'
  zh: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running使用Pinocchio。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Chasing Autonomy 使用 Pinocchio 进行动力学计算和优化求解。
    | 证据: - 优化目标：最小化加权跟踪误差 Φ = Σ‖x_k − x_k^d‖²_W，使用Casadi+Pinocchio+IPOPT求解'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_chasing_autonomy_dynamic_retargeting_con_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_chasing_autonomy_dynamic_retargeting_con_2026/
  accessed_at: '2026-08-06'
---
