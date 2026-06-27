---
$id: ent_paper_adorno_dq_robotics_a_library_for_robo_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DQ Robotics: a Library for Robot Modeling and Control'
  zh: DQ Robotics：用于机器人建模与控制的库
  ko: 'DQ Robotics: 로봇 모델링 및 제어를 위한 라이브러리'
summary:
  en: Introduces DQ Robotics, an open-source library that implements dual quaternion
    algebra for robot modeling and control across Python, MATLAB, and C++, supporting
    serial manipulators, mobile manipulators, cooperative dual arms, and humanoids.
  zh: 介绍 DQ Robotics，一个跨 Python、MATLAB 和 C++ 实现双四元数代数、用于机器人建模与控制的开源库，支持串联机械臂、移动机械臂、协作双臂和人形机器人。
  ko: Python, MATLAB, C++를 통합 API로 제공하는 이중사원수 대수를 활용한 로봇 모델링 및 제어 오픈소스 라이브러리 DQ Robotics를
    소개하며, 직렬 조작기, 이동 조작기, 협력 이중 팔 및 휴머노이드를 지원한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- tool_equipment
- knowledge
tags:
- dual_quaternion
- robot_modeling
- kinematic_control
- whole_body_control
- software_library
- humanoid_robot
- ros_interface
- v_rep_interface
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; source citations should
    be verified against the full paper before promotion.
sources:
- id: src_001
  type: paper
  title: 'DQ Robotics: a Library for Robot Modeling and Control'
  url: https://arxiv.org/abs/1910.11612
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

DQ Robotics is an open-source library that bridges the gap between dual quaternion theory and practical robot implementation. It provides a unified application programming interface across Python, MATLAB, and C++, allowing the same dual quaternion expressions to be used for teaching, rapid prototyping, and deployment on real systems. The library treats geometric objects such as points, lines, planes, spheres, and infinite cylinders as dual quaternion entities, and it supplies operators and Jacobians that let users express kinematic relationships and constraints in a compact, geometrically intuitive form.

The paper explains how DQ Robotics can model serial manipulators, mobile bases, mobile manipulators, cooperative dual-arm systems, and branched mechanisms such as humanoids. It also includes a collection of kinematic controllers based on pseudoinverse, quadratic programming (QP), and constrained optimization formulations, together with interfaces to ROS and V-REP. By packaging these capabilities behind a consistent API, the authors aim to make dual quaternion-based modeling and control accessible for education while remaining efficient enough for real-world applications.

Validation results presented in the paper cover several physical robotic platforms, including surgical robots, mobile manipulators, and humanoids. The authors argue that the library's performance and expressiveness make it suitable for whole-body control tasks on complex robotic systems.

## Key Contributions

- Unified dual quaternion algebra API across Python, MATLAB, and C++.
- Kinematic modeling for serial manipulators, mobile bases, mobile manipulators, cooperative dual arms, and branched mechanisms.
- Built-in geometric primitives (points, lines, planes, spheres, infinite cylinders) and their Jacobians for constrained control.
- Ready-to-use kinematic controllers, including pseudoinverse, QP-based, and constrained controllers, plus ROS and V-REP interfaces.
- Experimental validation on real robotic platforms such as surgical robots, mobile manipulators, and humanoids.

## Relevance to Humanoid Robotics

The paper explicitly includes branched mechanisms in its modeling scope and reports whole-body control applications on humanoid robots. Because humanoids are branched, multi-degree-of-freedom systems, a unified dual quaternion framework can simplify the representation of whole-body poses, constraints, and task Jacobians. The library's controller set and geometric primitives therefore provide tools that are directly usable for humanoid modeling, motion generation, and deployment.
