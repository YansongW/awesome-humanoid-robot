---
$id: ent_paper_wang_a_soft_continuum_robot_with_se_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Soft Continuum Robot with Self-Controllable Variable Curvature
  zh: 具有自可控变曲率的软连续体机器人
  ko: 자기 제어 가능한 가변 곡률을 가진 소프트 연속체 로봇
summary:
  en: This paper presents SCoReS, a pneumatic soft continuum robot that embeds a motor-controlled, granular-jamming growing
    spine to achieve continuous, segment-level curvature and stiffness variation without external forces or discrete locking
    mechanisms.
  zh: This paper introduces a new type of soft continuum robot, called SCoReS, which is capable of self-controlling continuously
    its curvature at the segment level; in contrast to previous designs which either require external forces or machine elements,
    or whose variable curvature capabilities are discrete -- depending on the number of locking mechanisms and segments. The
    ability to have a variable curvature, whose control is continuous and independent from external factors, makes a soft
    continuum robot more adaptive in constrained environments, similar to what is observed in nature in the elephant
  ko: 본 논문은 외력이나 이산식 잠금 장치 없이 세그먼트 단위에서 연속적인 곡률과 강성 변화를 실현하는 모터 제어 입자 잠금 성장 척추를 내장한 공압식 소프트 연속체 로봇 SCoReS를 제안한다.
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- system
tags:
- soft_continuum_robot
- variable_curvature
- continuous_stiffness_regulation
- granular_jamming
- growing_spine
- stiffness_control
- compliant_actuation
- fruit_grasping
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.01739v2.
sources:
- id: src_001
  type: paper
  title: A Soft Continuum Robot with Self-Controllable Variable Curvature
  url: https://arxiv.org/abs/2401.01739
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
This paper introduces a new type of soft continuum robot, called SCoReS, which is capable of self-controlling continuously its curvature at the segment level; in contrast to previous designs which either require external forces or machine elements, or whose variable curvature capabilities are discrete -- depending on the number of locking mechanisms and segments. The ability to have a variable curvature, whose control is continuous and independent from external factors, makes a soft continuum robot more adaptive in constrained environments, similar to what is observed in nature in the elephant's trunk or ostrich's neck for instance which exhibit multiple curvatures. To this end, our soft continuum robot enables reconfigurable variable curvatures utilizing a variable stiffness growing spine based on micro-particle granular jamming for the first time. We detail the design of the proposed robot, presenting its modeling through beam theory and FEA simulation -- which is validated through experiments. The robot's versatile bending profiles are then explored in experiments and an application to grasp fruits at different configurations is demonstrated.

## 核心内容
This paper introduces a new type of soft continuum robot, called SCoReS, which is capable of self-controlling continuously its curvature at the segment level; in contrast to previous designs which either require external forces or machine elements, or whose variable curvature capabilities are discrete -- depending on the number of locking mechanisms and segments. The ability to have a variable curvature, whose control is continuous and independent from external factors, makes a soft continuum robot more adaptive in constrained environments, similar to what is observed in nature in the elephant's trunk or ostrich's neck for instance which exhibit multiple curvatures. To this end, our soft continuum robot enables reconfigurable variable curvatures utilizing a variable stiffness growing spine based on micro-particle granular jamming for the first time. We detail the design of the proposed robot, presenting its modeling through beam theory and FEA simulation -- which is validated through experiments. The robot's versatile bending profiles are then explored in experiments and an application to grasp fruits at different configurations is demonstrated.

## 参考
- http://arxiv.org/abs/2401.01739v2


