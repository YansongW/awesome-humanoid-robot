---
$id: rel_ent_paper_avatarposer_articulated_full_b_2022_1_uses_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_avatarposer_articulated_full_b_2022_1
  name:
    en: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
    zh: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing uses Inverse Kinematics.'
  zh: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing使用逆运动学。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明源论文采用逆运动学优化手臂关节位置，因此使用该方法。 | 证据: - **优化环节**：采用逆运动学（Inverse
    Kinematics）优化手臂关节位置，使输出姿态与原始追踪输入严格对齐，从而生成类似动作捕捉动画的精确全身运动。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_avatarposer_articulated_full_b_2022_1
  url: https://kg.rounds-tech.com/entry/ent_paper_avatarposer_articulated_full_b_2022_1/
  accessed_at: '2026-07-31'
---
