---
$id: rel_ent_paper_prime_physically_consistent_robotic_iner_2026_mentions_ent_paper_kalman_filter_kf
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_prime_physically_consistent_robotic_iner_2026
  name:
    en: 'PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots'
    zh: 'PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots'
target:
  id: ent_paper_kalman_filter_kf
  name:
    en: Kalman Filter (KF)
    zh: 与 Extended Kalman Filter (EKF) 经典论文、教材与权威教程
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots mentions Kalman
    Filter (KF).'
  zh: 'PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots提及与 Extended Kalman
    Filter (EKF) 经典论文、教材与权威教程。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 现有感知管线（EKF 或 mocap）只输出运动学，接触力、接触时间与惯性参数不可观测，导致重建轨迹违反刚体动力学，尤其在接触丰富的运动中。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_prime_physically_consistent_robotic_iner_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_prime_physically_consistent_robotic_iner_2026/
  accessed_at: '2026-08-06'
---
