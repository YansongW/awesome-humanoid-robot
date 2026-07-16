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

## Overview
A fundamental challenge in robot perception is the coupling of the sensor pose and robot pose. This has led to research in active vision where robot pose is changed to reorient the sensor to areas of interest for perception. Further, egomotion such as jitter, and external effects such as wind and others affect perception requiring additional effort in software such as image stabilization. This effect is particularly pronounced in micro-air vehicles and micro-robots who typically are lighter and subject to larger jitter but do not have the computational capability to perform stabilization in real-time. We present a novel microelectromechanical (MEMS) mirror LiDAR system to change the field of view of the LiDAR independent of the robot motion. Our design has the potential for use on small, low-power systems where the expensive components of the LiDAR can be placed external to the small robot. We show the utility of our approach in simulation and on prototype hardware mounted on a UAV. We believe that this LiDAR and its compact movable scanning design provide mechanisms to decouple robot and sensor geometry allowing us to simplify robot perception. We also demonstrate examples of motion compensation using IMU and external odometry feedback in hardware.

## Content
A fundamental challenge in robot perception is the coupling of the sensor pose and robot pose. This has led to research in active vision where robot pose is changed to reorient the sensor to areas of interest for perception. Further, egomotion such as jitter, and external effects such as wind and others affect perception requiring additional effort in software such as image stabilization. This effect is particularly pronounced in micro-air vehicles and micro-robots who typically are lighter and subject to larger jitter but do not have the computational capability to perform stabilization in real-time. We present a novel microelectromechanical (MEMS) mirror LiDAR system to change the field of view of the LiDAR independent of the robot motion. Our design has the potential for use on small, low-power systems where the expensive components of the LiDAR can be placed external to the small robot. We show the utility of our approach in simulation and on prototype hardware mounted on a UAV. We believe that this LiDAR and its compact movable scanning design provide mechanisms to decouple robot and sensor geometry allowing us to simplify robot perception. We also demonstrate examples of motion compensation using IMU and external odometry feedback in hardware.

## 개요
로봇 인식의 근본적인 도전 과제는 센서 자세와 로봇 자세의 결합입니다. 이로 인해 로봇 자세를 변경하여 센서를 인식에 필요한 관심 영역으로 재조정하는 능동 시각(active vision) 연구가 진행되었습니다. 또한, 떨림과 같은 자체 운동 및 바람과 같은 외부 영향은 이미지 안정화와 같은 소프트웨어에서 추가적인 노력을 필요로 하여 인식에 영향을 미칩니다. 이러한 효과는 일반적으로 더 가볍고 큰 떨림에 노출되지만 실시간 안정화를 수행할 계산 능력이 부족한 초소형 항공기 및 마이크로 로봇에서 특히 두드러집니다. 우리는 로봇 움직임과 독립적으로 LiDAR의 시야를 변경하는 새로운 미세전자기계(MEMS) 미러 LiDAR 시스템을 제시합니다. 우리의 설계는 LiDAR의 고가 구성 요소를 소형 로봇 외부에 배치할 수 있는 소형 저전력 시스템에서 사용될 가능성이 있습니다. 우리는 시뮬레이션과 UAV에 장착된 프로토타입 하드웨어에서 접근 방식의 유용성을 보여줍니다. 이 LiDAR와 그 컴팩트한 이동식 스캐닝 설계가 로봇과 센서 기하학을 분리하는 메커니즘을 제공하여 로봇 인식을 단순화할 수 있다고 믿습니다. 또한 하드웨어에서 IMU 및 외부 주행 거리 측정 피드백을 사용한 모션 보상 예시를 시연합니다.

## 핵심 내용
로봇 인식의 근본적인 도전 과제는 센서 자세와 로봇 자세의 결합입니다. 이로 인해 로봇 자세를 변경하여 센서를 인식에 필요한 관심 영역으로 재조정하는 능동 시각 연구가 진행되었습니다. 또한, 떨림과 같은 자체 운동 및 바람과 같은 외부 영향은 이미지 안정화와 같은 소프트웨어에서 추가적인 노력을 필요로 하여 인식에 영향을 미칩니다. 이러한 효과는 일반적으로 더 가볍고 큰 떨림에 노출되지만 실시간 안정화를 수행할 계산 능력이 부족한 초소형 항공기 및 마이크로 로봇에서 특히 두드러집니다. 우리는 로봇 움직임과 독립적으로 LiDAR의 시야를 변경하는 새로운 미세전자기계(MEMS) 미러 LiDAR 시스템을 제시합니다. 우리의 설계는 LiDAR의 고가 구성 요소를 소형 로봇 외부에 배치할 수 있는 소형 저전력 시스템에서 사용될 가능성이 있습니다. 우리는 시뮬레이션과 UAV에 장착된 프로토타입 하드웨어에서 접근 방식의 유용성을 보여줍니다. 이 LiDAR와 그 컴팩트한 이동식 스캐닝 설계가 로봇과 센서 기하학을 분리하는 메커니즘을 제공하여 로봇 인식을 단순화할 수 있다고 믿습니다. 또한 하드웨어에서 IMU 및 외부 주행 거리 측정 피드백을 사용한 모션 보상 예시를 시연합니다.
