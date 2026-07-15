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
  en: This paper proposes a lightweight MEMS-mirror LiDAR that actively reorients its field of view using IMU or external
    pose feedback, decoupling sensor geometry from robot motion to enable hardware-level motion compensation on small robots
    and UAVs.
  zh: A fundamental challenge in robot perception is the coupling of the sensor pose and robot pose. This has led to research
    in active vision where robot pose is changed to reorient the sensor to areas of interest for perception. Further, egomotion
    such as jitter, and external effects such as wind and others affect perception requiring additional effort in software
    such as image stabilization. This effect is particularly pronounced in micro-air vehicles and micro-robots who typically
    are lighter and subject to larger jitter but do not have the computational capability to perform stabilization in re
  ko: 본 논문은 IMU 또는 외부 포즈 피드백을 사용하여 시야를 능동적으로 재조향하는 경량 MEMS 미러 LiDAR를 제안하여, 소형 로봇과 UAV에서 센서 기하학과 로봇 동작을 분리하고 하드웨어 수준의 모션 보상을
    가능하게 한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.14334v2.
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

## 概述
A fundamental challenge in robot perception is the coupling of the sensor pose and robot pose. This has led to research in active vision where robot pose is changed to reorient the sensor to areas of interest for perception. Further, egomotion such as jitter, and external effects such as wind and others affect perception requiring additional effort in software such as image stabilization. This effect is particularly pronounced in micro-air vehicles and micro-robots who typically are lighter and subject to larger jitter but do not have the computational capability to perform stabilization in real-time. We present a novel microelectromechanical (MEMS) mirror LiDAR system to change the field of view of the LiDAR independent of the robot motion. Our design has the potential for use on small, low-power systems where the expensive components of the LiDAR can be placed external to the small robot. We show the utility of our approach in simulation and on prototype hardware mounted on a UAV. We believe that this LiDAR and its compact movable scanning design provide mechanisms to decouple robot and sensor geometry allowing us to simplify robot perception. We also demonstrate examples of motion compensation using IMU and external odometry feedback in hardware.

## 核心内容
A fundamental challenge in robot perception is the coupling of the sensor pose and robot pose. This has led to research in active vision where robot pose is changed to reorient the sensor to areas of interest for perception. Further, egomotion such as jitter, and external effects such as wind and others affect perception requiring additional effort in software such as image stabilization. This effect is particularly pronounced in micro-air vehicles and micro-robots who typically are lighter and subject to larger jitter but do not have the computational capability to perform stabilization in real-time. We present a novel microelectromechanical (MEMS) mirror LiDAR system to change the field of view of the LiDAR independent of the robot motion. Our design has the potential for use on small, low-power systems where the expensive components of the LiDAR can be placed external to the small robot. We show the utility of our approach in simulation and on prototype hardware mounted on a UAV. We believe that this LiDAR and its compact movable scanning design provide mechanisms to decouple robot and sensor geometry allowing us to simplify robot perception. We also demonstrate examples of motion compensation using IMU and external odometry feedback in hardware.

## 参考
- http://arxiv.org/abs/2302.14334v2


