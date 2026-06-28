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
  en: Proposes modal-based forward and instantaneous kinematics for a 1-DoF pneumatic
    bellow soft actuator and uses fixed centrode deviation with nonlinear least-squares
    optimization to detect external contacts and estimate their location along the
    backbone.
  zh: 提出了一种基于模态的一自由度气动波纹管软体驱动器正运动学与瞬时运动学建模方法，并利用固定中心线偏差结合非线性最小二乘优化来检测外部接触并估计接触位置。
  ko: 1자유도 공기압 벨로우 연성 액츄에이터의 모달 기반 정운동학 및 순간운동학을 제안하고, 고정 중심선 편차법과 비선형 최소자승 최적화를 사용하여
    외부 접촉을 감지하고 백본 상의 접촉 위치를 추정한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper was not reviewed
    and the entry requires human review before promotion to verified.
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

## Overview

Soft robots can manipulate within constrained spaces while maintaining safe interaction with their surroundings. However, their adaptable compliance makes them susceptible to external contact forces that deform the robot shape and alter kinematic and dynamic behavior. This paper focuses on a 1-DoF pneumatic bellow bending actuator, a fundamental building block for complex multi-DoF soft robots, and develops a modal-based kinematic model for it.

The actuator backbone is represented as a spatial curve using an integral representation. Forward and instantaneous kinematics are computed explicitly through a modal approach. To handle external disturbances, the authors employ the fixed centrode deviation (FCD) method to detect contact events and formulate a nonlinear least-squares optimization problem to estimate the contact location along the backbone. Simulation and calibration results are reported, showing sub-pixel estimation error for contact location.

Contact force magnitude estimation is explicitly excluded from the scope. The reported validation is limited to a single 1-DoF pneumatic bellow actuator and relies on accurate extrinsic sensing of the end-effector pose.

## Key Contributions

- Modal-based forward and instantaneous kinematics for a 1-DoF pneumatic bellow soft actuator.
- Fixed centrode deviation (FCD) method for detecting external contact during actuator motion.
- Nonlinear least-squares optimization formulation for estimating contact location along the actuator backbone.
- Simulation and calibration validation demonstrating sub-pixel contact-location estimation error.

## Relevance to Humanoid Robotics

Pneumatic soft bellow actuators are fundamental building blocks for complex multi-DoF soft robots, including compliant limbs and joints for humanoid systems. Reliable kinematic modeling and contact detection are essential for safe, controllable interaction in unstructured environments where unexpected collisions are common.

By providing a computationally tractable method to estimate where contact occurs along a soft limb, this work supports trajectory planning, force-free control strategies, and safe physical human-robot interaction for future humanoid robots that incorporate soft actuation technologies.
