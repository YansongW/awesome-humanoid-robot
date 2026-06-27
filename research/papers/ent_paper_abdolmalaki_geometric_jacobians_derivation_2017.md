---
$id: ent_paper_abdolmalaki_geometric_jacobians_derivation_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometric Jacobians Derivation and Kinematic Singularity Analysis for Smokie
    Robot Manipulator & the Barrett WAM
  zh: Smokie机器人操作臂与Barrett WAM的几何雅可比推导及运动学奇异性分析
  ko: Smokie 로봇 매니퓰레이터 및 Barrett WAM의 기하학적 자코비안 도출과 운동학적 특이점 분석
summary:
  en: Derives the 6×6 geometric Jacobians and kinematic singularities of the 6-DOF
    Smokie OUR and Barrett WAM manipulators from Denavit-Hartenberg parameters and
    direct kinematics, and surveys redundant kinematic allocation schemes for the
    7-DOF Barrett WAM.
  zh: 基于D-H参数和正运动学，推导6自由度Smokie OUR与Barrett WAM机械臂的6×6几何雅可比矩阵和运动学奇异性，并综述7自由度Barrett
    WAM的冗余运动学分配方案。
  ko: D-H 파라미터와 정기구학을 바탕으로 6자유도 Smokie OUR 및 Barrett WAM 매니퓰레이터의 6×6 기하학적 자코비안과 운동학적
    특이점을 도출하고, 7자유도 Barrett WAM의 중복 운동학 할당 방식을 검토한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv abstract and supplied metadata; full-text review
    is needed to confirm component/material details and exact section citations.
sources:
- id: src_001
  type: paper
  title: Geometric Jacobians Derivation and Kinematic Singularity Analysis for Smokie
    Robot Manipulator & the Barrett WAM
  url: https://arxiv.org/abs/1707.04821
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper presents a kinematic analysis of two 6-degree-of-freedom (DOF) manipulators: the Smokie OUR arm and the Barrett WAM arm. It begins by establishing the Denavit-Hartenberg (D-H) parameters and direct kinematics for each arm, then uses these models to compute the full 6×6 geometric Jacobian matrices. The Jacobian is central to relating joint velocities to end-effector twists and to understanding where the arm loses degrees of freedom.

Singular configurations are located by examining the determinant and rank of the Jacobian matrix, with numerical evaluation carried out in MATLAB. Schematic and CAD illustrations are provided to visualize the singular poses of both robots. The authors note that the Smokie OUR arm lacks a spherical wrist, which prevents the decoupling of position and orientation singularities, while the Barrett WAM's analytical determinant is complicated and can yield imaginary values. The paper concludes with a survey of redundant kinematic allocation and inverse-kinematics schemes for the 7-DOF Barrett WAM.

## Key Contributions

- Derives D-H parameters and direct kinematics for the Smokie OUR and Barrett WAM arms.
- Computes the full 6×6 geometric Jacobian matrices for both manipulators.
- Identifies kinematic singularities by analyzing the determinant and rank deficiency of the Jacobian matrices.
- Provides schematic and CAD visualizations of the singular configurations for both robots.
- Surveys redundant kinematic allocation and inverse-kinematics schemes for the 7-DOF Barrett WAM.

## Relevance to Humanoid Robotics

Anthropomorphic, high-dexterity arms such as the Barrett WAM are directly applicable to humanoid robot arms, where reliable manipulation requires avoiding kinematic singularities and maintaining full end-effector controllability. The Jacobian-based singularity analysis presented here supports the design, control, and trajectory planning of humanoid arms in both research and industrial deployment. Understanding these singular configurations is essential for preventing control failure and loss of motion freedom during manipulation tasks.
