---
$id: ent_paper_abdolmalaki_geometric_jacobians_derivation_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometric Jacobians Derivation and Kinematic Singularity Analysis for Smokie Robot Manipulator & the Barrett WAM
  zh: Smokie机器人操作臂与Barrett WAM的几何雅可比推导及运动学奇异性分析
  ko: Smokie 로봇 매니퓰레이터 및 Barrett WAM의 기하학적 자코비안 도출과 운동학적 특이점 분석
summary:
  en: Derives the 6×6 geometric Jacobians and kinematic singularities of the 6-DOF Smokie OUR and Barrett WAM manipulators
    from Denavit-Hartenberg parameters and direct kinematics, and surveys redundant kinematic allocation schemes for the 7-DOF
    Barrett WAM.
  zh: 基于D-H参数和正运动学，推导6自由度Smokie OUR与Barrett WAM机械臂的6×6几何雅可比矩阵和运动学奇异性，并综述7自由度Barrett WAM的冗余运动学分配方案。
  ko: D-H 파라미터와 정기구학을 바탕으로 6자유도 Smokie OUR 및 Barrett WAM 매니퓰레이터의 6×6 기하학적 자코비안과 운동학적 특이점을 도출하고, 7자유도 Barrett WAM의 중복 운동학 할당
    방식을 검토한다.
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
- geometric_jacobian
- kinematic_singularity
- manipulator_arm
- barrett_wam
- smokie_our
- denavit_hartenberg_parameters
- redundant_manipulator
- humanoid_arm
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1707.04821v2.
sources:
- id: src_001
  type: paper
  title: Geometric Jacobians Derivation and Kinematic Singularity Analysis for Smokie Robot Manipulator & the Barrett WAM
  url: https://arxiv.org/abs/1707.04821
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
This paper discusses deriving geometric jacobians and identifying and analyzing the kinematic singularities for two 6 DOF arm robots. First we show the direct kinematics and D-H parameters derived for these two arms. The Geometric jacobian is computed for Barrett WAM and Smokie OUR. By analyzing the jacobian matrices we find the configurations at which J is rank deficient and derive the kinematic singularities through jacobian's determinent. Schematic are provided to show the singular configurations of both robots. Finally a survey is done on redundant kinematic allocation schemesfor 7 DoF Barrett WAM.

## 核心内容
This paper discusses deriving geometric jacobians and identifying and analyzing the kinematic singularities for two 6 DOF arm robots. First we show the direct kinematics and D-H parameters derived for these two arms. The Geometric jacobian is computed for Barrett WAM and Smokie OUR. By analyzing the jacobian matrices we find the configurations at which J is rank deficient and derive the kinematic singularities through jacobian's determinent. Schematic are provided to show the singular configurations of both robots. Finally a survey is done on redundant kinematic allocation schemesfor 7 DoF Barrett WAM.

## 参考
- http://arxiv.org/abs/1707.04821v2

## Overview
This paper discusses deriving geometric Jacobians and identifying and analyzing the kinematic singularities for two 6 DOF arm robots. First, we show the direct kinematics and D-H parameters derived for these two arms. The geometric Jacobian is computed for Barrett WAM and Smokie OUR. By analyzing the Jacobian matrices, we find the configurations at which J is rank deficient and derive the kinematic singularities through the Jacobian's determinant. Schematics are provided to show the singular configurations of both robots. Finally, a survey is done on redundant kinematic allocation schemes for the 7 DoF Barrett WAM.

## Content
This paper discusses deriving geometric Jacobians and identifying and analyzing the kinematic singularities for two 6 DOF arm robots. First, we show the direct kinematics and D-H parameters derived for these two arms. The geometric Jacobian is computed for Barrett WAM and Smokie OUR. By analyzing the Jacobian matrices, we find the configurations at which J is rank deficient and derive the kinematic singularities through the Jacobian's determinant. Schematics are provided to show the singular configurations of both robots. Finally, a survey is done on redundant kinematic allocation schemes for the 7 DoF Barrett WAM.

## 개요
본 논문은 두 개의 6자유도(6 DOF) 로봇 팔에 대한 기하학적 자코비안(Geometric Jacobian) 유도와 운동학적 특이점(Kinematic Singularities) 식별 및 분석을 다룹니다. 먼저 이 두 팔에 대해 유도된 직접 운동학(Direct Kinematics)과 D-H 파라미터를 제시합니다. Barrett WAM과 Smokie OUR에 대한 기하학적 자코비안을 계산합니다. 자코비안 행렬을 분석하여 J의 계수(rank)가 부족한 형상을 찾고, 자코비안 행렬식을 통해 운동학적 특이점을 유도합니다. 두 로봇의 특이 형상을 보여주는 개략도가 제공됩니다. 마지막으로 7자유도(7 DoF) Barrett WAM을 위한 중복 운동학 할당 기법(Redundant Kinematic Allocation Schemes)에 대한 조사가 수행됩니다.

## 핵심 내용
본 논문은 두 개의 6자유도(6 DOF) 로봇 팔에 대한 기하학적 자코비안(Geometric Jacobian) 유도와 운동학적 특이점(Kinematic Singularities) 식별 및 분석을 다룹니다. 먼저 이 두 팔에 대해 유도된 직접 운동학(Direct Kinematics)과 D-H 파라미터를 제시합니다. Barrett WAM과 Smokie OUR에 대한 기하학적 자코비안을 계산합니다. 자코비안 행렬을 분석하여 J의 계수(rank)가 부족한 형상을 찾고, 자코비안 행렬식을 통해 운동학적 특이점을 유도합니다. 두 로봇의 특이 형상을 보여주는 개략도가 제공됩니다. 마지막으로 7자유도(7 DoF) Barrett WAM을 위한 중복 운동학 할당 기법(Redundant Kinematic Allocation Schemes)에 대한 조사가 수행됩니다.
