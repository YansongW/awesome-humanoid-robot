---
$id: ent_paper_arachchige_dynamic_modeling_and_validatio_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dynamic Modeling and Validation of Soft Robotic Snake Locomotion
  zh: 软体机器蛇运动的动态建模与验证
  ko: 소프트 로봇 뱀 보행의 동적 모델링 및 검증
summary:
  en: Presents a complete spatial dynamic model of a pneumatic soft robotic snake
    using a floating-base kinematic skin representation and distributed contact dynamics,
    and validates planar and spatial rolling gaits numerically and experimentally.
  zh: 提出了一种采用浮动基座运动学表皮表示与分布式接触动力学的气动软体机器蛇完整空间动力学模型，并通过数值仿真与实验验证了平面和空间滚动步态。
  ko: 부유 기반 운동학적 피부 표현과 분산 접촉 역학을 활용한 공압식 소프트 로봇 뱀의 완전한 공간 동적 모델을 제시하고, 평면 및 공간 롤링
    보행을 수치적으로 그리고 실험적으로 검증한다.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- soft_robotics
- snake_robot
- continuum_robotics
- pneumatic_artificial_muscles
- mckibben_muscles
- dynamic_modeling
- distributed_contact_dynamics
- floating_base
- recursive_lagrangian
- rolling_gait
- locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; full-text section-level
    verification was not performed.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: Dynamic Modeling and Validation of Soft Robotic Snake Locomotion
  url: https://arxiv.org/abs/2303.02291
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- formalism
- method
---

## Overview

Soft robotic snakes made of compliant materials can continuously deform their bodies, allowing them to mimic biological snakes' flexible and agile locomotion more closely than rigid-bodied designs. However, without wheel support, existing soft snake robots have largely been restricted to planar gaits derived from kinematic models. Because snake locomotion arises from reaction forces produced by distributed skin-ground contact, a dynamic model that captures these contact forces is needed to extend soft snake locomotion into spatial gaits.

This paper develops a complete spatial dynamic model for a pneumatically powered soft robotic snake. The model combines a floating-base kinematic representation of the robot's skin—extended from a neutral-axis curve to the actual skin surface—with a distributed contact-dynamics formulation. The dynamic equations are derived through a recursive Lagrangian approach, enabling the prediction of spatial motion while accounting for contact forces along the body.

The authors numerically evaluate planar and spatial rolling gaits using the proposed model and experimentally validate the resulting trajectories on a pneumatic three-section soft snake prototype with nine actuated degrees of freedom. Qualitative and quantitative comparisons show close agreement, with reported velocity errors below 9% between simulation and the physical prototype.

## Key Contributions

- First complete spatial dynamic model for soft robotic snakes that includes distributed contact dynamics.
- Floating-base kinematic model extended from the neutral axis to the robot skin for contact-point generation.
- Numerical evaluation of planar and spatial rolling gaits in a contact-enabled simulation.
- Experimental validation of both gaits on a pneumatic 9-DoF soft robotic snake prototype.
- Quantitative verification showing less than 9% velocity error between simulation and prototype.

## Relevance to Humanoid Robotics

Although the demonstrated platform is a snake robot rather than a humanoid, the modeling methods are relevant to humanoid systems that use soft pneumatic actuation or continuum-style limbs. The treatment of McKibben-type pneumatic muscle actuators, distributed skin-ground contact, and recursive Lagrangian dynamics provides transferable formalisms for modeling compliance and contact in legged or snake-like appendages.

The work therefore offers indirect but useful foundations for humanoid design engineering, particularly for platforms exploring soft actuation, whole-body contact modeling, or non-rigid kinematic representations. Direct application would require re-deriving the model for the specific geometry and contact conditions of a bipedal or humanoid platform.
