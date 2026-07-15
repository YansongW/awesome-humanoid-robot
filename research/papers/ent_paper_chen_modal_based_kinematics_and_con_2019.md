---
$id: ent_paper_chen_modal_based_kinematics_and_con_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Modal-based Kinematics and Contact Detection of Soft Robots
  zh: 基于模态的软体机器人运动学与接触检测
  ko: 모달 기반 소프트 로봇 운동학 및 접촉 감지
summary:
  en: Proposes modal-based forward and instantaneous kinematics for a 1-DoF pneumatic bellow soft actuator and uses fixed
    centrode deviation with nonlinear least-squares optimization to detect external contacts and estimate their location along
    the backbone.
  zh: Soft robots offer an alternative approach to manipulate inside the constrained space while maintaining the safe interaction
    with the external environment. Due to its adaptable compliance characteristic, external contact force can easily deform
    the robot shapes and lead to undesired robot kinematic and dynamic properties. Accurate contact detection and contact
    position estimation are of critical importance for soft robot modeling, control, trajectory planning, and eventually affect
    the success of task completion. In this paper, we focus on the study of 1-DoF soft pneumatic bellow bending actuat
  ko: 1자유도 공기압 벨로우 연성 액츄에이터의 모달 기반 정운동학 및 순간운동학을 제안하고, 고정 중심선 편차법과 비선형 최소자승 최적화를 사용하여 외부 접촉을 감지하고 백본 상의 접촉 위치를 추정한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- soft_robotics
- pneumatic_bellow_actuator
- contact_detection
- modal_kinematics
- fixed_centrode_deviation
- nonlinear_least_squares
- compliant_actuator
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1906.11654v1.
sources:
- id: src_001
  type: paper
  title: Modal-based Kinematics and Contact Detection of Soft Robots
  url: https://arxiv.org/abs/1906.11654
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
Soft robots offer an alternative approach to manipulate inside the constrained space while maintaining the safe interaction with the external environment. Due to its adaptable compliance characteristic, external contact force can easily deform the robot shapes and lead to undesired robot kinematic and dynamic properties. Accurate contact detection and contact position estimation are of critical importance for soft robot modeling, control, trajectory planning, and eventually affect the success of task completion. In this paper, we focus on the study of 1-DoF soft pneumatic bellow bending actuator, which is one of the fundamental components to construct complex, multi-DoF soft robots. This 1-DoF soft robot is modeled through the integral representation of the spacial curve. The direct and instantaneous kinematics are calculated explicitly through a modal method. The fixed centrode deviation (FCD) method is used to to detect the external contact and estimate contact location. Simulation results indicate that the contact location can be accurately estimated by solving a nonlinear least square optimization problem.

## 核心内容
Soft robots offer an alternative approach to manipulate inside the constrained space while maintaining the safe interaction with the external environment. Due to its adaptable compliance characteristic, external contact force can easily deform the robot shapes and lead to undesired robot kinematic and dynamic properties. Accurate contact detection and contact position estimation are of critical importance for soft robot modeling, control, trajectory planning, and eventually affect the success of task completion. In this paper, we focus on the study of 1-DoF soft pneumatic bellow bending actuator, which is one of the fundamental components to construct complex, multi-DoF soft robots. This 1-DoF soft robot is modeled through the integral representation of the spacial curve. The direct and instantaneous kinematics are calculated explicitly through a modal method. The fixed centrode deviation (FCD) method is used to to detect the external contact and estimate contact location. Simulation results indicate that the contact location can be accurately estimated by solving a nonlinear least square optimization problem.

## 参考
- http://arxiv.org/abs/1906.11654v1


