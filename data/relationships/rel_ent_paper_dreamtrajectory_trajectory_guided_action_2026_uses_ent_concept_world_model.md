---
$id: rel_ent_paper_dreamtrajectory_trajectory_guided_action_2026_uses_ent_concept_world_model
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_dreamtrajectory_trajectory_guided_action_2026
  name:
    en: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation'
    zh: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation'
target:
  id: ent_concept_world_model
  name:
    en: World Model
    zh: 世界模型
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation uses World
    Model.'
  zh: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation使用世界模型。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用世界模型来预测轨迹。 | 证据: - **World Model Prediction**:
    A lightweight recurrent world model W_φ(o_t, s_t, a_{t:t+H-1}) predicts the trajectory τ̃(a) ∈ ℝ^{H×7} that a candidate
    action chunk would induce.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_dreamtrajectory_trajectory_guided_action_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_dreamtrajectory_trajectory_guided_action_2026/
  accessed_at: '2026-08-06'
---
