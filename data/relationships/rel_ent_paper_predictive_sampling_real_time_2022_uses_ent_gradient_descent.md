---
$id: rel_ent_paper_predictive_sampling_real_time_2022_uses_ent_gradient_descent
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_predictive_sampling_real_time_2022
  name:
    en: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
    zh: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
target:
  id: ent_gradient_descent
  name:
    en: Gradient Descent
    zh: 梯度下降法
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo uses Gradient Descent.'
  zh: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo使用梯度下降法。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: MJPC支持基于梯度的规划器，包括Gradient Descent，因此Predictive
    Sampling论文使用了Gradient Descent算法。 | 证据: MJPC allows the user to easily author and solve complex robotics tasks, and currently
    supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method
    we call Predictive Sampling.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_predictive_sampling_real_time_2022
  url: https://kg.rounds-tech.com/entry/ent_paper_predictive_sampling_real_time_2022/
  accessed_at: '2026-07-16'
---
