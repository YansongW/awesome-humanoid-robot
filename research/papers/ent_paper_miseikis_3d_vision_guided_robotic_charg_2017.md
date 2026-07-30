---
$id: ent_paper_miseikis_3d_vision_guided_robotic_charg_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 3D Vision Guided Robotic Charging Station for Electric and Plug-in Hybrid Vehicles
  zh: 面向电动和插电式混合动力汽车的3D视觉引导机器人充电站
  ko: 전기 및 플러그인 하이브리드 차량을 위한 3D 비전 기반 로봇 충전 스테이션
summary:
  en: This 2017 arXiv paper presents an automated robotic charging station that uses a stereo-camera 3D vision system, shape-based
    matching, and a UR10 arm to locate and plug into EV/PHEV charging ports without vehicle modification.
  zh: 本文提出一种基于3D视觉引导的自动机器人充电站，使用立体相机、形状匹配算法和UR10机械臂，无需改装车辆即可定位并插入电动汽车/插电式混合动力汽车充电接口。核心贡献在于通过形状匹配实现充电口位姿精确识别，并利用连接器插头结构完成相机-机器人系统标定。
  ko: 이 2017년 arXiv 논문은 스테레오 카메라 3D 비전 시스템, 형상 기반 매칭 및 UR10 로봇 암을 사용하여 차량을 개조하지 않고도 EV/PHEV 충전 포트를 찾아 연결하는 자동 로봇 충전 스테이션을
    제시한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
- intelligence
tags:
- robotic_charging
- ev_charging
- 3d_vision
- stereo_vision
- shape_based_matching
- visual_servoing
- hand_eye_calibration
- markerless_calibration
- force_monitored_insertion
- plug_insertion
- ur10
- contact_rich_manipulation
- manipulation_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1703.05381v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 3D Vision Guided Robotic Charging Station for Electric and Plug-in Hybrid Vehicles
  url: https://arxiv.org/abs/1703.05381
  date: '2017'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该2017年arXiv论文针对电动汽车充电不便的问题，设计了一套全自动机器人充电系统。系统由立体相机3D视觉模块、UR10协作机器人和充电站组成，通过形状匹配算法识别充电口并获取精确位姿，无需车辆预装特殊标记。标定过程利用充电插头自身结构完成，避免了额外标定物。机器人采用三步运动规划策略完成插拔动作，实验验证了系统有效性。

## 核心内容
### 系统架构
- 硬件组成：立体相机3D视觉系统 + UR10六轴协作机器人 + 充电站
- 核心流程：视觉定位 → 位姿解算 → 机器人运动规划 → 插拔执行

### 视觉定位方法
- 采用形状匹配（shape-based matching）算法识别充电口
- 通过立体相机获取3D点云数据，计算充电口精确六自由度位姿
- 无需车辆改装或额外标记，仅依赖充电口几何特征

### 标定方案
- 利用充电连接器插头的已知结构完成相机-机器人手眼标定
- 无需棋盘格或标定板，简化部署流程

### 运动规划策略
- 三步插接流程：
  1. 粗定位：基于视觉引导将机械臂移至充电口附近
  2. 精对准：通过力/位混合控制调整末端姿态
  3. 插接执行：沿充电口轴向完成插入动作

### 实验验证
- 在真实充电场景中完成多组插拔测试
- 成功实现自动插拔，未报告具体成功率数值
- 系统响应时间与定位精度受限于立体相机性能（未提供具体参数）

## Overview
Electric vehicles (EVs) and plug-in hybrid vehicles (PHEVs) are rapidly gaining popularity on our roads. Besides a comparatively high purchasing price, the main two problems limiting their use are the short driving range and inconvenient charging process. In this paper we address the following by presenting an automatic robot-based charging station with 3D vision guidance for plugging and unplugging the charger. First of all, the whole system concept consisting of a 3D vision system, an UR10 robot and a charging station is presented. Then we show the shape-based matching methods used to successfully identify and get the exact pose of the charging port. The same approach is used to calibrate the camera-robot system by using just known structure of the connector plug and no additional markers. Finally, a three-step robot motion planning procedure for plug-in is presented and functionality is demonstrated in a series of successful experiments.

## 개요
전기차(EV)와 플러그인 하이브리드 차량(PHEV)이 도로에서 빠르게 인기를 얻고 있습니다. 비교적 높은 구매 가격 외에도, 사용을 제한하는 주요 두 가지 문제는 짧은 주행 거리와 불편한 충전 과정입니다. 본 논문에서는 충전기를 연결 및 분리하기 위한 3D 비전 유도 기능을 갖춘 자동 로봇 기반 충전 스테이션을 제시하여 이 문제를 다룹니다. 먼저, 3D 비전 시스템, UR10 로봇 및 충전 스테이션으로 구성된 전체 시스템 개념을 소개합니다. 그런 다음 충전 포트를 성공적으로 식별하고 정확한 자세를 얻는 데 사용된 형상 기반 매칭 방법을 보여줍니다. 동일한 접근 방식을 사용하여 추가 마커 없이 커넥터 플러그의 알려진 구조만으로 카메라-로봇 시스템을 보정합니다. 마지막으로, 플러그인을 위한 3단계 로봇 동작 계획 절차를 제시하고 일련의 성공적인 실험을 통해 기능을 입증합니다.

## 핵심 내용
전기차(EV)와 플러그인 하이브리드 차량(PHEV)이 도로에서 빠르게 인기를 얻고 있습니다. 비교적 높은 구매 가격 외에도, 사용을 제한하는 주요 두 가지 문제는 짧은 주행 거리와 불편한 충전 과정입니다. 본 논문에서는 충전기를 연결 및 분리하기 위한 3D 비전 유도 기능을 갖춘 자동 로봇 기반 충전 스테이션을 제시하여 이 문제를 다룹니다. 먼저, 3D 비전 시스템, UR10 로봇 및 충전 스테이션으로 구성된 전체 시스템 개념을 소개합니다. 그런 다음 충전 포트를 성공적으로 식별하고 정확한 자세를 얻는 데 사용된 형상 기반 매칭 방법을 보여줍니다. 동일한 접근 방식을 사용하여 추가 마커 없이 커넥터 플러그의 알려진 구조만으로 카메라-로봇 시스템을 보정합니다. 마지막으로, 플러그인을 위한 3단계 로봇 동작 계획 절차를 제시하고 일련의 성공적인 실험을 통해 기능을 입증합니다.

## 参考
- http://arxiv.org/abs/1703.05381v1
