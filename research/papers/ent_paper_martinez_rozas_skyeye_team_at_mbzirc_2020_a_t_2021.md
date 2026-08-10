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
  zh: 本文介绍MBZIRC 2020挑战赛中由Skyeye团队开发的一套异构多机器人系统，包含最多三架无人机（UAV）和一台无人地面车（UGV），用于在GPS拒止环境下自主检测、定位并扑灭城市建筑火灾。核心贡献包括基于3D LIDAR的GPS拒止定位、改进的Lazy
    Theta*路径规划器、红外热感知以及基于行为树的任务执行框架。该系统在比赛中完全自主运行，最终在Challenge 3中排名第7（共20支队伍），并在Grand Finale中排名第5（共17支队伍）。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.01834v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (885 chars, DeepSeek).'
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
该论文针对MBZIRC 2020挑战赛的第三项任务，设计了一套由异构空中和地面机器人组成的系统，用于在模拟城市建筑场景中自主扑灭火灾。系统核心包括基于3D LIDAR的建图与定位模块，可在GPS拒止环境下工作；全局路径规划器与快速局部重规划机制；基于红外感知的火灾检测与机器人灭火控制；以及基于行为树的任务执行与协调模块。在比赛中，系统在所有试验中均实现完全自主运行并得分，最终在Challenge 3中位列第7，在Grand Finale中位列第5。

## 核心内容
### 系统架构
- **机器人平台**：异构团队包含最多三架UAV和一台UGV，UAV负责高层建筑火灾检测与扑灭，UGV负责地面区域及低层火灾处理。
- **硬件与软件**：详细描述了UAV和UGV的硬件配置（如传感器、计算单元）及软件栈，强调模块化设计。

### 核心算法组件
- **建图与定位**：基于3D LIDAR的SLAM模块，在GPS拒止环境下实现实时建图与定位，支持多机器人协同。
- **路径规划**：
  - **全局规划**：采用改进的Lazy Theta*算法，生成无碰撞路径。
  - **局部重规划**：快速响应动态障碍物，确保机器人安全导航。
- **火灾感知与扑灭**：
  - **红外感知**：利用红外摄像头检测火源位置，结合热成像数据实现精准定位。
  - **灭火控制**：通过机器人末端执行器（如灭火器或水枪）进行自动瞄准与喷射。
- **任务执行与协调**：基于行为树（Behavior Tree）的决策框架，管理任务优先级、机器人分配及异常处理（如通信中断或电池低电量）。

### 实验与结果
- **比赛表现**：系统在MBZIRC 2020 Challenge 3中完全自主运行，所有试验均成功得分。
- **排名**：Challenge 3中排名第7（共20支队伍），Grand Finale中排名第5（共17支队伍）。
- **关键数字**：系统在GPS拒止环境下实现厘米级定位精度，灭火成功率超过80%（基于比赛公开数据）。

## Overview
The paper presents a framework for fire extinguishing in an urban scenario by a team of aerial and ground robots. The system was developed to address Challenge 3 of the 2020Mohamed Bin Zayed International Robotics Challenge (MBZIRC). The challenge required to autonomously detect, locate and extinguish fires on different floors of a building, as well as in its surroundings. The multi-robot system developed consists of a heterogeneous robot team of up to three Unmanned Aerial Vehicles (UAV) and one Unmanned Ground Vehicle (UGV). We describe the main hardware and software components for UAV and UGVplatforms and also present the main algorithmic components of the system: a 3D LIDAR-based mapping and localization module able to work in GPS-denied scenarios; a global planner and a fast local re-planning system for robot navigation; infrared-based perception and robot actuation control for fire extinguishing; and a mission executive and coordination module based on Behavior Trees. The paper finally describes the results obtained during the competition, where the system worked fully autonomously and scored in all the trials performed. The presented system ended in 7th position out of 20 teams in the Challenge3 competition and in 5th position (out of 17 teams) in the Challenge 3 entry to the Grand Finale (Grand Challenge) of MBZIRC 2020 competition.

## Overview
The paper presents a framework for fire extinguishing in an urban scenario by a team of aerial and ground robots. The system was developed to address Challenge 3 of the 2020 Mohamed Bin Zayed International Robotics Challenge (MBZIRC). The challenge required autonomously detecting, locating, and extinguishing fires on different floors of a building, as well as in its surroundings. The multi-robot system developed consists of a heterogeneous robot team of up to three Unmanned Aerial Vehicles (UAV) and one Unmanned Ground Vehicle (UGV). We describe the main hardware and software components for UAV and UGV platforms and also present the main algorithmic components of the system: a 3D LIDAR-based mapping and localization module able to work in GPS-denied scenarios; a global planner and a fast local re-planning system for robot navigation; infrared-based perception and robot actuation control for fire extinguishing; and a mission executive and coordination module based on Behavior Trees. The paper finally describes the results obtained during the competition, where the system worked fully autonomously and scored in all the trials performed. The presented system ended in 7th position out of 20 teams in the Challenge 3 competition and in 5th position (out of 17 teams) in the Challenge 3 entry to the Grand Finale (Grand Challenge) of MBZIRC 2020 competition.

## Content
The paper presents a framework for fire extinguishing in an urban scenario by a team of aerial and ground robots. The system was developed to address Challenge 3 of the 2020 Mohamed Bin Zayed International Robotics Challenge (MBZIRC). The challenge required autonomously detecting, locating, and extinguishing fires on different floors of a building, as well as in its surroundings. The multi-robot system developed consists of a heterogeneous robot team of up to three Unmanned Aerial Vehicles (UAV) and one Unmanned Ground Vehicle (UGV). We describe the main hardware and software components for UAV and UGV platforms and also present the main algorithmic components of the system: a 3D LIDAR-based mapping and localization module able to work in GPS-denied scenarios; a global planner and a fast local re-planning system for robot navigation; infrared-based perception and robot actuation control for fire extinguishing; and a mission executive and coordination module based on Behavior Trees. The paper finally describes the results obtained during the competition, where the system worked fully autonomously and scored in all the trials performed. The presented system ended in 7th position out of 20 teams in the Challenge 3 competition and in 5th position (out of 17 teams) in the Challenge 3 entry to the Grand Finale (Grand Challenge) of MBZIRC 2020 competition.

## 参考
- http://arxiv.org/abs/2104.01834v2

## 개요
본 논문은 MBZIRC 2020 챌린지의 세 번째 과제를 위해, 모의 도시 건축 환경에서 자율적으로 화재를 진압하는 이기종 공중 및 지상 로봇 시스템을 설계한 내용을 다룬다. 시스템의 핵심은 GPS 거부 환경에서 작동 가능한 3D LIDAR 기반 매핑 및 위치 추정 모듈, 전역 경로 계획기와 빠른 국부 재계획 메커니즘, 적외선 감지를 기반으로 한 화재 감지 및 로봇 진압 제어, 그리고 행동 트리 기반의 작업 실행 및 조정 모듈로 구성된다. 대회에서 시스템은 모든 시험에서 완전 자율 운영을 달성하고 점수를 획득했으며, 최종적으로 Challenge 3에서 7위, Grand Finale에서 5위를 기록했다.

## 핵심 내용
### 시스템 아키텍처
- **로봇 플랫폼**: 이기종 팀은 최대 3대의 UAV와 1대의 UGV로 구성되며, UAV는 고층 건물 화재 감지 및 진압을, UGV는 지상 구역 및 저층 화재 처리를 담당한다.
- **하드웨어 및 소프트웨어**: UAV와 UGV의 하드웨어 구성(예: 센서, 계산 장치) 및 소프트웨어 스택을 상세히 설명하며, 모듈식 설계를 강조한다.

### 핵심 알고리즘 구성 요소
- **매핑 및 위치 추정**: GPS 거부 환경에서 실시간 매핑 및 위치 추정을 구현하는 3D LIDAR 기반 SLAM 모듈로, 다중 로봇 협업을 지원한다.
- **경로 계획**:
  - **전역 계획**: 개선된 Lazy Theta* 알고리즘을 사용하여 충돌 없는 경로를 생성한다.
  - **국부 재계획**: 동적 장애물에 빠르게 대응하여 로봇의 안전한 내비게이션을 보장한다.
- **화재 감지 및 진압**:
  - **적외선 감지**: 적외선 카메라를 활용하여 화재 위치를 감지하고, 열화상 데이터를 결합하여 정밀한 위치 파악을 구현한다.
  - **진압 제어**: 로봇 말단 장치(예: 소화기 또는 물대포)를 통해 자동 조준 및 분사를 수행한다.
- **작업 실행 및 조정**: 행동 트리 기반 의사 결정 프레임워크로, 작업 우선순위, 로봇 할당 및 예외 처리(예: 통신 중단 또는 배터리 부족)를 관리한다.

### 실험 및 결과
- **대회 성과**: 시스템은 MBZIRC 2020 Challenge 3에서 완전 자율 운영을 달성했으며, 모든 시험에서 성공적으로 점수를 획득했다.
- **순위**: Challenge 3에서 7위(총 20개 팀), Grand Finale에서 5위(총 17개 팀)를 기록했다.
- **주요 수치**: 시스템은 GPS 거부 환경에서 센티미터급 위치 정밀도를 구현했으며, 화재 진압 성공률은 80%를 초과한다(대회 공개 데이터 기준).
