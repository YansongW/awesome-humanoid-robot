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
  zh: 提出一种迭代几何方法，利用欧氏有符号距离场（ESDF）在不平整地形上对带主动翻转器的移动地面机器人进行三维姿态预测，在真实履带机器人上达到平均3.11厘米和3.91度的精度。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.02121v1.
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
Autonomous locomotion for mobile ground robots in unstructured environments such as waypoint navigation or flipper control requires a sufficiently accurate prediction of the robot-terrain interaction. Heuristics like occupancy grids or traversability maps are widely used but limit actions available to robots with active flippers as joint positions are not taken into account. We present a novel iterative geometric method to predict the 3D pose of mobile ground robots with active flippers on uneven ground with high accuracy and online planning capabilities. This is achieved by utilizing the ability of signed distance fields to represent surfaces with sub-voxel accuracy. The effectiveness of the presented approach is demonstrated on two different tracked robots in simulation and on a real platform. Compared to a tracking system as ground truth, our method predicts the robot position and orientation with an average accuracy of 3.11 cm and 3.91°, outperforming a recent heightmap-based approach. The implementation is made available as an open-source ROS package.

## 核心内容
Autonomous locomotion for mobile ground robots in unstructured environments such as waypoint navigation or flipper control requires a sufficiently accurate prediction of the robot-terrain interaction. Heuristics like occupancy grids or traversability maps are widely used but limit actions available to robots with active flippers as joint positions are not taken into account. We present a novel iterative geometric method to predict the 3D pose of mobile ground robots with active flippers on uneven ground with high accuracy and online planning capabilities. This is achieved by utilizing the ability of signed distance fields to represent surfaces with sub-voxel accuracy. The effectiveness of the presented approach is demonstrated on two different tracked robots in simulation and on a real platform. Compared to a tracking system as ground truth, our method predicts the robot position and orientation with an average accuracy of 3.11 cm and 3.91°, outperforming a recent heightmap-based approach. The implementation is made available as an open-source ROS package.

## 参考
- http://arxiv.org/abs/2405.02121v1

## Overview
Autonomous locomotion for mobile ground robots in unstructured environments such as waypoint navigation or flipper control requires a sufficiently accurate prediction of the robot-terrain interaction. Heuristics like occupancy grids or traversability maps are widely used but limit actions available to robots with active flippers as joint positions are not taken into account. We present a novel iterative geometric method to predict the 3D pose of mobile ground robots with active flippers on uneven ground with high accuracy and online planning capabilities. This is achieved by utilizing the ability of signed distance fields to represent surfaces with sub-voxel accuracy. The effectiveness of the presented approach is demonstrated on two different tracked robots in simulation and on a real platform. Compared to a tracking system as ground truth, our method predicts the robot position and orientation with an average accuracy of 3.11 cm and 3.91°, outperforming a recent heightmap-based approach. The implementation is made available as an open-source ROS package.

## Content
Autonomous locomotion for mobile ground robots in unstructured environments such as waypoint navigation or flipper control requires a sufficiently accurate prediction of the robot-terrain interaction. Heuristics like occupancy grids or traversability maps are widely used but limit actions available to robots with active flippers as joint positions are not taken into account. We present a novel iterative geometric method to predict the 3D pose of mobile ground robots with active flippers on uneven ground with high accuracy and online planning capabilities. This is achieved by utilizing the ability of signed distance fields to represent surfaces with sub-voxel accuracy. The effectiveness of the presented approach is demonstrated on two different tracked robots in simulation and on a real platform. Compared to a tracking system as ground truth, our method predicts the robot position and orientation with an average accuracy of 3.11 cm and 3.91°, outperforming a recent heightmap-based approach. The implementation is made available as an open-source ROS package.

## 개요
비정형 환경에서 이동 지상 로봇의 자율 주행(예: 경유지 항법 또는 플리퍼 제어)은 로봇-지형 상호작용에 대한 충분히 정확한 예측을 필요로 합니다. 점유 격자(occupancy grids)나 주행 가능 지도(traversability maps)와 같은 휴리스틱이 널리 사용되지만, 관절 위치를 고려하지 않아 능동 플리퍼를 가진 로봇의 동작을 제한합니다. 본 논문에서는 능동 플리퍼를 가진 이동 지상 로봇의 3D 자세를 불균일 지형에서 높은 정확도와 온라인 계획 능력으로 예측하는 새로운 반복 기하학적 방법을 제시합니다. 이는 부호 거리 필드(signed distance fields)가 서브복셀 정밀도로 표면을 표현하는 능력을 활용하여 달성됩니다. 제안된 접근법의 효과는 시뮬레이션과 실제 플랫폼에서 두 가지 다른 궤도 로봇을 통해 입증되었습니다. 기준 실측값으로 추적 시스템과 비교했을 때, 우리 방법은 로봇 위치와 방향을 평균 3.11cm 및 3.91°의 정확도로 예측하여 최근 높이맵 기반 접근법보다 우수한 성능을 보였습니다. 구현은 오픈소스 ROS 패키지로 제공됩니다.

## 핵심 내용
비정형 환경에서 이동 지상 로봇의 자율 주행(예: 경유지 항법 또는 플리퍼 제어)은 로봇-지형 상호작용에 대한 충분히 정확한 예측을 필요로 합니다. 점유 격자(occupancy grids)나 주행 가능 지도(traversability maps)와 같은 휴리스틱이 널리 사용되지만, 관절 위치를 고려하지 않아 능동 플리퍼를 가진 로봇의 동작을 제한합니다. 본 논문에서는 능동 플리퍼를 가진 이동 지상 로봇의 3D 자세를 불균일 지형에서 높은 정확도와 온라인 계획 능력으로 예측하는 새로운 반복 기하학적 방법을 제시합니다. 이는 부호 거리 필드(signed distance fields)가 서브복셀 정밀도로 표면을 표현하는 능력을 활용하여 달성됩니다. 제안된 접근법의 효과는 시뮬레이션과 실제 플랫폼에서 두 가지 다른 궤도 로봇을 통해 입증되었습니다. 기준 실측값으로 추적 시스템과 비교했을 때, 우리 방법은 로봇 위치와 방향을 평균 3.11cm 및 3.91°의 정확도로 예측하여 최근 높이맵 기반 접근법보다 우수한 성능을 보였습니다. 구현은 오픈소스 ROS 패키지로 제공됩니다.
