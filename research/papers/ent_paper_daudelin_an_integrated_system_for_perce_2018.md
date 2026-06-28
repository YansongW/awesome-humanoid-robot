---
$id: ent_paper_daudelin_an_integrated_system_for_perce_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: An Integrated System for Perception-Driven Autonomy with Modular Robots
  zh: 面向模块化机器人的感知驱动自主集成系统
  ko: 모듈형 로봇을 위한 지각 기반 자율 통합 시스템
summary:
  en: Presents a modular robot system that combines centralized perception, mapping,
    and LTL-based high-level planning with distributed SMORES-EP hardware so the robot
    can autonomously explore unknown environments, decide when and how to reconfigure,
    and manipulate objects to complete tasks, validated in three hardware demonstrations.
  zh: 提出了一种将集中式感知、建图与基于LTL的高层规划同分布式SMORES-EP硬件相结合的模块化机器人系统，使机器人能够自主探索未知环境、决定何时以及如何重构，并操作物体以完成任务，已通过三项硬件演示验证。
  ko: 중앙 집중식 인지, 매핑 및 LTL 기반 고수준 계획을 분산형 SMORES-EP 하드웨어와 결합하여 로봇이 미지 환경을 자율 탐색하고,
    언제 어떻게 재구성할지 결정하며, 물체를 조작해 작업을 완료할 수 있게 하는 모듈형 로봇 시스템을 제시하고 세 가지 하드웨어 시연으로 검증하였다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- intelligence
- system
- knowledge
tags:
- modular_robotics
- self_reconfigurable_robotics
- smores_ep
- ltl_planning
- reactive_reconfiguration
- perception_planning_integration
- apriltag_localization
- rgb_d_perception
- autonomous_exploration
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full paper was not
    independently read. Hardware component specifications, demonstration details,
    and relationship claims require human review before promotion to verified.
sources:
- id: src_001
  type: paper
  title: An Integrated System for Perception-Driven Autonomy with Modular Robots
  url: https://arxiv.org/abs/1709.05435
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper introduces an integrated system in which a modular robot, built from SMORES-EP modules, completes high-level tasks in unknown environments without beacons or human intervention. A centralized perception and mapping pipeline observes the environment, an environment-characterization step maps perceived scenes to a library of robot configurations and behaviors, and an LTL-based high-level planner decides when to reconfigure and which behavior to execute. The hardware combines distributed SMORES-EP modules with a centralized sensor module that carries an Orbecc Astra Mini RGB-D camera, a downward-facing webcam for AprilTag tracking, a UP computing board, and a LiPo battery.

The system architecture deliberately mixes centralized sensing and planning with distributed modular hardware. The robot can autonomously explore, detect task-relevant environmental features such as stairs or tunnels, choose a configuration from its library, physically reconfigure using AprilTag-assisted mobile docking, and then perform object retrieval, stair climbing, or high-reach placement. All demonstrations are performed on physical hardware, not only in simulation.

Three demonstrations are reported: retrieving an object through a tunnel, delivering an object by climbing stairs, and placing an object on a high surface. These are used to argue that the system is the first modular robot implementation to autonomously complete high-level tasks through reactive reconfiguration in unknown environments.

## Key Contributions

- First modular robot system demonstrated to autonomously complete high-level tasks by reactively reconfiguring in unknown environments.
- Hybrid architecture that couples centralized perception, mapping, and LTL-based planning with distributed SMORES-EP modular hardware.
- Environment-characterization method that maps perceived scenes to pre-defined robot configurations and behaviors.
- Mobile reconfiguration procedure using onboard RGB-D sensing, a downward-facing camera, and AprilTag fiducials.
- Hardware validation in three autonomous tasks: tunnel object retrieval, stair-climbing delivery, and high-reach placement.

## Relevance to Humanoid Robotics

The paper does not study humanoid robots directly, so its immediate relevance to humanoid mass production is limited. However, its perception-planning-reconfiguration architecture and its use of a configuration/behavior library could inform adaptive humanoid platforms or modular humanoid subsystems that must change morphology to match task requirements. The reliance on centralized sensing, explicit environment characterization, and reactive LTL planning also illustrates integration challenges that reconfigurable humanoids would face. The work is therefore most useful as a methodological and architectural reference rather than as a component-level contribution to humanoid production.
