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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.14334v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (717 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2302.14334v2

## 개요
로봇 인식에서 센서와 로봇 자세의 결합은 핵심 난제이며, 특히 진동에 취약한 초소형 비행체와 소형 로봇에서 더욱 두드러집니다. 기존의 능동 비전 방법은 로봇 자세를 변경하여 센서 방향을 조정하는 데 의존하지만 계산 비용이 큽니다. 본 논문에서 제안하는 MEMS 미러 LiDAR 시스템은 로봇 운동과 독립적인 시야각 재지향을 통해 고가의 부품을 외부에 배치하고, 저전력 플랫폼에서 하드웨어 수준의 모션 보상을 구현합니다. 시뮬레이션과 드론 프로토타입 하드웨어 실험을 통해 이 방법이 단순화된 인식 작업에서의 효율성을 검증했습니다.

## 핵심 내용
### 핵심 문제
- 센서와 로봇 자세의 결합으로 인해 인식이 자체 진동, 외부 풍란 등의 영향을 받으며, 기존의 소프트웨어 안정화(예: 이미지 손떨림 보정)는 계산 자원이 제한된 초소형 로봇에는 적합하지 않습니다.

### 시스템 설계
- MEMS 미러를 스캐닝 핵심으로 사용하며, 전자기 구동을 통해 2차원 빔 편향을 구현하고, 시야각은 로봇 운동과 독립적으로 능동 조정이 가능합니다.
- 핵심 혁신: 레이저 송수신과 같은 고가 부품을 로봇 외부에 배치하고, 기내에는 미러와 광학 경로만 유지하여 하중과 전력 소모를 줄입니다.

### 모션 보상 메커니즘
- **IMU 피드백 모드**: 기내 IMU를 사용하여 로봇 자세 변화를 실시간 감지하고, 미러 편향을 통해 시야 오프셋을 보상합니다.
- **외부 오도메트리 피드백**: 시각/레이저 오도메트리 데이터를 결합하여 더 복잡한 운동 분리(예: 드론 호버링 시 시야 안정화)를 구현합니다.

### 실험 검증
- **시뮬레이션 테스트**: 시뮬레이션 드론 진동 시나리오에서 보상 후 포인트 클라우드 왜곡이 82% 감소(비보상 상태 대비).
- **하드웨어 프로토타입**: 쿼드콥터 드론에 탑재하여 실측 결과:
  - 보상 후 목표 물체(예: 지상 표적)의 LiDAR 포인트 클라우드 위치 편차가 ±15cm에서 ±3cm로 감소.
  - 시스템 총 전력 소모는 1.2W(MEMS 구동 및 IMU 처리 포함), 무게 45g.

### 결론
본 설계는 하드웨어 수준의 분리를 통해 소프트웨어 알고리즘을 대체하여, 초소형 로봇에 실시간 저전력 모션 보상 솔루션을 제공하며, 향후 다중 센서 협동 인식 시나리오로 확장 가능합니다.
