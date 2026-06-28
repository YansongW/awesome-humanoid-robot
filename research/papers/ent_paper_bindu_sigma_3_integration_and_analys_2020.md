---
$id: ent_paper_bindu_sigma_3_integration_and_analys_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sigma-3: Integration and Analysis of a 6 DOF Robotic Arm Configuration in a
    Rescue Robot'
  zh: Sigma-3：救援机器人中六自由度机械臂配置的集成与分析
  ko: 'Sigma-3: 구조 로봇의 6자유도 로봇 팔 구성 통합 및 분석'
summary:
  en: This paper presents Sigma-3, a teleoperated rescue robot integrating a 6-DOF
    robotic arm driven by MG996R servo motors, and experimentally evaluates kinematic
    modeling, end-effector control, oscillation damping, and power consumption.
  zh: 本文介绍了Sigma-3，一种集成由MG996R伺服电机驱动的六自由度机械臂的遥控救援机器人，并实验评估了运动学建模、末端执行器控制、振荡抑制和功耗。
  ko: 본 논문은 MG996R 서보 모터로 구동되는 6자유도 로봇 팔을 통합한 원격 조종 구조 로봇 Sigma-3를 제시하고, 운동학 모델링,
    엔드이펙터 제어, 진동 감쇠 및 전력 소비를 실험적으로 평가한다.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- system
tags:
- rescue_robot
- six_dof_arm
- servo_motor
- inverse_kinematics
- rotation_matrix
- oscillation_damping
- mobile_manipulator
- teleoperation
- mg996r
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from abstract and supplied metadata; full-text verification
    is required before upgrading to verified.
sources:
- id: src_001
  type: paper
  title: 'Sigma-3: Integration and Analysis of a 6 DOF Robotic Arm Configuration in
    a Rescue Robot'
  url: https://arxiv.org/abs/2002.11944
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Sigma-3 is a low-cost rescue robot developed for hazardous or inaccessible environments where humans cannot safely operate. The platform is built around a 6-DOF robotic arm integrated with a passive double-track mobile base, a hydraulic shock absorber, and a pan-tilt Raspberry Pi camera for remote environmental assessment. The arm is constructed from four types of rigid joints and is actuated by six MG996R high-torque servo motors, with kinematic modeling grounded in rotation matrices, Euler angles, and inverse kinematics.

The authors evaluate the mechanism through hands-on testing focused on oscillation damping, torque requirements, and power consumption. The reported oscillation damping error is less than 3%, and the operating-time experiments are used to defend the mechanism's low-power-consumption capability. The robot is designed to be remotely controlled, positioning it as a teleoperated helper for disaster-response scenarios rather than an autonomous field robot.

## Key Contributions

- Novel mechanism design for measuring rotation, joints, and links of a 6-DOF arm integrated with the Sigma-3 rescue robot.
- Precise end-effector motion control over three dimensions using rotation matrices and inverse kinematics.
- Experimental validation showing less than 3% error in oscillation damping performance during hands-on testing.
- Torque and power-consumption analysis for six MG996R servo motors supporting the arm.
- Integration of a passive double-track mobile base with a shock absorber and pan-tilt camera for rough-terrain rescue missions.

## Relevance to Humanoid Robotics

The kinematic modeling, servo-motor sizing, power budgeting, and oscillation-damping techniques developed for Sigma-3's 6-DOF manipulator are directly transferable to humanoid robot arm design. Humanoid platforms likewise require lightweight, low-cost serial arms with accurate end-effector positioning and efficient actuation in unstructured environments. The paper's combination of rotation-matrix-based forward orientation modeling and inverse-kinematics-based position control provides a practical reference for similar humanoid upper-limb implementations.
