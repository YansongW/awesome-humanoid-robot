---
$id: ent_paper_sombolestan_hierarchical_adaptive_loco_man_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Adaptive Loco-manipulation Control for Quadruped Robots
  zh: 面向四足机器人的分层自适应移动操作控制
  ko: 사족 로봇을 위한 계층적 적응형 이동-조작 제어
summary:
  en: Proposes a hierarchical adaptive control framework that enables quadruped robots
    to perform loco-manipulation without assuming object mass, terrain friction, or
    slope, and experimentally validates it on a Unitree A1 robot manipulating unknown
    time-varying loads up to 7 kg.
  zh: 提出一种分层自适应控制框架，使四足机器人无需已知物体质量、地形摩擦或坡度即可完成移动操作任务，并在Unitree A1机器人上通过操纵未知时变负载达7
    kg进行了实验验证。
  ko: 사족 로봇이 물체 질량, 지형 마찰 또는 경사를 사전에 알 필요 없이 이동-조작 작업을 수행할 수 있게 하는 계층적 적응형 제어 프레임워크를
    제안하고, Unitree A1 로봇에서 최대 7 kg의 미지 시변 하중을 조작하여 실험적으로 검증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- loco_manipulation
- adaptive_control
- model_predictive_control
- quadruped_robot
- unitree_a1
- force_control
- whole_body_control
- unknown_object_manipulation
- terrain_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv abstract; controller details, stability proofs,
    and full citation context require human review against the PDF.
sources:
- id: src_001
  type: paper
  title: Hierarchical Adaptive Loco-manipulation Control for Quadruped Robots
  url: https://arxiv.org/abs/2209.13145
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper addresses the problem of performing simultaneous locomotion and manipulation with quadruped robots when object and terrain parameters are unknown. It proposes a hierarchical adaptive control framework in which an adaptive manipulation controller first regulates contact forces online to manipulate an unknown object on unknown terrain, and a unified model predictive control (MPC) formulation then incorporates those manipulation forces into the robot dynamics to maintain balance.

The framework does not require prior knowledge of the object's mass, the friction coefficient, or the slope of the terrain. The adaptive layer estimates unknown parameters and adjusts desired manipulation forces, while the MPC layer regulates the interaction force between the robot and the object. The authors validate the approach on a Unitree A1 robot, demonstrating manipulation of an unknown time-varying load up to 7 kg (about 60% of the robot's weight) and rapid adaptation to slopes up to 20° and to surfaces with different friction coefficients.

The work stays primarily at the method level: it combines an adaptive force controller with a whole-body MPC formulation and provides hardware experiments, but leaves multi-dimensional manipulation, grasping/release behaviors, and direct terrain perception for future work.

## Key Contributions

- Adaptive manipulation controller that estimates unknown object mass and external forces for contact-force regulation.
- Unified MPC formulation that augments locomotion dynamics with manipulation force states to regulate interaction forces while maintaining balance.
- Hardware demonstration on a Unitree A1 robot manipulating unknown time-varying loads up to 7 kg without prior object or terrain knowledge.
- Experimental validation on unknown slopes and on surfaces with varying friction coefficients.

## Relevance to Humanoid Robotics

The force-adaptive, whole-body MPC approach developed for quadruped loco-manipulation under model uncertainty is directly transferable to humanoid robots. Humanoids deployed in factories, logistics centers, or unstructured environments must frequently push, carry, or maneuver heavy objects whose mass and inertial properties are not known precisely, while walking over varying terrain. The paper's combination of online adaptive force estimation with a unified balance-and-force MPC provides a template for humanoid whole-body controllers that must maintain stability during physical interaction. The hardware focus on loads up to a large fraction of robot weight also highlights real-world applicability to industrial manipulation tasks where payload-to-robot mass ratios are significant.
