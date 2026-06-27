---
$id: ent_paper_amanzadeh_predictive_control_with_indire_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Predictive Control with Indirect Adaptive Laws for Payload Transportation by
    Quadrupedal Robots
  zh: 四足机器人载荷运输的间接自适应预测控制
  ko: 사족 보행 로봇의 페이로드 운송을 위한 간접 적응 예측 제어
summary:
  en: This paper presents a hierarchical adaptive model-predictive-control (AMPC)
    framework for quadrupedal payload transportation, using an indirect gradient-descent
    adaptive law to estimate uncertain reduced-order template-model parameters online,
    embedding a convex stability criterion into MPC constraints, and tracking planned
    trajectories with a low-level nonlinear whole-body QP controller. Hardware experiments
    on the Unitree A1 demonstrate transport of unknown static payloads up to 109%
    of robot mass on flat terrain and 91% on rough terrain, as well as dynamic payloads
    of 73% of robot mass on rough terrain.
  zh: 本文提出了一种用于四足机器人负载运输的分层自适应模型预测控制（AMPC）框架，通过间接梯度下降自适应律在线估计降阶模板模型的不确定参数，将凸稳定性判据嵌入MPC约束，并由低层非线性全身QP控制器跟踪规划轨迹。在Unitree
    A1上的硬件实验表明，机器人可在平地运输质量达自身109%的未知静态负载，在粗糙地形运输达91%，并可在粗糙地形处理相当于自身质量73%的动态负载。
  ko: 본 논문은 간접 경사 하강 적응 법칙을 사용하여 저차원 템플릿 모델의 불확실한 매개변수를 온라인으로 추정하고, MPC 제약 내에 볼록 안정성
    기준을 포함하며, 하위 레벨 비선형 전신 QP 제어기로 궤적을 추적하는 사족 보행 로봇의 페이로드 운송을 위한 계층형 적응 모델 예측 제어(AMPC)
    프레임워크를 제안한다. Unitree A1에서의 하드웨어 실험을 통해 평지에서 로봇 질량의 109%, 거친 지형에서 91%에 달하는 미지의
    정적 페이로드와 거친 지형에서 질량의 73%인 동적 페이로드 운송을 입증하였다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- adaptive_mpc
- model_predictive_control
- whole_body_control
- indirect_adaptive_law
- online_parameter_estimation
- stability_constrained_optimization
- payload_transport
- legged_robots
- quadruped
- unitree_a1
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the abstract and metadata; quantitative payload limits
    and method claims require human review against the full paper.
sources:
- id: src_001
  type: paper
  title: Predictive Control with Indirect Adaptive Laws for Payload Transportation
    by Quadrupedal Robots
  url: https://arxiv.org/abs/2603.08831
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3474550
theoretical_depth:
- method
---

## Overview

Transporting unknown payloads is a critical capability for legged robots in logistics, construction, and service tasks, yet variations in mass and inertia introduce parametric uncertainty that can destabilize model-based controllers. This paper proposes a hierarchical planning and control framework in which a high-level adaptive model predictive controller (AMPC) plans reduced-order trajectories for a single-rigid-body template model while a low-level nonlinear whole-body controller tracks those trajectories at 1 kHz. The high-level AMPC uses an indirect gradient-descent adaptive law to estimate unknown template-model parameters in real time, and it incorporates a convex stability criterion within the MPC constraints to guarantee stability of the parameter-estimation error. Extensive numerical studies and hardware experiments on the Unitree A1 robot validate the framework under static and dynamic payloads, flat and rough terrains, push disturbances, and obstacles.

## Key Contributions

- An indirect gradient-descent adaptive estimation law with formal asymptotic-stability guarantees for the template-model estimation error.
- A convex stability criterion derived as an MPC constraint that enables real-time QP-based adaptive MPC.
- A hierarchical implementation combining high-level AMPC on single-rigid-body dynamics with a 1 kHz nonlinear whole-body QP controller.
- Experimental demonstration of payload transport up to 109% of robot mass on flat terrain, 91% on rough terrain, and dynamic payloads of 73% of robot mass on rough terrain using the Unitree A1.

## Relevance to Humanoid Robotics

Although the experiments are performed on a quadruped, the core techniques—online estimation of mass/inertia parameters, stability-constrained trajectory optimization, and whole-body tracking—are directly applicable to humanoid robots. Humanoids face similar challenges when carrying loads, responding to external pushes, and maintaining balance over uneven terrain, making the AMPC framework a relevant algorithmic reference for load-carrying, balancing, and gait stabilization in humanoid deployment.
