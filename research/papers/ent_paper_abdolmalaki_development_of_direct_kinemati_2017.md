---
$id: ent_paper_abdolmalaki_development_of_direct_kinemati_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Development of Direct Kinematics and Workspace Representation for Smokie Robot
    Manipulator & the Barrett WAM
  zh: Smokie机器人机械臂与Barrett WAM的直接运动学与工作空间表示研究
  ko: Smokie 로봇 매니퓰레이터 및 Barrett WAM의 직접운동학과 작업공간 표현 개발
summary:
  en: This paper derives Denavit-Hartenberg parameters and direct-kinematics transformation
    matrices for the 6-DOF Smokie Robot and a 6-DOF configuration of the Barrett WAM,
    then uses a MATLAB Monte Carlo sampler to visualize their 3-D workspaces from
    multiple views.
  zh: 本文推导了6自由度Smokie机器人和6自由度Barrett WAM构型的Denavit-Hartenberg参数与直接运动学变换矩阵，并使用MATLAB蒙特卡洛采样器从多个视角可视化其三维工作空间。
  ko: 본 논문은 6자유도 Smokie 로봇과 6자유도 Barrett WAM 구성의 Denavit-Hartenberg 매개변수 및 직접운동학 변환
    행렬을 도출한 후, MATLAB 몬테카를로 샘플러를 사용하여 여러 시점에서 3차원 작업공간을 시각화한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- direct_kinematics
- denavit_hartenberg_parameters
- workspace_representation
- serial_manipulator
- barrett_wam
- smokie_robot
- monte_carlo_sampling
- upper_limb
- motion_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text verification needed before
    promotion to verified.
sources:
- id: src_001
  type: paper
  title: Development of Direct Kinematics and Workspace Representation for Smokie
    Robot Manipulator & the Barrett WAM
  url: https://arxiv.org/abs/1707.04820
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper presents a modelling pipeline for two 6-DOF serial manipulators: the Smokie Robot OUR industrial arm and the Barrett WAM. The first step is the assignment of coordinate frames to each link and the measurement of exact link dimensions so that Denavit-Hartenberg (D-H) parameters can be tabulated. Using the D-H parameters, the authors construct homogeneous transformation matrices that describe the direct (forward) kinematics of each manipulator. The computed forward-kinematics functions are then embedded in a MATLAB Monte Carlo sampler that randomly varies joint variables within their limits and accumulates end-effector positions to produce 3-D point-cloud workspace representations. The WAM results are compared with the workspace figure published by the manufacturer, while the Smokie Robot results are presented without an independent reference because the manufacturer did not publish a workspace figure.

## Key Contributions

- Derives complete Denavit-Hartenberg parameter tables for the 6-DOF Smokie Robot and a 6-DOF version of the Barrett WAM.
- Develops direct-kinematics homogeneous transformation matrices for both manipulators.
- Implements a Monte Carlo-based MATLAB procedure to generate and plot 3-D end-effector workspaces.
- Compares the simulated 7-DOF WAM workspace with the manufacturer-published workspace figure.
- Provides isometric, top-view, and side-view workspace plots for both arms.

## Relevance to Humanoid Robotics

The workflow demonstrated in this paper—D-H parameter derivation, direct-kinematics formulation, and Monte Carlo workspace visualization for serial manipulator arms—is directly transferable to humanoid robot upper-limb design and motion planning. Humanoid arms are typically serial or branched serial chains, and accurate forward kinematics plus reachable workspace analysis are prerequisite tasks for trajectory generation, collision avoidance, and deployment verification. Although the paper studies two industrial/research arms rather than a full humanoid, the methods are foundational for modelling humanoid arms and hands.
