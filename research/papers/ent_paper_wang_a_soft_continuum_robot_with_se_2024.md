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

## Overview
This paper introduces a new type of soft continuum robot, called SCoReS, which is capable of self-controlling continuously its curvature at the segment level; in contrast to previous designs which either require external forces or machine elements, or whose variable curvature capabilities are discrete -- depending on the number of locking mechanisms and segments. The ability to have a variable curvature, whose control is continuous and independent from external factors, makes a soft continuum robot more adaptive in constrained environments, similar to what is observed in nature in the elephant's trunk or ostrich's neck for instance which exhibit multiple curvatures. To this end, our soft continuum robot enables reconfigurable variable curvatures utilizing a variable stiffness growing spine based on micro-particle granular jamming for the first time. We detail the design of the proposed robot, presenting its modeling through beam theory and FEA simulation -- which is validated through experiments. The robot's versatile bending profiles are then explored in experiments and an application to grasp fruits at different configurations is demonstrated.

## Content
This paper introduces a new type of soft continuum robot, called SCoReS, which is capable of self-controlling continuously its curvature at the segment level; in contrast to previous designs which either require external forces or machine elements, or whose variable curvature capabilities are discrete -- depending on the number of locking mechanisms and segments. The ability to have a variable curvature, whose control is continuous and independent from external factors, makes a soft continuum robot more adaptive in constrained environments, similar to what is observed in nature in the elephant's trunk or ostrich's neck for instance which exhibit multiple curvatures. To this end, our soft continuum robot enables reconfigurable variable curvatures utilizing a variable stiffness growing spine based on micro-particle granular jamming for the first time. We detail the design of the proposed robot, presenting its modeling through beam theory and FEA simulation -- which is validated through experiments. The robot's versatile bending profiles are then explored in experiments and an application to grasp fruits at different configurations is demonstrated.

## 개요
본 논문은 SCoReS라고 불리는 새로운 유형의 소프트 연속체 로봇을 소개합니다. 이 로봇은 세그먼트 수준에서 곡률을 지속적으로 자체 제어할 수 있습니다. 이는 외부 힘 또는 기계 요소를 필요로 하거나, 잠금 메커니즘과 세그먼트 수에 따라 가변 곡률 기능이 이산적인 기존 설계와 대조됩니다. 제어가 연속적이고 외부 요인과 독립적인 가변 곡률을 갖는 능력은 소프트 연속체 로봇이 제한된 환경에서 더 적응적으로 만들어 줍니다. 이는 예를 들어 여러 곡률을 나타내는 코끼리 코나 타조 목과 같은 자연에서 관찰되는 것과 유사합니다. 이를 위해, 우리의 소프트 연속체 로봇은 처음으로 미세 입자 과립 잠금(micro-particle granular jamming)에 기반한 가변 강도 성장 척추를 활용하여 재구성 가능한 가변 곡률을 가능하게 합니다. 우리는 제안된 로봇의 설계를 상세히 설명하고, 보 이론(beam theory)과 FEA 시뮬레이션을 통한 모델링을 제시하며, 이는 실험을 통해 검증됩니다. 그런 다음 로봇의 다양한 굽힘 프로파일을 실험에서 탐구하고, 다양한 구성에서 과일을 잡는 응용을 시연합니다.

## 핵심 내용
본 논문은 SCoReS라고 불리는 새로운 유형의 소프트 연속체 로봇을 소개합니다. 이 로봇은 세그먼트 수준에서 곡률을 지속적으로 자체 제어할 수 있습니다. 이는 외부 힘 또는 기계 요소를 필요로 하거나, 잠금 메커니즘과 세그먼트 수에 따라 가변 곡률 기능이 이산적인 기존 설계와 대조됩니다. 제어가 연속적이고 외부 요인과 독립적인 가변 곡률을 갖는 능력은 소프트 연속체 로봇이 제한된 환경에서 더 적응적으로 만들어 줍니다. 이는 예를 들어 여러 곡률을 나타내는 코끼리 코나 타조 목과 같은 자연에서 관찰되는 것과 유사합니다. 이를 위해, 우리의 소프트 연속체 로봇은 처음으로 미세 입자 과립 잠금(micro-particle granular jamming)에 기반한 가변 강도 성장 척추를 활용하여 재구성 가능한 가변 곡률을 가능하게 합니다. 우리는 제안된 로봇의 설계를 상세히 설명하고, 보 이론(beam theory)과 FEA 시뮬레이션을 통한 모델링을 제시하며, 이는 실험을 통해 검증됩니다. 그런 다음 로봇의 다양한 굽힘 프로파일을 실험에서 탐구하고, 다양한 구성에서 과일을 잡는 응용을 시연합니다.
