---
$id: ent_paper_jorgensen_thermal_recovery_of_multi_limb_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Thermal Recovery of Multi-Limbed Robots with Electric Actuators
  zh: 具有电动执行器的多肢机器人的热恢复
  ko: 전기 액추에이터를 갖춘 다지체 로봇의 열 회복
summary:
  en: Proposes a data-driven, effort-based thermal model and a contact-constrained thermal inverse-kinematics approach to
    find robot configurations that cool overheated actuators, validated experimentally on the NASA Valkyrie humanoid.
  zh: 提出了一种数据驱动、基于作力的一阶热模型以及接触约束热逆运动学方法，用于寻找使过热执行器降温的机器人构型，并在NASA Valkyrie人形机器人上进行了实验验证。
  ko: 과열된 액추에이터를 냉각시키는 로봇 구형을 찾기 위해 데이터 기반의 노력 기반 1차 열 모델과 접촉 제약 열 역기구학 방법을 제안하고 NASA Valkyrie 휴머노이드에서 실험적으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- thermal_recovery
- actuator_thermal_model
- contact_constrained_thermal_ik
- gradient_descent
- nasa_valkyrie
- series_elastic_actuator
- effort_based_model
- humanoid_thermal_management
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1902.00187v4.
sources:
- id: src_001
  type: paper
  title: Thermal Recovery of Multi-Limbed Robots with Electric Actuators
  url: https://arxiv.org/abs/1902.00187
  date: '2019'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2019.2894068
theoretical_depth:
- method
---
## 概述
The problem of finding thermally minimizing configurations of a humanoid robot to recover its actuators from unsafe thermal states is addressed. A first-order, data-driven, effort-based, thermal model of the robot's actuators is devised, which is used to predict future thermal states. Given this predictive capability, a map between configurations and future temperatures is formulated to find what configurations, subject to valid contact constraints, can be taken now to minimize future thermal states. Effectively, this approach is a realization of a contact-constrained thermal inverse-kinematics (IK) process. Experimental validation of the proposed approach is performed on the NASA Valkyrie robot hardware.

## 核心内容
The problem of finding thermally minimizing configurations of a humanoid robot to recover its actuators from unsafe thermal states is addressed. A first-order, data-driven, effort-based, thermal model of the robot's actuators is devised, which is used to predict future thermal states. Given this predictive capability, a map between configurations and future temperatures is formulated to find what configurations, subject to valid contact constraints, can be taken now to minimize future thermal states. Effectively, this approach is a realization of a contact-constrained thermal inverse-kinematics (IK) process. Experimental validation of the proposed approach is performed on the NASA Valkyrie robot hardware.

## 参考
- http://arxiv.org/abs/1902.00187v4

