---
$id: rel_ent_paper_deniz_identification_of_a_physics_ba_2026_integrates_ent_component_harmonic_drive_reducer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: integrates
source:
  id: ent_paper_deniz_identification_of_a_physics_ba_2026
  name:
    en: Identification of a Physics-Based Electrical Power Consumption Model for the
      Unitree G1 Humanoid Arm
    zh: Unitree G1人形机器人手臂基于物理的电力消耗模型辨识
    ko: Unitree G1 휴머노이드 팔의 물리 기반 전력 소비 모델 식별
target:
  id: ent_component_harmonic_drive_reducer
  name:
    en: Harmonic-drive reducers
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: Harmonic-drive reducers are used in the arm joints and exhibit asymmetric acceleration/braking
    behaviour.
  zh: 谐波减速器用于手臂关节，并表现出加速/制动非对称行为。
  ko: 하모닉 드라이브 감속기는 팔 관절에 사용되며 가속/제동 비대칭 거동을 보입니다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Limitations: Single efficiency
    parameter is used for both acceleration and braking despite asymmetric harmonic-drive
    behaviour.'
sources:
- id: src_001
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for
    the Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
---



