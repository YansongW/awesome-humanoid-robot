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
  en: Introduces DQ Robotics, an open-source library that implements dual quaternion algebra for robot modeling and control
    across Python, MATLAB, and C++, supporting serial manipulators, mobile manipulators, cooperative dual arms, and humanoids.
  zh: 介绍 DQ Robotics，一个跨 Python、MATLAB 和 C++ 实现双四元数代数、用于机器人建模与控制的开源库，支持串联机械臂、移动机械臂、协作双臂和人形机器人。
  ko: Python, MATLAB, C++를 통합 API로 제공하는 이중사원수 대수를 활용한 로봇 모델링 및 제어 오픈소스 라이브러리 DQ Robotics를 소개하며, 직렬 조작기, 이동 조작기, 협력 이중 팔 및
    휴머노이드를 지원한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1910.11612v3.
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
## 概述
Dual quaternion algebra and its application to robotics have gained considerable interest in the last two decades. Dual quaternions have great geometric appeal and easily capture physical phenomena inside an algebraic framework that is useful for both robot modeling and control. Mathematical objects, such as points, lines, planes, infinite cylinders, spheres, coordinate systems, twists, and wrenches are all well defined as dual quaternions. Therefore, simple operators are used to represent those objects in different frames and operations such as inner products and cross products are used to extract useful geometric relationships between them. Nonetheless, the dual quaternion algebra is not widespread as it could be, mostly because efficient and easy-to-use computational tools are not abundant and usually are restricted to the particular algebra of quaternions. To bridge this gap between theory and implementation, this paper introduces DQ Robotics, a library for robot modeling and control using dual quaternion algebra that is easy to use and intuitive enough to be used for self-study and education while being computationally efficient for deployment on real applications.

## 核心内容
Dual quaternion algebra and its application to robotics have gained considerable interest in the last two decades. Dual quaternions have great geometric appeal and easily capture physical phenomena inside an algebraic framework that is useful for both robot modeling and control. Mathematical objects, such as points, lines, planes, infinite cylinders, spheres, coordinate systems, twists, and wrenches are all well defined as dual quaternions. Therefore, simple operators are used to represent those objects in different frames and operations such as inner products and cross products are used to extract useful geometric relationships between them. Nonetheless, the dual quaternion algebra is not widespread as it could be, mostly because efficient and easy-to-use computational tools are not abundant and usually are restricted to the particular algebra of quaternions. To bridge this gap between theory and implementation, this paper introduces DQ Robotics, a library for robot modeling and control using dual quaternion algebra that is easy to use and intuitive enough to be used for self-study and education while being computationally efficient for deployment on real applications.

## 参考
- http://arxiv.org/abs/1910.11612v3

