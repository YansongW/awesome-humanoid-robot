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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.02121v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
비정형 환경에서 이동 지상 로봇의 자율 주행(예: 경유지 항법 또는 플리퍼 제어)은 로봇-지형 상호작용에 대한 충분히 정확한 예측을 필요로 합니다. 점유 격자(occupancy grids)나 주행 가능 지도(traversability maps)와 같은 휴리스틱이 널리 사용되지만, 관절 위치를 고려하지 않아 능동 플리퍼를 가진 로봇의 동작을 제한합니다. 본 논문에서는 능동 플리퍼를 가진 이동 지상 로봇의 3D 자세를 불균일 지형에서 높은 정확도와 온라인 계획 능력으로 예측하는 새로운 반복 기하학적 방법을 제시합니다. 이는 부호 거리 필드(signed distance fields)가 서브복셀 정밀도로 표면을 표현하는 능력을 활용하여 달성됩니다. 제안된 접근법의 효과는 시뮬레이션과 실제 플랫폼에서 두 가지 다른 궤도 로봇을 통해 입증되었습니다. 기준 실측값으로 추적 시스템과 비교했을 때, 우리 방법은 로봇 위치와 방향을 평균 3.11cm 및 3.91°의 정확도로 예측하여 최근 높이맵 기반 접근법보다 우수한 성능을 보였습니다. 구현은 오픈소스 ROS 패키지로 제공됩니다.

## 핵심 내용
비정형 환경에서 이동 지상 로봇의 자율 주행(예: 경유지 항법 또는 플리퍼 제어)은 로봇-지형 상호작용에 대한 충분히 정확한 예측을 필요로 합니다. 점유 격자(occupancy grids)나 주행 가능 지도(traversability maps)와 같은 휴리스틱이 널리 사용되지만, 관절 위치를 고려하지 않아 능동 플리퍼를 가진 로봇의 동작을 제한합니다. 본 논문에서는 능동 플리퍼를 가진 이동 지상 로봇의 3D 자세를 불균일 지형에서 높은 정확도와 온라인 계획 능력으로 예측하는 새로운 반복 기하학적 방법을 제시합니다. 이는 부호 거리 필드(signed distance fields)가 서브복셀 정밀도로 표면을 표현하는 능력을 활용하여 달성됩니다. 제안된 접근법의 효과는 시뮬레이션과 실제 플랫폼에서 두 가지 다른 궤도 로봇을 통해 입증되었습니다. 기준 실측값으로 추적 시스템과 비교했을 때, 우리 방법은 로봇 위치와 방향을 평균 3.11cm 및 3.91°의 정확도로 예측하여 최근 높이맵 기반 접근법보다 우수한 성능을 보였습니다. 구현은 오픈소스 ROS 패키지로 제공됩니다.

## 参考
- http://arxiv.org/abs/2405.02121v1
