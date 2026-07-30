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
  zh: 本文基于Denavit-Hartenberg参数与正运动学，推导了6自由度Smokie OUR与Barrett WAM机械臂的6×6几何雅可比矩阵及其运动学奇异点，并综述了7自由度Barrett WAM的冗余运动学分配方案。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1707.04821v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
论文首先为Smokie OUR与Barrett WAM两种6自由度机械臂建立了正运动学模型与D-H参数，随后计算了各自的几何雅可比矩阵。通过分析雅可比矩阵的秩亏缺条件并求解行列式，确定了两种机械臂的运动学奇异位形，并提供了示意图加以说明。最后，针对7自由度Barrett WAM的冗余运动学分配方案进行了综述。

## 核心内容
### 方法
- 从D-H参数出发，建立两种6自由度机械臂的正运动学模型。
- 基于正运动学推导6×6几何雅可比矩阵，该矩阵将关节速度映射到末端执行器空间速度。

### 运动学奇异点分析
- 通过计算雅可比矩阵的行列式，找出使矩阵秩亏缺的关节配置。
- 对于Smokie OUR与Barrett WAM，分别给出了奇异位形的示意图，直观展示机械臂在奇异点处的姿态。

### 冗余运动学分配（7自由度Barrett WAM）
- 综述了7自由度Barrett WAM的冗余运动学分配方案，包括利用冗余自由度避免奇异点、优化关节运动范围等策略。

### 关键结论
- 两种6自由度机械臂的奇异点均通过雅可比行列式为零的条件确定，具体位形由机械臂的几何结构（如连杆长度、关节偏移）决定。
- 冗余自由度分配方案可有效提升7自由度Barrett WAM的灵活性与避奇异能力。

## Overview
This paper discusses deriving geometric jacobians and identifying and analyzing the kinematic singularities for two 6 DOF arm robots. First we show the direct kinematics and D-H parameters derived for these two arms. The Geometric jacobian is computed for Barrett WAM and Smokie OUR. By analyzing the jacobian matrices we find the configurations at which J is rank deficient and derive the kinematic singularities through jacobian's determinent. Schematic are provided to show the singular configurations of both robots. Finally a survey is done on redundant kinematic allocation schemesfor 7 DoF Barrett WAM.

## Overview
This paper discusses deriving geometric Jacobians and identifying and analyzing the kinematic singularities for two 6 DOF arm robots. First, we show the direct kinematics and D-H parameters derived for these two arms. The geometric Jacobian is computed for Barrett WAM and Smokie OUR. By analyzing the Jacobian matrices, we find the configurations at which J is rank deficient and derive the kinematic singularities through the Jacobian's determinant. Schematics are provided to show the singular configurations of both robots. Finally, a survey is done on redundant kinematic allocation schemes for the 7 DoF Barrett WAM.

## Content
This paper discusses deriving geometric Jacobians and identifying and analyzing the kinematic singularities for two 6 DOF arm robots. First, we show the direct kinematics and D-H parameters derived for these two arms. The geometric Jacobian is computed for Barrett WAM and Smokie OUR. By analyzing the Jacobian matrices, we find the configurations at which J is rank deficient and derive the kinematic singularities through the Jacobian's determinant. Schematics are provided to show the singular configurations of both robots. Finally, a survey is done on redundant kinematic allocation schemes for the 7 DoF Barrett WAM.

## 개요
본 논문은 두 개의 6자유도(6 DOF) 로봇 팔에 대한 기하학적 자코비안(Geometric Jacobian) 유도와 운동학적 특이점(Kinematic Singularities) 식별 및 분석을 다룹니다. 먼저 이 두 팔에 대해 유도된 직접 운동학(Direct Kinematics)과 D-H 파라미터를 제시합니다. Barrett WAM과 Smokie OUR에 대한 기하학적 자코비안을 계산합니다. 자코비안 행렬을 분석하여 J의 계수(rank)가 부족한 형상을 찾고, 자코비안 행렬식을 통해 운동학적 특이점을 유도합니다. 두 로봇의 특이 형상을 보여주는 개략도가 제공됩니다. 마지막으로 7자유도(7 DoF) Barrett WAM을 위한 중복 운동학 할당 기법(Redundant Kinematic Allocation Schemes)에 대한 조사가 수행됩니다.

## 핵심 내용
본 논문은 두 개의 6자유도(6 DOF) 로봇 팔에 대한 기하학적 자코비안(Geometric Jacobian) 유도와 운동학적 특이점(Kinematic Singularities) 식별 및 분석을 다룹니다. 먼저 이 두 팔에 대해 유도된 직접 운동학(Direct Kinematics)과 D-H 파라미터를 제시합니다. Barrett WAM과 Smokie OUR에 대한 기하학적 자코비안을 계산합니다. 자코비안 행렬을 분석하여 J의 계수(rank)가 부족한 형상을 찾고, 자코비안 행렬식을 통해 운동학적 특이점을 유도합니다. 두 로봇의 특이 형상을 보여주는 개략도가 제공됩니다. 마지막으로 7자유도(7 DoF) Barrett WAM을 위한 중복 운동학 할당 기법(Redundant Kinematic Allocation Schemes)에 대한 조사가 수행됩니다.

## 参考
- http://arxiv.org/abs/1707.04821v2
