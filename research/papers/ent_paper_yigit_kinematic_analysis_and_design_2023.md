---
$id: ent_paper_yigit_kinematic_analysis_and_design_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Kinematic Analysis and Design of a Novel (6+3)-DoF Parallel Robot with Fixed
    Actuators
  zh: 一种具有固定执行器的新型（6+3）自由度并联机器人的运动学分析与设计
  ko: 고정 액츄에이터를 갖춘 신형 (6+3)-DoF 병렬 로봇의 운동학적 분석 및 설계
summary:
  en: Presents a kinematically redundant (6+3)-DoF parallel robot built from three
    identical base-mounted 3-DoF RU/2-RUS legs, deriving inverse kinematics and Jacobian
    matrices via screw theory, classifying singularities, and optimizing leg geometry
    for a 2g acceleration workspace aimed at backdrivable physical human-robot interaction.
  zh: 提出了一种运动学冗余的（6+3）自由度并联机器人，该机器人由三个相同的基座安装式3自由度RU/2-RUS支腿构成，利用螺旋理论推导逆运动学和雅可比矩阵，对奇异性进行分类，并优化支腿几何结构以获得2g加速度工作空间，旨在实现可反向驱动的物理人机交互。
  ko: 세 개의 동일한 기座 설치형 3-DoF RU/2-RUS 다리로 구성된 운동학적 중복 (6+3)-DoF 병렬 로봇을 제안하고, 스크루 이론을
    통해 역운동학 및 야코비 행렬을 도출하며, 특이점을 분류하고, 2g 가속도 작업 공간을 위해 다리 기하학을 최적화하여 역구동 가능한 물리적
    인간-로봇 상호작용을 목표로 합니다.
domains:
- 02_components
- 06_design_engineering
- 03_manufacturing_processes
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- parallel_robot
- fixed_actuator
- kinematic_redundancy
- ru_2rus_leg
- screw_theory
- jacobian
- singularity_analysis
- direct_drive
- backdrivability
- physical_human_robot_interaction
- low_inertia
- workspace_optimization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from abstract and supplied metadata; full-text review is needed
    to confirm section citations, exact component specifications, and singularity
    assumptions.
sources:
- id: src_001
  type: paper
  title: Kinematic Analysis and Design of a Novel (6+3)-DoF Parallel Robot with Fixed
    Actuators
  url: https://arxiv.org/abs/2304.12499
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper introduces a kinematically redundant (6+3)-DoF parallel manipulator whose three identical legs are 3-DoF RU/2-RUS mechanisms. By mounting all motors on the fixed base, the design keeps reflected inertia low and enables backdrivable actuation, which is presented as advantageous for safe physical human-robot interaction. A preliminary CAD model is used to illustrate how direct-drive motors, timing-belt transmissions, carbon-fibre tubes, and aluminium parts can be integrated into a compact leg module.

The authors derive the inverse kinematics and Jacobian of the leg using screw theory, then analyze singularities under a simplifying geometric assumption. They also present a workspace-optimization strategy that maximizes the volume in which the leg end-effector can achieve 2g acceleration in every direction given a 10 Nm actuator torque limit. The resulting design is framed as a scalable building block for lightweight, force-controllable robotic limbs.

The work remains at the preliminary-design stage: no physical prototype is built or experimentally validated, and dynamic modelling is left for future research. The torque analysis assumes a conservative 0.5 kg point mass at the end-effector, which may not account for all moving-part inertias.

## Key Contributions

- Introduced a kinematically redundant (6+3)-DoF parallel robot with all motors fixed at the base for low reflected inertia and backdrivability.
- Derived inverse kinematics and Jacobian matrices of the 3-DoF RU/2-RUS leg mechanism using screw theory.
- Provided a simplified condition for type II singularities under the geometric assumption that spherical joint centers E and F are coincident.
- Optimized leg geometry to maximize the workspace where the end-effector can achieve 2g acceleration in all directions with 10 Nm actuator torque.
- Presented a preliminary CAD-based prototype design including direct-drive actuators, timing belts, carbon-fibre tubes, and aluminium structural parts.

## Relevance to Humanoid Robotics

The fixed-actuator, low-inertia, backdrivable parallel leg module addresses core requirements for humanoid robots that must interact physically with humans: low reflected inertia improves force controllability and safety during contact, while base-mounted actuators simplify cabling and thermal management. The paper explicitly frames the mechanism as a scalable building block for force-controllable joints and limbs. Its use of direct-drive actuation and modular RU/2-RUS legs is therefore relevant to the design of lightweight, mass-manufacturable hardware for humanoids.
