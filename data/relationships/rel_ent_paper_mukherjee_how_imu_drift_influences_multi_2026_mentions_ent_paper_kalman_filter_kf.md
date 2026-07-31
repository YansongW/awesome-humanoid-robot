---
$id: rel_ent_paper_mukherjee_how_imu_drift_influences_multi_2026_mentions_ent_paper_kalman_filter_kf
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_mukherjee_how_imu_drift_influences_multi_2026
  name:
    en: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in Subterranean Terrains
    zh: IMU漂移如何影响地下地形地面机器人的多雷达惯性里程计
target:
  id: ent_paper_kalman_filter_kf
  name:
    en: Kalman Filter (KF)
    zh: 与 Extended Kalman Filter (EKF) 经典论文、教材与权威教程
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in Subterranean Terrains mentions Kalman Filter
    (KF).
  zh: IMU漂移如何影响地下地形地面机器人的多雷达惯性里程计提及与 Extended Kalman Filter (EKF) 经典论文、教材与权威教程。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: This paper proposes a two-stage Multi-Radar Inertial
    Odometry (MRIO) framework that estimates radar ego-velocity via least squares, uses an EKF for online IMU bias correction,
    and fuses corrected IMU accelerations with measurements from multiple TI IWR6843AOP EVM FMCW radars to achieve robust
    locali'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_mukherjee_how_imu_drift_influences_multi_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_mukherjee_how_imu_drift_influences_multi_2026/
  accessed_at: '2026-07-31'
---
