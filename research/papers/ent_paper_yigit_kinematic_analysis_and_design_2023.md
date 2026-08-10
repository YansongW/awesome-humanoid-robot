---
$id: ent_paper_yigit_kinematic_analysis_and_design_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Kinematic Analysis and Design of a Novel (6+3)-DoF Parallel Robot with Fixed Actuators
  zh: 一种具有固定执行器的新型（6+3）自由度并联机器人的运动学分析与设计
  ko: 고정 액츄에이터를 갖춘 신형 (6+3)-DoF 병렬 로봇의 운동학적 분석 및 설계
summary:
  en: Presents a kinematically redundant (6+3)-DoF parallel robot built from three identical base-mounted 3-DoF RU/2-RUS legs,
    deriving inverse kinematics and Jacobian matrices via screw theory, classifying singularities, and optimizing leg geometry
    for a 2g acceleration workspace aimed at backdrivable physical human-robot interaction.
  zh: 本文提出一种新型运动冗余 (6+3) 自由度并联机器人，由三个相同的基座安装式 3-DoF RU/2-RUS 支腿构成。通过旋量理论推导逆运动学与雅可比矩阵，分类奇异性，并优化支腿几何结构以实现面向可反向驱动物理人机交互的 2g 加速度工作空间。
  ko: 세 개의 동일한 기座 설치형 3-DoF RU/2-RUS 다리로 구성된 운동학적 중복 (6+3)-DoF 병렬 로봇을 제안하고, 스크루 이론을 통해 역운동학 및 야코비 행렬을 도출하며, 특이점을 분류하고, 2g
    가속도 작업 공간을 위해 다리 기하학을 최적화하여 역구동 가능한 물리적 인간-로봇 상호작용을 목표로 합니다.
domains:
- 02_components
- 06_design_engineering
- 03_manufacturing_processes
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- parallel_robot
- fixed_actuator
- kinematic_redundancy
- ru_2rus_leg
- screw_theory
- jacobian
- singularity_analysis
- direct_drive
- backdrivability
- physical_human_robot_interaction
- low_inertia
- workspace_optimization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.12499v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (594 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Kinematic Analysis and Design of a Novel (6+3)-DoF Parallel Robot with Fixed Actuators
  url: https://arxiv.org/abs/2304.12499
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该机器人采用三个相同的 3-DoF RU/2-RUS 支腿，通过球铰连接至可配置平台。支腿机构将电机安装于基座，从而降低反射惯性，并计划使用直驱电机以实现直观的物理人机交互。设计重点在于最大化支腿末端执行器在所有方向上达到 2g 加速度的工作空间。在简化假设下识别了支腿机构的所有奇异性，并通过 CAD 模型展示了机器人的初步设计。

## 核心内容
### 机器人构型与运动学
- 提出一种运动冗余 (6+3) 自由度并联机器人，由三个相同的 3-DoF RU/2-RUS 支腿构成。
- 支腿通过球铰连接至可配置平台，电机全部安装于基座，以降低反射惯性。
- 采用旋量理论推导逆运动学与雅可比矩阵，为后续奇异性分析奠定基础。

### 奇异性分析
- 在简化假设下，识别了支腿机构的所有奇异性类型，包括运动学奇异与约束奇异。
- 奇异性分类有助于避免机器人在工作空间内出现失控或刚度丧失的情况。

### 工作空间优化
- 设计目标为最大化支腿末端执行器在所有方向上达到 2g 加速度的工作空间。
- 通过优化支腿几何结构（如连杆长度与关节布局），确保机器人适用于可反向驱动的物理人机交互场景。

### 初步设计验证
- 通过 CAD 模型展示了 (6+3) 自由度机器人的初步设计，包括基座、支腿与可配置平台的装配关系。
- 该设计为后续样机制造与实验验证提供了基础。

## 参考
- http://arxiv.org/abs/2304.12499v1

## Overview
This robot employs three identical 3-DoF RU/2-RUS legs, connected via spherical joints to a configurable platform. The leg mechanism mounts motors on the base to reduce reflected inertia, and direct-drive motors are planned to enable intuitive physical human-robot interaction. The design focuses on maximizing the workspace where the leg end-effector achieves 2g acceleration in all directions. Under simplified assumptions, all singularities of the leg mechanism are identified, and a preliminary design of the robot is presented through a CAD model.

## Content
### Robot Configuration and Kinematics
- Proposes a kinematically redundant (6+3) degree-of-freedom parallel robot, composed of three identical 3-DoF RU/2-RUS legs.
- The legs connect to a configurable platform via spherical joints, with all motors mounted on the base to reduce reflected inertia.
- Uses screw theory to derive inverse kinematics and Jacobian matrices, laying the foundation for subsequent singularity analysis.

### Singularity Analysis
- Under simplified assumptions, all types of singularities in the leg mechanism are identified, including kinematic and constraint singularities.
- The classification of singularities helps avoid loss of control or stiffness within the robot's workspace.

### Workspace Optimization
- The design goal is to maximize the workspace where the leg end-effector achieves 2g acceleration in all directions.
- By optimizing the leg geometry (such as link lengths and joint layout), the robot is ensured to be suitable for backdrivable physical human-robot interaction scenarios.

### Preliminary Design Validation
- A preliminary design of the (6+3) degree-of-freedom robot is presented through a CAD model, including the assembly relationships of the base, legs, and configurable platform.
- This design provides a foundation for subsequent prototype manufacturing and experimental validation.

## 개요
이 로봇은 세 개의 동일한 3-DoF RU/2-RUS 다리로 구성되며, 볼 조인트를 통해 구성 가능한 플랫폼에 연결됩니다. 다리 메커니즘은 모터를 베이스에 장착하여 반사 관성을 낮추며, 직관적인 물리적 인간-로봇 상호작용을 위해 직접 구동 모터를 사용할 계획입니다. 설계의 핵심은 다리 엔드 이펙터가 모든 방향에서 2g 가속도를 달성할 수 있는 작업 공간을 최대화하는 데 있습니다. 단순화된 가정 하에 다리 메커니즘의 모든 특이점을 식별했으며, CAD 모델을 통해 로봇의 초기 설계를 제시했습니다.

## 핵심 내용
### 로봇 구성 및 운동학
- 운동학적 중복성(6+3) 자유도를 가진 병렬 로봇을 제안하며, 세 개의 동일한 3-DoF RU/2-RUS 다리로 구성됩니다.
- 다리는 볼 조인트를 통해 구성 가능한 플랫폼에 연결되며, 모든 모터는 베이스에 장착되어 반사 관성을 낮춥니다.
- 스크류 이론을 사용하여 역운동학과 자코비안 행렬을 유도하며, 이는 이후 특이점 분석의 기초를 제공합니다.

### 특이점 분석
- 단순화된 가정 하에 다리 메커니즘의 모든 특이점 유형을 식별했으며, 운동학적 특이점과 구속 특이점을 포함합니다.
- 특이점 분류는 로봇이 작업 공간 내에서 제어 불능이나 강성 손실을 겪지 않도록 하는 데 도움이 됩니다.

### 작업 공간 최적화
- 설계 목표는 다리 엔드 이펙터가 모든 방향에서 2g 가속도를 달성할 수 있는 작업 공간을 최대화하는 것입니다.
- 다리 기하학(예: 링크 길이와 관절 배치)을 최적화하여 로봇이 역구동 가능한 물리적 인간-로봇 상호작용 시나리오에 적합하도록 보장합니다.

### 초기 설계 검증
- CAD 모델을 통해 (6+3) 자유도 로봇의 초기 설계를 제시하며, 베이스, 다리 및 구성 가능한 플랫폼의 조립 관계를 포함합니다.
- 이 설계는 이후 프로토타입 제작 및 실험 검증의 기초를 제공합니다.
