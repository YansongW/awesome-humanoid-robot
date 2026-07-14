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

