---
$id: ent_paper_martinez_rozas_skyeye_team_at_mbzirc_2020_a_t_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Skyeye Team at MBZIRC 2020: A team of aerial and ground robots for GPS-denied
    autonomous fire extinguishing in an urban building scenario'
  zh: Skyeye 团队参加 MBZIRC 2020：用于城市建筑场景下无 GPS 自主灭火的空地机器人团队
  ko: 'Skyeye 팀 MBZIRC 2020: GPS 차단 도시 건축물 환경에서 자율 소화를 위한 공중 및 지상 로봇 팀'
summary:
  en: Presents a heterogeneous multi-robot system of up to three UAVs and one UGV
    that autonomously detects, localizes, and extinguishes fires in a simulated high-rise
    building at MBZIRC 2020 using LIDAR-based GPS-denied localization, modified Lazy
    Theta* planners, thermal perception, and Behavior Tree mission execution.
  zh: 介绍了一种由最多三架无人机和一辆无人地面车组成的异构多机器人系统，该系统在 MBZIRC 2020 比赛中利用基于激光雷达的无 GPS 定位、改进的 Lazy
    Theta* 规划器、热成像感知和行为树任务执行，自主检测、定位并扑灭模拟高层建筑火灾。
  ko: 최대 3대의 UAV와 1대의 UGV로 구성된 이종 다중 로봇 시스템을 제시하며, LIDAR 기반 GPS 차단 위치 추정, 수정된 Lazy
    Theta* 경로 계획기, 열 감지 및 비헤이비어 트리 임무 수행을 통해 MBZIRC 2020에서 모의 고층 건축물 화재를 자율적으로 탐지·위치
    추정·진압한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- gps_denied_localization
- multi_robot_coordination
- behavior_trees
- lazy_theta_star
- monte_carlo_localization
- uav_ugv_team
- firefighting
- autonomous_navigation
- lidar_mapping
- thermal_perception
- mbzirc_2020
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Skyeye Team at MBZIRC 2020: A team of aerial and ground robots for GPS-denied
    autonomous fire extinguishing in an urban building scenario'
  url: https://arxiv.org/abs/2104.01834
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper presents the Skyeye team's fully autonomous multi-robot system designed for MBZIRC 2020 Challenge 3, which required a team of up to three unmanned aerial vehicles (UAVs) and one unmanned ground vehicle (UGV) to detect, localize, and extinguish simulated fires in and around a 15-meter high-rise building. The heterogeneous system integrates aerial platforms (DJI Matrice 210 V2 and DJI Matrice 600 Pro) with the SIAR 6-wheeled UGV, each carrying onboard sensing, computation, and actuation for navigation and firefighting. The work details the hardware adaptations, software architecture, and algorithmic components that allowed the team to operate fully autonomously and score in all trials, finishing 7th of 20 teams in Challenge 3 and 5th of 17 teams in the Grand Challenge entry.

The core algorithmic contributions span four areas: a 3D LIDAR-based mapping and localization module that works in GPS-denied scenarios; a global planner and fast local re-planning system for safe robot navigation; infrared-based perception and actuation control for fire extinguishing; and a mission executive and coordination module based on Behavior Trees. The localization approach decouples mapping from localization, using LIDAR odometry (A-LOAM/LOAM) for mapping and a multi-sensor 3D Monte Carlo localization filter integrating LIDAR, GPS, altimeter, and IMU yaw for real-time pose estimation. Navigation relies on modified Lazy Theta* planners extended with obstacle-distance safety margins for both 2D UGV and 3D UAV motion planning.

## Key Contributions

- GPS-denied multi-sensor 3D Monte Carlo localization that fuses LIDAR point-cloud matching with GPS, altimeter, and IMU yaw updates to operate seamlessly across GPS-available and GPS-denied conditions.
- Modified Lazy Theta* path planners that incorporate obstacle-distance cost terms and line-of-sight constraints for safe and repeatable 2D UGV and 3D UAV navigation in cluttered environments.
- An onboard Behavior Tree mission executive that composes atomic actionlib tasks (TakeOff, Land, GoToGoal, FireDetection3D, FireExtinguish) into modular, reactive per-robot missions and enables rapid reconfiguration during competition.
- An integrated heterogeneous multi-robot firefighting system combining UAVs, UGV, thermal perception, water ejection, and electromagnetic blanket deployment, validated at MBZIRC 2020 with fully autonomous scoring in all trials.

## Relevance to Humanoid Robotics

Although the paper targets UAV/UGV firefighting, the GPS-denied localization, robust autonomous navigation, Behavior Tree mission execution, and multi-robot coordination it develops are foundational capabilities that transfer directly to humanoid robots deployed in hazardous, unstructured, GPS-limited industrial and disaster-response settings. Humanoids operating inside buildings, near infrastructure, or in smoke-obstructed environments will need the same tightly-coupled mapping, localization, planning, and reactive task execution stack demonstrated here. The modular Behavior Tree executive and the safety-aware planner formulation are particularly reusable for legged platforms that must switch between locomotion, manipulation, and interaction tasks in dynamic environments.
