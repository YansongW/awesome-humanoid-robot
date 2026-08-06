---
$id: rel_ent_paper_wolf_vla_whole_body_humanoid_optimal_2026_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_wolf_vla_whole_body_humanoid_optimal_2026
  name:
    en: 'WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning'
    zh: 'WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning'
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: 'WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning uses Pinocchio.'
  zh: 'WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning使用Pinocchio。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明求解器采用基于Pinocchio的Crocoddyl框架，说明源论文使用了Pinocchio。
    | 证据: - 求解器采用基于 Pinocchio 的 Crocoddyl 框架，使用多重打靶公式化的 Box-FDDP 变体，显式强制关节力矩限制。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_wolf_vla_whole_body_humanoid_optimal_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_wolf_vla_whole_body_humanoid_optimal_2026/
  accessed_at: '2026-08-06'
---
