---
$id: ent_paper_pucci_automatic_gain_tuning_of_a_mom_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automatic Gain Tuning of a Momentum Based Balancing Controller for Humanoid
    Robots
  zh: 人形机器人基于动量平衡控制器的自动增益调节
  ko: 휴머노이드 로봇을 위한 모멘텀 기반 균형 제어기의 자동 이득 튜닝
summary:
  en: Proposes an automatic gain-tuning method for a momentum-based balancing controller
    for humanoid robots by linearizing the closed-loop constrained joint-space dynamics
    and optimizing gains to match desired stiffness and damping, validated in simulation
    on the iCub humanoid.
  zh: 提出了一种针对人形机器人基于动量的平衡控制器的自动增益调节方法，通过线性化闭环约束关节空间动力学并优化增益以匹配期望的刚度和阻尼，在iCub人形机器人仿真中进行了验证。
  ko: 휴머노이드 로봇을 위한 모멘텀 기반 균형 제어기의 자동 이득 튜닝 기법을 제안하며, 폐쇄 루프 구속 관절 공간 동역학을 선형화하고 이득을
    최적화하여 원하는 강성과 감쇄 특성을 얻으며, iCub 휴머노이드 시뮬레이션으로 검증함.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- intelligence
- knowledge
tags:
- momentum_based_control
- balancing_controller
- gain_tuning
- floating_base
- centroidal_dynamics
- joint_space_linearization
- symmetric_positive_definite
- icub
- humanoid_robot
- simulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata/abstract; full paper not read. Requires
    human review before verification.
sources:
- id: src_001
  type: paper
  title: Automatic Gain Tuning of a Momentum Based Balancing Controller for Humanoid
    Robots
  url: https://arxiv.org/abs/1610.02849
  date: '2016'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

Humanoid balancing controllers built on momentum-based principles can stabilize the robot's centroidal dynamics, but they typically require the manual tuning of many controller gains. This manual process is time-consuming and difficult, especially for floating-base systems. The paper addresses this problem by proposing an automatic gain-tuning technique for a momentum-based balancing controller that also ensures stabilization of the associated zero dynamics.

The core of the method is to linearize the closed-loop, constrained joint-space dynamics around an equilibrium point and then choose controller gains so that the linearized system exhibits desired stiffness and damping properties. Gain selection is formulated as a least-squares matching problem. Because the gain matrices must remain symmetric and positive definite, the authors propose a tracker for symmetric positive definite matrices that enforces these constraints during optimization.

The proposed approach is evaluated in simulation on a 23-degree-of-freedom model of the iCub humanoid robot. The simulation scenarios include both one-foot and two-foot balancing, demonstrating that the automatically tuned controller can stabilize the robot under the assumed contact conditions.

## Key Contributions

- Automatic gain tuning for momentum-based balancing controllers on humanoid robots.
- Linearization of the closed-loop constrained joint-space dynamics to support systematic gain design.
- Formulation of gain optimization as a least-squares matching of desired stiffness and damping matrices.
- A tracker for symmetric positive definite matrices that enforces gain-matrix constraints online.
- Simulation validation on a 23-DoF iCub humanoid robot for one-foot and two-foot balancing.

## Relevance to Humanoid Robotics

Automated tuning of balancing controllers reduces the manual calibration burden that currently slows the deployment of humanoid robots on different hardware platforms. By targeting momentum-based balancing and centroidal dynamics, the work is directly relevant to stable standing and contact-rich control for humanoids.

However, the reported validation is limited to simulation, and the online implementation of the tuning algorithm is left to future work. Consequently, its immediate applicability to real-world mass production or hardware deployment remains to be demonstrated.
