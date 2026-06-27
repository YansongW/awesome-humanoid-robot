---
$id: ent_paper_chen_design_of_an_adaptive_lightwei_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design of an Adaptive Lightweight LiDAR to Decouple Robot-Camera Geometry
  zh: 用于解耦机器人-相机几何结构自适应轻量激光雷达设计
  ko: 로봇-카메라 기하학을 분리하는 적응형 경량 LiDAR 설계
summary:
  en: This paper proposes a lightweight MEMS-mirror LiDAR that actively reorients
    its field of view using IMU or external pose feedback, decoupling sensor geometry
    from robot motion to enable hardware-level motion compensation on small robots
    and UAVs.
  zh: 本文提出一种轻量MEMS镜激光雷达，利用IMU或外部位姿反馈主动重定向视场，将传感器几何与机器人运动解耦，从而在小型机器人和无人机上实现硬件级运动补偿。
  ko: 본 논문은 IMU 또는 외부 포즈 피드백을 사용하여 시야를 능동적으로 재조향하는 경량 MEMS 미러 LiDAR를 제안하여, 소형 로봇과
    UAV에서 센서 기하학과 로봇 동작을 분리하고 하드웨어 수준의 모션 보상을 가능하게 한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- component
- system
tags:
- mems_lidar
- sensor_motion_compensation
- lidar_inertial_odometry
- active_vision
- lightweight_lidar
- robot_sensor_decoupling
- hardware_motion_compensation
- uav_perception
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: Design of an Adaptive Lightweight LiDAR to Decouple Robot-Camera Geometry
  url: https://arxiv.org/abs/2302.14334
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

A fundamental challenge in robot perception is the rigid coupling between sensor pose and robot pose, which forces small robots to rely on computationally expensive software stabilization to counteract egomotion jitter and external disturbances such as wind. This paper proposes an adaptive, lightweight LiDAR based on a microelectromechanical (MEMS) mirror that can actively redirect its beam and change its field of view independently of the robot's motion. By placing heavier LiDAR electronics off-board and keeping only a compact scanning head on the robot, the design is aimed at micro-air vehicles and other small, low-power platforms.

The system uses onboard IMU data or external odometry feedback to compensate for robot motion in hardware. The authors characterize the MEMS mirror geometrically and develop control algorithms for several compensation modes, including full SO(3) rotation compensation, two-axis gimbal-style compensation, rotational field-of-view stabilization, and target aiming. They validate the approach in AirSim/Unreal Engine simulations and on a physical UAV prototype equipped with the MEMS LiDAR, an IMU, and an Arduino controller.

Experimental results reported in the paper include reduced odometry error and stabilized point clouds compared with uncompensated sensing. The authors also release an open-source adaptation of LIO-SAM that supports rotation-compensated LiDAR-inertial odometry for their hardware.

## Key Contributions

- Design of a lightweight MEMS-mirror LiDAR with wide non-resonant scanning angles and high-rate hardware motion compensation.
- Geometric characterization and compensation control algorithms for full SO(3) rotation compensation, two-axis gimbal-style compensation, rotational FoV stabilization, and target aiming.
- Simulation validation in AirSim/Unreal Engine Blocks and Mountains scenes and hardware validation on a UAV prototype using IMU and external odometry feedback.
- Open-source adaptation of LIO-SAM to support rotation-compensated LiDAR-inertial odometry.

## Relevance to Humanoid Robotics

Humanoid robots experience significant locomotion-induced jitter and payload constraints, making stable onboard perception challenging. The hardware-level motion compensation and sensor-robot geometry decoupling demonstrated in this paper can be directly transferred to humanoid platforms, potentially enabling lighter onboard LiDAR sensing and reducing the need for heavy software stabilization pipelines. The ability to stabilize the LiDAR field of view independently of base motion is particularly relevant for legged systems where torso oscillations are inherent during walking.
