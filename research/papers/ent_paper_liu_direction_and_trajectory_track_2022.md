---
$id: ent_paper_liu_direction_and_trajectory_track_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Direction and Trajectory Tracking Control for Nonholonomic Spherical Robot by
    Combining Sliding Mode Controller and Model Prediction Controller
  zh: 结合滑模控制器与模型预测控制器的非完整球形机器人方向与轨迹跟踪控制
  ko: 슬라이딩 모드 컨트롤러와 모델 예측 컨트롤러를 결합한 비홀로노믹 구형 로봇의 방향 및 궤적 추적 제어
summary:
  en: Proposes a hierarchical terminal sliding-mode direction controller (HTSMC),
    a model-predictive instruction planner (MPC), and the combined MHH trajectory-tracking
    framework for a nonholonomic spherical robot, validated with hardware experiments.
  zh: 针对非完整球形机器人提出分层终端滑模方向控制器（HTSMC）、模型预测指令规划器（MPC）以及两者结合的MHH轨迹跟踪框架，并通过硬件实验验证。
  ko: 비홀로노믹 구형 로봇을 위해 계층적 터미널 슬라이딩 모드 방향 제어기(HTSMC), 모델 예측 명령 계획기(MPC), 이를 결합한 MHH
    궤적 추적 프레임워크를 제안하고 하드웨어 실험으로 검증함.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- sliding_mode_control
- model_predictive_control
- trajectory_tracking
- nonholonomic_robot
- lyapunov_stability
- spherical_robot
- hardware_validation
- motion_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full paper text was not reviewed.
    Component and institutional details rely on supplied metadata. Requires human
    review before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Direction and Trajectory Tracking Control for Nonholonomic Spherical Robot
    by Combining Sliding Mode Controller and Model Prediction Controller
  url: https://arxiv.org/abs/2205.14181
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Spherical robots are nonlinear, nonholonomic, and unstable systems, which makes direction and trajectory tracking control difficult. This paper proposes a hierarchical terminal sliding mode controller (HTSMC) for fast and stable direction control, a model predictive controller (MPC) for optimal command planning, and an integrated MHH framework that combines these controllers with an existing velocity controller. Because both torque controllers in the MHH framework are Lyapunov-based sliding mode controllers, the framework aims to achieve good control performance while guaranteeing stability without adding explicit stability or dynamic constraints to the MPC optimization.

The HTSMC integrates a fast terminal algorithm, hierarchical control ideas, and the dynamic motion features of a spherical robot. The MPC layer generates optimal velocity and direction commands that are passed to the lower-level controllers. The authors also present the whole-body dynamic model of the spherical robot and validate the proposed controllers through hardware experiments.

The hardware platform includes a 2-DOF heavy pendulum, spherical shell, central frame, long/short axis motors, IMU, encoder, a mini PC with an Intel i7-8559U, and a lower computer based on a TI TMS320F28069. Experiments were performed on a flat tiled floor to demonstrate the efficacy of the controllers.

## Key Contributions

- Designed HTSMC, a model-based direction controller for spherical robots, and verified it on hardware.
- Proposed the MHH trajectory tracking framework, the first hardware-validated integral trajectory tracking solution for spherical robots reported in the paper.
- Presented an MPC instruction planning controller for spherical robots applied on hardware for the first time in this work.
- Provided the whole-body dynamic model and conducted practical hardware experiments demonstrating controller effectiveness.

## Relevance to Humanoid Robotics

Although the paper studies a spherical robot, its core techniques are directly relevant to humanoid robotics. The Lyapunov-based sliding mode controllers and MPC-based command planning provide stability-guaranteed trajectory tracking methods that can inform humanoid locomotion, balance control, and real-time motion planning. Nonholonomic and unstable dynamics are shared features between spherical robots and bipedal humanoids, so the control design and hardware-validation experience can support future humanoid mass production and deployment.
