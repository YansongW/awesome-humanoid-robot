---
$id: ent_paper_zheng_scalable_simulation_and_demons_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots
  zh: 可扩展的跳跃式压电二维软体机器人仿真与演示
  ko: 확장 가능한 점핑 압전 2차원 소프트 로봇의 시뮬레이션 및 실증
summary:
  en: This paper presents a five-actuator piezoelectric soft robot and a scalable
    PyBullet-based simulation framework that models actuators as discrete rigid-link
    elements connected by motors, validated against static and dynamic experiments
    including inchworm crawling and jumping.
  zh: 本文提出了一种五执行器压电软体机器人，并开发了一个基于 PyBullet 的可扩展仿真框架，该框架将执行器建模为通过电机连接的离散刚性连杆，并通过包括
    inchworm 爬行和跳跃在内的静态与动态实验进行了验证。
  ko: 본 논문은 5개의 구동기를 갖춘 압전 소프트 로봇을 제시하고, 모터로 연결된 이산 강성 링크 요소로 구동부를 모델링하는 확장 가능한 PyBullet
    기반 시뮬레이션 프레임워크를 개발하며, inchworm 기어가기 및 점핑을 포함한 정적·동적 실험으로 검증하였다.
domains:
- 02_components
- 06_design_engineering
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- soft_robot
- piezoelectric_actuator
- pybullet_simulation
- pseudo_rigid_body_model
- soft_actuator
- jumping_robot
- inchworm_motion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper was not inspected.
    Requires human review before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots
  url: https://arxiv.org/abs/2202.13521
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Soft robots can adopt a wide variety of shapes and motions, but their compliant mechanics make modeling and control difficult. This paper demonstrates a planar five-actuator soft robot built from piezoelectric layers laminated onto a steel-foil substrate, and introduces a scalable simulation framework that predicts its static and dynamic behavior. The framework uses the PyBullet physics engine and represents each soft actuator as a chain of discrete rigid links connected by motors; applied voltages are translated into motor torques so that the resulting deformations match the physical robot.

The authors validate their approach through a sequence of experiments of increasing complexity. First, they analyze a single-actuator cantilever under static and AC excitation. They then extend the analyses to the full five-actuator robot, comparing simulated and measured shapes under DC voltages, slow quasi-static inchworm crawling, and impulsive jumping motions in the vertical and vertical-horizontal directions. The simulations capture strongly nonlinear behavior, including forward speeds of approximately 1 cm/s, without curve-fitting parameters to the robot motions.

An important feature of the work is that model parameters—such as stiffness and the voltage-dependent target bending angle—are derived analytically from material and geometric properties rather than tuned empirically. The authors also report an open-source release of their simulation code, enabling others to reproduce and extend the framework.

## Key Contributions

- Demonstration of a five-actuator piezoelectric soft robot capable of inchworm crawling and jumping motions.
- Development of a scalable PyBullet simulation framework that models soft actuators as motor-driven discrete rigid-link elements.
- Analytical derivation of actuator model parameters, including stiffness and voltage-dependent target angle, from material properties.
- Experimental validation of static shapes, cantilever dynamics, inchworm motion, and in-place jumping without curve-fitting motion parameters.
- Open-source release of the simulation code.

## Relevance to Humanoid Robotics

Although the demonstrated prototype is a planar soft robot rather than a humanoid, its validated modeling and simulation methodology is directly relevant to the design of soft actuators, flexible limbs, and compliant structures in humanoid robots. The motor-link pseudo-rigid body approach provides a computationally tractable way to simulate soft components within standard physics engines, which can lower the barrier to prototyping and controlling soft humanoid subsystems. In addition, the analytical parameter-derivation workflow offers a template for moving from material properties to predictive actuator models, supporting knowledge-chain completeness for humanoid components and design-engineering tools.
