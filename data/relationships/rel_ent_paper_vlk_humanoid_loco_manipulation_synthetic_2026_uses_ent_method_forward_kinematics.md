---
$id: rel_ent_paper_vlk_humanoid_loco_manipulation_synthetic_2026_uses_ent_method_forward_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_vlk_humanoid_loco_manipulation_synthetic_2026
  name:
    en: 'VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes'
    zh: 'VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes'
target:
  id: ent_method_forward_kinematics
  name:
    en: Forward Kinematics
    zh: 正运动学
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: 'VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes uses Forward Kinematics.'
  zh: 'VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes使用正运动学。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在训练损失中使用可微分的正向运动学层。 | 证据: **Differentiable
    Forward Kinematics Layer**: A differentiable FK layer in the training loss imposes geometric constraints on global body
    and end-effector positions, significantly improving the physical plausibility of generated trajectories and wrist'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_vlk_humanoid_loco_manipulation_synthetic_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_vlk_humanoid_loco_manipulation_synthetic_2026/
  accessed_at: '2026-08-06'
---
