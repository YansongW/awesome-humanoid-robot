---
$id: rel_ent_component_battery_management_system_mentions_ent_paper_kalman_filter_kf
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_component_battery_management_system
  name:
    en: Battery Management System
    zh: 电池管理系统
target:
  id: ent_paper_kalman_filter_kf
  name:
    en: Kalman Filter (KF)
    zh: 与 Extended Kalman Filter (EKF) 经典论文、教材与权威教程
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Battery Management System mentions Kalman Filter (KF).
  zh: 电池管理系统提及与 Extended Kalman Filter (EKF) 经典论文、教材与权威教程。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: **扩展卡尔曼滤波（EKF）SOC 估计**。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_battery_management_system
  url: https://kg.rounds-tech.com/entry/ent_component_battery_management_system/
  accessed_at: '2026-07-31'
---
