---
$id: ent_paper_ghansah_hierarchical_reduced_order_mod_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on
    Humanoid Robots
  zh: 面向人形机器人稳健运动的层级化降阶模型预测控制
  ko: 인간형 로봇의 견고한 보행을 위한 계층적 차수 축소 모델 예측 제어
summary:
  en: Presents a hierarchical reduced-order model predictive control framework for
    humanoid locomotion, combining a 40 Hz nonlinear step planner based on ALIP step-to-step
    dynamics with a 500 Hz linear MPC that incorporates arm and torso dynamics, validated
    in simulation and hardware on the Unitree G1.
  zh: 提出了一种面向人形机器人行走的层级化降阶模型预测控制框架，将基于ALIP步间动力学的40 Hz非线性步态规划器与包含手臂和躯干动态的500 Hz线性MPC相结合，并在Unitree
    G1的仿真和硬件实验中进行了验证。
  ko: ALIP 보행 간 동역학에 기반한 40Hz 비선형 보행 계획기와 팔 및 몸통 동역학을 포함하는 500Hz 선형 MPC를 결합한 인간형 로봇
    보행을 위한 계층적 차수 축소 MPC 프레임워크를 제시하고, Unitree G1에서 시뮬레이션 및 하드웨어 실험으로 검증한다.
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
- model_predictive_control
- humanoid_locomotion
- alip
- srb_mpc
- unitree_g1
- push_recovery
- step_planning
- onboard_control
- bipedal_walking
- disturbance_rejection
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review is needed
    to confirm section-level citations, exact experimental conditions, and hardware
    configuration details.
sources:
- id: src_001
  type: paper
  title: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion
    on Humanoid Robots
  url: https://arxiv.org/abs/2509.04722
  date: '2025'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: The proposed hierarchical MPC framework is validated through simulation and
      hardware experiments on the Unitree G1 humanoid robot.
    zh: 所提出的层级化MPC框架在Unitree G1人形机器人上通过仿真和硬件实验进行了验证。
    ko: 제안된 계층적 MPC 프레임워크는 Unitree G1 인간형 로봇에서 시뮬레이션 및 하드웨어 실험을 통해 검증되었다.
- id: ent_oem_unitree_robotics
  relationship: uses
  description:
    en: The hardware experiments use the Unitree G1 humanoid robot produced by Unitree.
    zh: 硬件实验使用了由宇树科技生产的Unitree G1人形机器人。
    ko: 하드웨어 실험에는 Unitree가 제조한 Unitree G1 인간형 로봇이 사용되었다.
---



## Overview

This paper proposes a computationally efficient hierarchical control framework for robust humanoid robot locomotion based on reduced-order models. At the high level, a nonlinear model predictive controller (NMPC) operates on the step-to-step dynamics of the Angular Momentum Linear Inverted Pendulum (ALIP) model, jointly optimizing step periods, step lengths, and ankle torques at 40 Hz. The resulting ALIP trajectories serve as references for a mid-level linear MPC that extends the standard single rigid body (SRB) formulation to include simplified arm and torso dynamics through a decomposed SRB approach, running at 500 Hz on an onboard mini-PC.

The authors report that adaptive step timing increases push-recovery success by 36%, while the added upper-body control improves yaw disturbance rejection. The framework is validated both in simulation with MuJoCo and in hardware experiments on the Unitree G1, demonstrating robust locomotion over indoor and outdoor terrains including grass, stone pavement, and uneven gym mats. The system runs entirely on a Minisforum EM780 onboard computer with an AMD Ryzen 7 7840U CPU, using an Intel RealSense T265 camera for state estimation.

## Key Contributions

- A high-level NMPC based on ALIP step-to-step dynamics that simultaneously optimizes step lengths, step durations, and ankle torques.
- A decomposed single rigid body (SRB) formulation that incorporates arm and torso dynamics while preserving the linearity required for fast linear MPC.
- Extensive simulation and hardware validation on the Unitree G1, showing 36% improvement in push-recovery success from adaptive step timing and improved yaw disturbance rejection through upper-body control.

## Relevance to Humanoid Robotics

Reliable, real-time locomotion control is a core capability for deploying humanoid robots outside controlled laboratory environments. This work directly addresses that need by demonstrating a fast, onboard hierarchical MPC pipeline that runs at practical control frequencies on the Unitree G1 and handles diverse terrains and external disturbances. Its emphasis on computational efficiency and hardware validation supports the broader goal of making humanoid robots robust enough for real-world tasks and scalable toward mass production.
