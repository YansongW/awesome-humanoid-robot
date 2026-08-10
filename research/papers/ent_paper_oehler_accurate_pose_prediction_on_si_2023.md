---
$id: ent_paper_oehler_accurate_pose_prediction_on_si_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Accurate Pose Prediction on Signed Distance Fields for Mobile Ground Robots in Rough Terrain
  zh: 粗糙地形移动地面机器人有符号距离场精确姿态预测
  ko: 거친 지형에서 이동 지상 로봇을 위한 부호 거리 장의 정확한 자세 예측
summary:
  en: Presents an iterative geometric method that predicts the 3D pose of mobile ground robots with active flippers on uneven
    terrain by settling the robot against an Euclidean Signed Distance Field, achieving 3.11 cm and 3.91° average accuracy
    on real tracked robots.
  zh: 本文提出一种迭代几何方法，通过将移动地面机器人（配备主动履带）与欧几里得符号距离场（Euclidean Signed Distance Field）进行匹配，预测其在崎岖地形上的3D位姿。该方法在真实履带机器人上实现了平均3.11厘米的位置精度和3.91°的姿态精度，并作为开源ROS包发布。
  ko: 활성 플리퍼를 갖춘 이동 지상 로봇의 거친 지형에서 3차원 자세를 예측하는 반복 기하학적 방법을 제안하며, 실제 궤형 로봇에서 평균 위치 오차 3.11cm, 방향 오차 3.91°를 달성한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- sdf_contact_estimation
- esdf
- pose_prediction
- rough_terrain
- active_flippers
- robot_terrain_interaction
- whole_body_planning
- ros1
verification:
  status: partially_verified
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.02121v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (649 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Accurate Pose Prediction on Signed Distance Fields for Mobile Ground Robots in Rough Terrain
  url: https://arxiv.org/abs/2405.02121
  date: '2023'
  accessed_at: '2026-06-28'
  doi: 10.1109/SSRR59696.2023.10499944
theoretical_depth:
- method
---
## 概述
针对非结构化环境中移动地面机器人的自主导航与履带控制问题，现有基于占据网格或可通行性地图的启发式方法因未考虑关节位置而限制了主动履带机器人的动作能力。本文提出一种新颖的迭代几何方法，利用符号距离场（Signed Distance Fields）的亚体素表面表示能力，在在线规划场景下高精度预测机器人的3D位姿。该方法在两种不同履带机器人的仿真与真实平台实验中，相比近期基于高度图的方法，实现了更优的定位与定向精度。

## 核心内容
### 方法核心
- 利用欧几里得符号距离场（Euclidean Signed Distance Field）的亚体素精度特性，通过迭代几何匹配将机器人模型“沉降”至地形表面。
- 输入为机器人关节角度与地形SDF，输出为预测的3D位姿（位置+姿态），支持在线规划。

### 实验设置
- **平台**：两种不同尺寸的履带机器人（仿真+真实平台）。
- **对比基准**：基于高度图（heightmap）的近期方法。
- **真值系统**：运动捕捉系统（ground truth tracking system）。

### 关键结果
- **位置精度**：平均误差3.11 cm。
- **姿态精度**：平均误差3.91°。
- **性能对比**：显著优于高度图方法，尤其在复杂地形下。

### 结论与开源
- 该方法为主动履带机器人在非结构化地形上的位姿预测提供了高精度、低延迟的解决方案。
- 实现已作为开源ROS包发布，便于社区复现与扩展。

## Overview
Autonomous locomotion for mobile ground robots in unstructured environments such as waypoint navigation or flipper control requires a sufficiently accurate prediction of the robot-terrain interaction. Heuristics like occupancy grids or traversability maps are widely used but limit actions available to robots with active flippers as joint positions are not taken into account. We present a novel iterative geometric method to predict the 3D pose of mobile ground robots with active flippers on uneven ground with high accuracy and online planning capabilities. This is achieved by utilizing the ability of signed distance fields to represent surfaces with sub-voxel accuracy. The effectiveness of the presented approach is demonstrated on two different tracked robots in simulation and on a real platform. Compared to a tracking system as ground truth, our method predicts the robot position and orientation with an average accuracy of 3.11 cm and 3.91°, outperforming a recent heightmap-based approach. The implementation is made available as an open-source ROS package.

## 参考
- http://arxiv.org/abs/2405.02121v1

## 개요
비구조화 환경에서 이동형 지상 로봇의 자율 내비게이션 및 궤도 제어 문제에 대해, 기존의 점유 격자 또는 주행 가능성 지도 기반 휴리스틱 방법은 관절 위치를 고려하지 않아 능동 궤도 로봇의 동작 능력을 제한합니다. 본 논문은 부호 거리장(Signed Distance Fields)의 서브복셀 표면 표현 능력을 활용한 새로운 반복 기하학적 방법을 제안하며, 온라인 계획 시나리오에서 로봇의 3D 자세를 고정밀도로 예측합니다. 이 방법은 두 가지 서로 다른 궤도 로봇의 시뮬레이션 및 실제 플랫폼 실험에서 최근의 높이 맵 기반 방법보다 우수한 위치 및 방향 정밀도를 달성했습니다.

## 핵심 내용
### 방법 핵심
- 유클리드 부호 거리장(Euclidean Signed Distance Field)의 서브복셀 정밀도 특성을 활용하여, 반복 기하학적 매칭을 통해 로봇 모델을 지형 표면에 "침강"시킵니다.
- 입력은 로봇 관절 각도와 지형 SDF이며, 출력은 예측된 3D 자세(위치+방향)로 온라인 계획을 지원합니다.

### 실험 설정
- **플랫폼**: 두 가지 서로 다른 크기의 궤도 로봇(시뮬레이션+실제 플랫폼).
- **비교 기준**: 높이 맵(heightmap) 기반 최근 방법.
- **실측 시스템**: 모션 캡처 시스템(ground truth tracking system).

### 주요 결과
- **위치 정밀도**: 평균 오차 3.11 cm.
- **자세 정밀도**: 평균 오차 3.91°.
- **성능 비교**: 높이 맵 방법보다 현저히 우수하며, 특히 복잡한 지형에서 두드러집니다.

### 결론 및 오픈소스
- 이 방법은 능동 궤도 로봇의 비구조화 지형에서의 자세 예측을 위한 고정밀도, 저지연 솔루션을 제공합니다.
- 구현은 오픈소스 ROS 패키지로 공개되어 커뮤니티의 재현 및 확장을 용이하게 합니다.
