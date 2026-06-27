---
$id: ent_paper_baek_toward_control_of_wheeled_huma_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Toward Control of Wheeled Humanoid Robots with Unknown Payloads: Equilibrium
    Point Estimation via Real-to-Sim Adaptation'
  zh: 面向未知载荷轮式人形机器人的控制：通过实到仿自适应估计平衡点
  ko: 미지의 페이로드를 가진 휠형 휴머노이드 로봇 제어를 향한 실제-시뮬레이션 적응 기반 평형점 추정
summary:
  en: This paper presents a framework that estimates the total mass and center of
    mass of a wheeled-legged robot from its proprioceptive response to unknown payloads,
    explicitly predicts the new equilibrium point, and uses a nonlinear dynamics model
    injected into RaiSim whose parameters are optimized by Particle Swarm Optimization
    for real-to-sim adaptation.
  zh: 本文提出了一种框架，该框架根据轮腿机器人对未知载荷的本体感觉响应估计系统总质量和质心，显式预测新的平衡点，并将经粒子群优化参数化后的非线性动力学模型嵌入RaiSim以实现实到仿自适应。
  ko: 본 논문은 휠-다리 로봇이 미지의 페이로드에 대한 본체감각 응답으로부터 전체 질량과 질량 중심을 추정하고, 새로운 평형점을 명시적으로 예측하며,
    입자 군집 최적화로 매개변수를 최적화한 비선형 동역학 모델을 RaiSim에 주입하여 실제-시뮬레이션 적응을 실현하는 프레임워크를 제시한다.
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
- wheeled_humanoid
- wheeled_legged_robot
- unknown_payload
- equilibrium_point_estimation
- real_to_sim
- sim_to_real
- particle_swarm_optimization
- model_based_control
- lqr_control
- wheeled_inverted_pendulum
- raisim
- system_identification
- center_of_mass_estimation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from arXiv abstract and provided metadata; full-text review
    is needed before verification.
sources:
- id: src_001
  type: paper
  title: 'Toward Control of Wheeled Humanoid Robots with Unknown Payloads: Equilibrium
    Point Estimation via Real-to-Sim Adaptation'
  url: https://arxiv.org/abs/2403.10948
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

Controlling wheeled humanoids becomes unstable when the robot manipulates or transports objects whose inertial properties are unknown, because the system's mass, center of mass, and equilibrium point change in ways that are not directly measured. This paper addresses that problem by proposing a framework that explicitly predicts the new equilibrium point of a wheeled-legged robot after it picks up an unknown payload. The approach first estimates the total mass and center of mass of the combined robot-payload system from its proprioceptive response to the initially unknown dynamics, then computes the corresponding equilibrium point. To avoid relying on additional sensors such as force/torque sensors or cameras, and to reduce the amount of expensive real-world data required, the authors use a data-driven real-to-sim adaptation method. A more accurate nonlinear dynamics model, incorporating effects such as friction, damping, and actuator dead-zone, is injected into a RaiSim rigid-body simulator; the parameters of this model are optimized with Particle Swarm Optimization against a small amount of real-world data. The result is a simulator that more closely matches physical behavior and can generate training data for estimating the equilibrium point under payload uncertainty.

The framework is validated on a custom physical wheeled inverted pendulum (WIP) testbed, which is treated as a simplified model of a wheeled-legged robot. The hardware uses an MIT Mini Cheetah actuator, a VectorNav VN-100 inertial measurement unit, and CAN bus communication, with control and data processing implemented in ROS. An LQR controller is designed around the estimated equilibrium point and tested in balancing and tracking tasks. The authors also report an ablation study comparing optimization algorithms and time-series regression architectures, supporting the choice of Particle Swarm Optimization and the selected network structure. The experimental results show that a more precise analytical model with optimized parameters reduces the simulation-to-reality gap and improves the controller's performance when the robot carries unknown payloads.

## Key Contributions

- A framework that explicitly predicts the new equilibrium point of a wheeled-legged robot subject to unknown payload dynamics.
- A real-to-sim adaptation method that embeds a more accurate nonlinear dynamics model into a RaiSim rigid-body simulator.
- Optimization of nonlinear dynamics model parameters using Particle Swarm Optimization to reduce the sim-to-real gap.
- Experimental validation on a custom physical wheeled inverted pendulum testbed using an LQR controller, demonstrating improved balancing and tracking under unknown payloads.
- An ablation study comparing optimization algorithms and time-series regression architectures.

## Relevance to Humanoid Robotics

The work is directly relevant to deploying wheeled humanoids in logistics, warehousing, and industrial settings, where a robot may unexpectedly lift or carry objects whose mass and inertial properties are not known in advance. By estimating the new equilibrium point without extra force/torque sensors or cameras, the framework points toward low-cost, sensor-minimal control strategies that can adapt online to payload changes. Although the current validation is limited to a wheeled inverted pendulum rather than a full humanoid, the underlying problem—maintaining stable model-based control under unknown payload disturbances—is central to practical wheeled-legged humanoid systems.
