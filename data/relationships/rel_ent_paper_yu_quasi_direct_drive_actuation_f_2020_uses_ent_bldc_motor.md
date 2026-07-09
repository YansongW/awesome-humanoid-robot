---
$id: rel_ent_paper_yu_quasi_direct_drive_actuation_f_2020_uses_ent_bldc_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_yu_quasi_direct_drive_actuation_f_2020
  name:
    en: Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton with High Backdrivability and High Bandwidth
    zh: 用于高反驱性和高带宽轻量化髋关节外骨骼的准直驱驱动
    ko: 높은 역구동성 및 높은 대역폭을 가진 경량 고관절 외골격용 준직구동 구동
target:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    ko: ''
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: A high-torque-density exterior-rotor BLDC motor is the core motor of the actuator.
  zh: 高扭矩密度外转子无刷直流电机是执行器的核心电机。
  ko: 높은 토크 밀도의 외부 회전자 BLDC 모터가 구동기의 핵심 모터이다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: The lightweight exterior rotor reduces rotary inertia and increases
    the torque-inertia ratio. Moreover, the customized motor uses sintered Neodymium Iron Boron (NdFeB) permanent magnets,
    which can reach 1.9 Tesla magnetic field intensity, as shown in Fig. 2 (b).'
sources:
- id: src_001
  type: paper
  title: Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton with High Backdrivability and High Bandwidth
  url: https://arxiv.org/abs/2004.00467
  date: '2020'
  accessed_at: '2026-06-26'
---
