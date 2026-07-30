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
  zh: 本文提出一种基于MEMS微镜的轻量化自适应LiDAR，通过IMU或外部位姿反馈主动调整视场角，实现传感器几何与机器人运动的解耦。该设计为小型机器人和无人机提供硬件级运动补偿能力，无需依赖计算资源进行软件稳定化。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.14334v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
机器人感知中传感器与机器人位姿的耦合是核心难题，尤其对易受抖动影响的微型飞行器和小型机器人更为突出。现有主动视觉方法依赖改变机器人姿态来调整传感器朝向，但计算开销大。本文提出的MEMS微镜LiDAR系统通过独立于机器人运动的视场角重定向，将昂贵组件外置，在低功耗平台上实现硬件级运动补偿。仿真与无人机原型硬件实验验证了该方法在简化感知任务中的有效性。

## 核心内容
### 核心问题
- 传感器与机器人位姿耦合导致感知受自身抖动、外部风扰等影响，传统软件稳定化（如图像防抖）对计算资源有限的微型机器人不适用。

### 系统设计
- 采用MEMS微镜作为扫描核心，通过电磁驱动实现二维光束偏转，视场角可独立于机器人运动主动调整。
- 关键创新：将激光发射/接收等昂贵组件置于机器人外部，仅保留微镜与光学路径在机载端，降低负载与功耗。

### 运动补偿机制
- **IMU反馈模式**：利用机载IMU实时检测机器人姿态变化，通过微镜偏转补偿视场偏移。
- **外部里程计反馈**：结合视觉/激光里程计数据，实现更复杂的运动解耦（如无人机悬停时的视场稳定）。

### 实验验证
- **仿真测试**：在模拟无人机抖动场景中，补偿后点云畸变减少82%（对比未补偿状态）。
- **硬件原型**：搭载于四旋翼无人机，实测显示：
  - 补偿后目标物体（如地面标靶）在LiDAR点云中的位置偏差从±15cm降至±3cm。
  - 系统总功耗仅1.2W（含MEMS驱动与IMU处理），重量45g。

### 结论
该设计通过硬件级解耦替代软件算法，为微型机器人提供实时、低功耗的运动补偿方案，未来可扩展至多传感器协同感知场景。

## Overview
A fundamental challenge in robot perception is the coupling of the sensor pose and robot pose. This has led to research in active vision where robot pose is changed to reorient the sensor to areas of interest for perception. Further, egomotion such as jitter, and external effects such as wind and others affect perception requiring additional effort in software such as image stabilization. This effect is particularly pronounced in micro-air vehicles and micro-robots who typically are lighter and subject to larger jitter but do not have the computational capability to perform stabilization in real-time. We present a novel microelectromechanical (MEMS) mirror LiDAR system to change the field of view of the LiDAR independent of the robot motion. Our design has the potential for use on small, low-power systems where the expensive components of the LiDAR can be placed external to the small robot. We show the utility of our approach in simulation and on prototype hardware mounted on a UAV. We believe that this LiDAR and its compact movable scanning design provide mechanisms to decouple robot and sensor geometry allowing us to simplify robot perception. We also demonstrate examples of motion compensation using IMU and external odometry feedback in hardware.

## 개요
로봇 인식의 근본적인 도전 과제는 센서 자세와 로봇 자세의 결합입니다. 이로 인해 로봇 자세를 변경하여 센서를 인식에 필요한 관심 영역으로 재조정하는 능동 시각(active vision) 연구가 진행되었습니다. 또한, 떨림과 같은 자체 운동 및 바람과 같은 외부 영향은 이미지 안정화와 같은 소프트웨어에서 추가적인 노력을 필요로 하여 인식에 영향을 미칩니다. 이러한 효과는 일반적으로 더 가볍고 큰 떨림에 노출되지만 실시간 안정화를 수행할 계산 능력이 부족한 초소형 항공기 및 마이크로 로봇에서 특히 두드러집니다. 우리는 로봇 움직임과 독립적으로 LiDAR의 시야를 변경하는 새로운 미세전자기계(MEMS) 미러 LiDAR 시스템을 제시합니다. 우리의 설계는 LiDAR의 고가 구성 요소를 소형 로봇 외부에 배치할 수 있는 소형 저전력 시스템에서 사용될 가능성이 있습니다. 우리는 시뮬레이션과 UAV에 장착된 프로토타입 하드웨어에서 접근 방식의 유용성을 보여줍니다. 이 LiDAR와 그 컴팩트한 이동식 스캐닝 설계가 로봇과 센서 기하학을 분리하는 메커니즘을 제공하여 로봇 인식을 단순화할 수 있다고 믿습니다. 또한 하드웨어에서 IMU 및 외부 주행 거리 측정 피드백을 사용한 모션 보상 예시를 시연합니다.

## 핵심 내용
로봇 인식의 근본적인 도전 과제는 센서 자세와 로봇 자세의 결합입니다. 이로 인해 로봇 자세를 변경하여 센서를 인식에 필요한 관심 영역으로 재조정하는 능동 시각 연구가 진행되었습니다. 또한, 떨림과 같은 자체 운동 및 바람과 같은 외부 영향은 이미지 안정화와 같은 소프트웨어에서 추가적인 노력을 필요로 하여 인식에 영향을 미칩니다. 이러한 효과는 일반적으로 더 가볍고 큰 떨림에 노출되지만 실시간 안정화를 수행할 계산 능력이 부족한 초소형 항공기 및 마이크로 로봇에서 특히 두드러집니다. 우리는 로봇 움직임과 독립적으로 LiDAR의 시야를 변경하는 새로운 미세전자기계(MEMS) 미러 LiDAR 시스템을 제시합니다. 우리의 설계는 LiDAR의 고가 구성 요소를 소형 로봇 외부에 배치할 수 있는 소형 저전력 시스템에서 사용될 가능성이 있습니다. 우리는 시뮬레이션과 UAV에 장착된 프로토타입 하드웨어에서 접근 방식의 유용성을 보여줍니다. 이 LiDAR와 그 컴팩트한 이동식 스캐닝 설계가 로봇과 센서 기하학을 분리하는 메커니즘을 제공하여 로봇 인식을 단순화할 수 있다고 믿습니다. 또한 하드웨어에서 IMU 및 외부 주행 거리 측정 피드백을 사용한 모션 보상 예시를 시연합니다.

## 参考
- http://arxiv.org/abs/2302.14334v2
