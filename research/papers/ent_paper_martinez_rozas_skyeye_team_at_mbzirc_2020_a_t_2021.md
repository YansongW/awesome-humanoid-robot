---
$id: ent_paper_martinez_rozas_skyeye_team_at_mbzirc_2020_a_t_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Skyeye Team at MBZIRC 2020: A team of aerial and ground robots for GPS-denied autonomous fire extinguishing in an urban
    building scenario'
  zh: Skyeye 团队参加 MBZIRC 2020：用于城市建筑场景下无 GPS 自主灭火的空地机器人团队
  ko: 'Skyeye 팀 MBZIRC 2020: GPS 차단 도시 건축물 환경에서 자율 소화를 위한 공중 및 지상 로봇 팀'
summary:
  en: Presents a heterogeneous multi-robot system of up to three UAVs and one UGV that autonomously detects, localizes, and
    extinguishes fires in a simulated high-rise building at MBZIRC 2020 using LIDAR-based GPS-denied localization, modified
    Lazy Theta* planners, thermal perception, and Behavior Tree mission execution.
  zh: 介绍了一种由最多三架无人机和一辆无人地面车组成的异构多机器人系统，该系统在 MBZIRC 2020 比赛中利用基于激光雷达的无 GPS 定位、改进的 Lazy Theta* 规划器、热成像感知和行为树任务执行，自主检测、定位并扑灭模拟高层建筑火灾。
  ko: 최대 3대의 UAV와 1대의 UGV로 구성된 이종 다중 로봇 시스템을 제시하며, LIDAR 기반 GPS 차단 위치 추정, 수정된 Lazy Theta* 경로 계획기, 열 감지 및 비헤이비어 트리 임무 수행을 통해
    MBZIRC 2020에서 모의 고층 건축물 화재를 자율적으로 탐지·위치 추정·진압한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.01834v2.
sources:
- id: src_001
  type: paper
  title: 'Skyeye Team at MBZIRC 2020: A team of aerial and ground robots for GPS-denied autonomous fire extinguishing in an
    urban building scenario'
  url: https://arxiv.org/abs/2104.01834
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
The paper presents a framework for fire extinguishing in an urban scenario by a team of aerial and ground robots. The system was developed to address Challenge 3 of the 2020Mohamed Bin Zayed International Robotics Challenge (MBZIRC). The challenge required to autonomously detect, locate and extinguish fires on different floors of a building, as well as in its surroundings. The multi-robot system developed consists of a heterogeneous robot team of up to three Unmanned Aerial Vehicles (UAV) and one Unmanned Ground Vehicle (UGV). We describe the main hardware and software components for UAV and UGVplatforms and also present the main algorithmic components of the system: a 3D LIDAR-based mapping and localization module able to work in GPS-denied scenarios; a global planner and a fast local re-planning system for robot navigation; infrared-based perception and robot actuation control for fire extinguishing; and a mission executive and coordination module based on Behavior Trees. The paper finally describes the results obtained during the competition, where the system worked fully autonomously and scored in all the trials performed. The presented system ended in 7th position out of 20 teams in the Challenge3 competition and in 5th position (out of 17 teams) in the Challenge 3 entry to the Grand Finale (Grand Challenge) of MBZIRC 2020 competition.

## 核心内容
The paper presents a framework for fire extinguishing in an urban scenario by a team of aerial and ground robots. The system was developed to address Challenge 3 of the 2020Mohamed Bin Zayed International Robotics Challenge (MBZIRC). The challenge required to autonomously detect, locate and extinguish fires on different floors of a building, as well as in its surroundings. The multi-robot system developed consists of a heterogeneous robot team of up to three Unmanned Aerial Vehicles (UAV) and one Unmanned Ground Vehicle (UGV). We describe the main hardware and software components for UAV and UGVplatforms and also present the main algorithmic components of the system: a 3D LIDAR-based mapping and localization module able to work in GPS-denied scenarios; a global planner and a fast local re-planning system for robot navigation; infrared-based perception and robot actuation control for fire extinguishing; and a mission executive and coordination module based on Behavior Trees. The paper finally describes the results obtained during the competition, where the system worked fully autonomously and scored in all the trials performed. The presented system ended in 7th position out of 20 teams in the Challenge3 competition and in 5th position (out of 17 teams) in the Challenge 3 entry to the Grand Finale (Grand Challenge) of MBZIRC 2020 competition.

## 参考
- http://arxiv.org/abs/2104.01834v2

## Overview
The paper presents a framework for fire extinguishing in an urban scenario by a team of aerial and ground robots. The system was developed to address Challenge 3 of the 2020 Mohamed Bin Zayed International Robotics Challenge (MBZIRC). The challenge required autonomously detecting, locating, and extinguishing fires on different floors of a building, as well as in its surroundings. The multi-robot system developed consists of a heterogeneous robot team of up to three Unmanned Aerial Vehicles (UAV) and one Unmanned Ground Vehicle (UGV). We describe the main hardware and software components for UAV and UGV platforms and also present the main algorithmic components of the system: a 3D LIDAR-based mapping and localization module able to work in GPS-denied scenarios; a global planner and a fast local re-planning system for robot navigation; infrared-based perception and robot actuation control for fire extinguishing; and a mission executive and coordination module based on Behavior Trees. The paper finally describes the results obtained during the competition, where the system worked fully autonomously and scored in all the trials performed. The presented system ended in 7th position out of 20 teams in the Challenge 3 competition and in 5th position (out of 17 teams) in the Challenge 3 entry to the Grand Finale (Grand Challenge) of MBZIRC 2020 competition.

## Content
The paper presents a framework for fire extinguishing in an urban scenario by a team of aerial and ground robots. The system was developed to address Challenge 3 of the 2020 Mohamed Bin Zayed International Robotics Challenge (MBZIRC). The challenge required autonomously detecting, locating, and extinguishing fires on different floors of a building, as well as in its surroundings. The multi-robot system developed consists of a heterogeneous robot team of up to three Unmanned Aerial Vehicles (UAV) and one Unmanned Ground Vehicle (UGV). We describe the main hardware and software components for UAV and UGV platforms and also present the main algorithmic components of the system: a 3D LIDAR-based mapping and localization module able to work in GPS-denied scenarios; a global planner and a fast local re-planning system for robot navigation; infrared-based perception and robot actuation control for fire extinguishing; and a mission executive and coordination module based on Behavior Trees. The paper finally describes the results obtained during the competition, where the system worked fully autonomously and scored in all the trials performed. The presented system ended in 7th position out of 20 teams in the Challenge 3 competition and in 5th position (out of 17 teams) in the Challenge 3 entry to the Grand Finale (Grand Challenge) of MBZIRC 2020 competition.

## 개요
본 논문은 항공 및 지상 로봇 팀이 도시 시나리오에서 화재를 진압하기 위한 프레임워크를 제시합니다. 이 시스템은 2020년 Mohamed Bin Zayed 국제 로봇 공학 챌린지(MBZIRC)의 챌린지 3을 해결하기 위해 개발되었습니다. 해당 챌린지는 건물의 여러 층과 주변에서 화재를 자율적으로 감지, 위치 파악 및 진압하는 것을 요구했습니다. 개발된 다중 로봇 시스템은 최대 3대의 무인 항공기(UAV)와 1대의 무인 지상 차량(UGV)으로 구성된 이기종 로봇 팀으로 이루어져 있습니다. 우리는 UAV 및 UGV 플랫폼의 주요 하드웨어 및 소프트웨어 구성 요소를 설명하고, 시스템의 주요 알고리즘 구성 요소도 제시합니다: GPS가 차단된 시나리오에서 작동 가능한 3D LIDAR 기반 매핑 및 위치 추정 모듈; 로봇 내비게이션을 위한 글로벌 플래너 및 빠른 로컬 재계획 시스템; 화재 진압을 위한 적외선 기반 인식 및 로봇 작동 제어; 그리고 행동 트리(Behavior Trees) 기반의 임무 실행 및 조정 모듈입니다. 마지막으로, 본 논문은 시스템이 완전히 자율적으로 작동하고 모든 수행된 시험에서 점수를 획득한 대회 중 얻은 결과를 설명합니다. 제시된 시스템은 챌린지 3 대회에서 20개 팀 중 7위를 차지했으며, MBZIRC 2020 대회의 그랜드 피날레(그랜드 챌린지) 진출을 위한 챌린지 3에서는 17개 팀 중 5위를 기록했습니다.

## 핵심 내용
본 논문은 항공 및 지상 로봇 팀이 도시 시나리오에서 화재를 진압하기 위한 프레임워크를 제시합니다. 이 시스템은 2020년 Mohamed Bin Zayed 국제 로봇 공학 챌린지(MBZIRC)의 챌린지 3을 해결하기 위해 개발되었습니다. 해당 챌린지는 건물의 여러 층과 주변에서 화재를 자율적으로 감지, 위치 파악 및 진압하는 것을 요구했습니다. 개발된 다중 로봇 시스템은 최대 3대의 무인 항공기(UAV)와 1대의 무인 지상 차량(UGV)으로 구성된 이기종 로봇 팀으로 이루어져 있습니다. 우리는 UAV 및 UGV 플랫폼의 주요 하드웨어 및 소프트웨어 구성 요소를 설명하고, 시스템의 주요 알고리즘 구성 요소도 제시합니다: GPS가 차단된 시나리오에서 작동 가능한 3D LIDAR 기반 매핑 및 위치 추정 모듈; 로봇 내비게이션을 위한 글로벌 플래너 및 빠른 로컬 재계획 시스템; 화재 진압을 위한 적외선 기반 인식 및 로봇 작동 제어; 그리고 행동 트리(Behavior Trees) 기반의 임무 실행 및 조정 모듈입니다. 마지막으로, 본 논문은 시스템이 완전히 자율적으로 작동하고 모든 수행된 시험에서 점수를 획득한 대회 중 얻은 결과를 설명합니다. 제시된 시스템은 챌린지 3 대회에서 20개 팀 중 7위를 차지했으며, MBZIRC 2020 대회의 그랜드 피날레(그랜드 챌린지) 진출을 위한 챌린지 3에서는 17개 팀 중 5위를 기록했습니다.
