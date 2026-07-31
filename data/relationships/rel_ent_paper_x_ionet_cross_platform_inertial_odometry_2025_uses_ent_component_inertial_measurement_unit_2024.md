---
$id: rel_ent_paper_x_ionet_cross_platform_inertial_odometry_2025_uses_ent_component_inertial_measurement_unit_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_x_ionet_cross_platform_inertial_odometry_2025
  name:
    en: 'X-IONet: Cross-Platform Inertial Odometry Network for Pedestrian and Legged Robot'
    zh: 'X-IONet: Cross-Platform Inertial Odometry Network for Pedestrian and Legged Robot'
target:
  id: ent_component_inertial_measurement_unit_2024
  name:
    en: Inertial Measurement Unit
    zh: 惯性测量单元
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'X-IONet: Cross-Platform Inertial Odometry Network for Pedestrian and Legged Robot uses Inertial Measurement Unit.'
  zh: 'X-IONet: Cross-Platform Inertial Odometry Network for Pedestrian and Legged Robot使用惯性测量单元。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: X-IONet 仅使用单个惯性测量单元（IMU）来运行，因此源使用目标。 | 证据: To
    tackle this challenge, we introduce X-IONet, a cross-platform inertial odometry framework that operates solely using a
    single Inertial Measurement Unit (IMU).'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_x_ionet_cross_platform_inertial_odometry_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_x_ionet_cross_platform_inertial_odometry_2025/
  accessed_at: '2026-07-31'
---
