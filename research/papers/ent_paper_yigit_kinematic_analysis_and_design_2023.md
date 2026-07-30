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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.12499v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## Overview
A novel kinematically redundant (6+3)-DoF parallel robot is presented in this paper. Three identical 3-DoF RU/2-RUS legs are attached to a configurable platform through spherical joints. With the selected leg mechanism, the motors are mounted at the base, reducing the reflected inertia. The robot is intended to be actuated with direct-drive motors in order to perform intuitive physical human-robot interaction. The design of the leg mechanism maximizes the workspace in which the end-effector of the leg can have a 2g acceleration in all directions. All singularities of the leg mechanism are identified under a simplifying assumption. A CAD model of the (6+3)-DoF robot is presented in order to illustrate the preliminary design of the robot.

## 개요
본 논문에서는 새로운 운동학적 중복성을 가진 (6+3)-자유도 병렬 로봇을 제시한다. 세 개의 동일한 3-자유도 RU/2-RUS 다리가 구형 조인트를 통해 구성 가능한 플랫폼에 부착된다. 선택된 다리 메커니즘을 통해 모터는 베이스에 장착되어 반사 관성을 줄인다. 이 로봇은 직관적인 물리적 인간-로봇 상호작용을 수행하기 위해 직접 구동 모터로 작동될 예정이다. 다리 메커니즘의 설계는 다리 엔드 이펙터가 모든 방향에서 2g 가속도를 가질 수 있는 작업 공간을 최대화한다. 단순화된 가정 하에 다리 메커니즘의 모든 특이점이 식별된다. 로봇의 예비 설계를 설명하기 위해 (6+3)-자유도 로봇의 CAD 모델이 제시된다.

## 핵심 내용
본 논문에서는 새로운 운동학적 중복성을 가진 (6+3)-자유도 병렬 로봇을 제시한다. 세 개의 동일한 3-자유도 RU/2-RUS 다리가 구형 조인트를 통해 구성 가능한 플랫폼에 부착된다. 선택된 다리 메커니즘을 통해 모터는 베이스에 장착되어 반사 관성을 줄인다. 이 로봇은 직관적인 물리적 인간-로봇 상호작용을 수행하기 위해 직접 구동 모터로 작동될 예정이다. 다리 메커니즘의 설계는 다리 엔드 이펙터가 모든 방향에서 2g 가속도를 가질 수 있는 작업 공간을 최대화한다. 단순화된 가정 하에 다리 메커니즘의 모든 특이점이 식별된다. 로봇의 예비 설계를 설명하기 위해 (6+3)-자유도 로봇의 CAD 모델이 제시된다.

## 参考
- http://arxiv.org/abs/2304.12499v1
