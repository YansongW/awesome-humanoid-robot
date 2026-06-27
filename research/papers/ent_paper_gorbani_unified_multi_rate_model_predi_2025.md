---
$id: ent_paper_gorbani_unified_multi_rate_model_predi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Multi-Rate Model Predictive Control for a Jet-Powered Humanoid Robot
  zh: 喷气动力人形机器人的统一多速率模型预测控制
  ko: 제트 동력 휴머노이드 로봇을 위한 통합 다중 속도 모델 예측 제어
summary:
  en: This paper presents a multi-rate Model Predictive Control framework for the
    jet-powered humanoid iRonCub that jointly embeds centroidal momentum dynamics
    and second-order nonlinear jet-engine dynamics, validated through MuJoCo simulations.
  zh: 本文提出了一种用于喷气动力人形机器人iRonCub的多速率模型预测控制框架，将质心动量动力学与二阶非线性喷气发动机动力学相结合，并通过MuJoCo仿真进行了验证。
  ko: 본 논문은 제트 동력 휴머노이드 iRonCub를 위한 다중 속도 모델 예측 제어 프레임워크를 제안하며, 질량 중심 운동량 역학과 2차 비선형
    제트 엔진 역학을 통합하고 MuJoCo 시뮬레이션을 통해 검증하였다.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- model_predictive_control
- multi_rate_control
- jet_powered_humanoid
- ironcub
- centroidal_momentum
- flight_control
- lpv_mpc
- jet_dynamics
- mujoco
- osqp
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and provided metadata; full-text review is required
    to confirm section citations, exact numerical claims, and relationship details.
sources:
- id: src_001
  type: paper
  title: Unified Multi-Rate Model Predictive Control for a Jet-Powered Humanoid Robot
  url: https://arxiv.org/abs/2505.16478v2
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

The paper addresses flight control for jet-powered humanoid robots, focusing on the iRonCub platform built on iCub 3. It proposes a Model Predictive Control framework that combines a linearised centroidal momentum model of flight dynamics with a second-order nonlinear model of jet propulsion. The formulation is cast as a Linear Parameter-Varying (LPV) MPC problem so that the slow, nonlinear jet dynamics are explicitly represented in the prediction model rather than treated as instantaneous actuators.

A central contribution is a unified multi-rate MPC scheme that generates control commands at different update rates for the robot's joints and its jet engines, avoiding the need for a hierarchical or cascaded controller decomposition. This is motivated by the practical reality that turbine actuation is typically much slower than joint-level control. The paper reports real-time feasibility using the OSQP solver at 200 Hz with sub-5 millisecond solve times, and presents simulation results in MuJoCo for disturbance rejection and minimum-jerk trajectory tracking.

The authors also include ablation studies to quantify the effect of including jet dynamics, using LPV linearisation, and employing multi-rate control. Limitations noted in the work include the use of Euler-angle representations (with singularities avoided under the intended VTOL envelope), constant rotation-matrix and angular-velocity assumptions over the prediction horizon, neglect of aerodynamic forces, and the absence of real-robot experiments.

## Key Contributions

- LPV MPC formulation that jointly embeds centroidal momentum dynamics and nonlinear second-order jet-engine dynamics.
- Unified multi-rate MPC formulation that handles different actuator update rates for joints and jet engines without hierarchical decomposition.
- Simulation validation on iRonCub in MuJoCo, demonstrating disturbance rejection and stable minimum-jerk flight trajectory tracking.
- Real-time feasibility demonstration using OSQP at 200 Hz with solve times below 5 ms.
- Ablation studies quantifying the impact of jet dynamics, LPV linearisation, and multi-rate control on closed-loop performance.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it targets the iRonCub, a jet-powered humanoid robot derived from the iCub 3 platform. It confronts control challenges that arise from real hardware constraints—specifically the slow, nonlinear dynamics of turbojet engines and the low update rate of turbine actuation—which are critical for practical flight-capable humanoid deployment.

While the niche focus on jet-powered flight maneuvers makes the application less central to mass-production humanoids, the underlying methodology (momentum-based MPC, LPV embedding of actuator dynamics, and multi-rate control) is transferable to other high-degree-of-freedom humanoid systems where actuators operate at heterogeneous rates or where actuator dynamics significantly affect stability.
