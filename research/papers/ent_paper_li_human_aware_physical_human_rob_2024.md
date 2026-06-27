---
$id: ent_paper_li_human_aware_physical_human_rob_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-Aware Physical Human-Robot Collaborative Transportation and Manipulation
    with Multiple Aerial Robots
  zh: 基于多架空中机器人的人类感知物理人机协作搬运与操作
  ko: 다중 공중 로봇을 이용한 인간 인식 물리적 인간-로봇 협력 운반 및 조작
summary:
  en: Proposes a hierarchical control framework in which a team of quadrotors carrying
    a cable-suspended rigid payload collaborates with a human to transport and manipulate
    the load in 6 DoF, using a force-sensorless wrench estimator, a 6-DoF admittance
    controller, and a redundant human-aware force distribution that enforces separation
    constraints.
  zh: 提出了一种分层控制框架，使多架携带缆绳悬挂刚性负载的四旋翼飞行器与人类协作，在6自由度下搬运与操作负载；该方法利用无 force 传感器的外力/力矩估计器、6自由度导纳控制器以及利用内部冗余的人感知力分配来满足分离约束。
  ko: 케이블로 매달린 강체 페이로드를 운반하는 쿼드로터 팀이 인간과 협력하여 6자유도로 물체를 운반 및 조작할 수 있는 계층적 제어 프레임워크를
    제안한다. 이 방법은 force 센서가 없는 외력/토크 추정기, 6자유도 어드미턴스 컨트롤러, 내부 중복성을 활용한 인간 인식 힘 분배를 통해
    분리 제약을 만족한다.
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
- admittance_control
- multi_robot_coordination
- aerial_manipulation
- physical_human_robot_interaction
- collaborative_transport
- force_distribution
- wrench_estimation
- cable_suspended_payload
- human_aware_control
- redundancy_resolution
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text and supplied metadata; requires human review
    before verification.
sources:
- id: src_001
  type: paper
  title: Human-Aware Physical Human-Robot Collaborative Transportation and Manipulation
    with Multiple Aerial Robots
  url: https://arxiv.org/abs/2210.05894
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses physical human-robot collaborative transportation and manipulation of a cable-suspended rigid payload using a team of quadrotors. Existing physical human-robot interaction research has concentrated on single ground or aerial robots, so multi-aerial-robot collaboration remains largely unexplored. The proposed framework lets a human worker directly apply forces and moments to the payload while the robot team assists in transporting and manipulating it in all six degrees of freedom. The experiments use quadrotors equipped with Qualcomm Snapdragon 801 onboard computers, a Vicon motion capture system, and a Phidget micro load cell for validation.

The technical approach has three core components. First, a collaborative payload external wrench estimator infers the wrench applied by the human from the multi-robot dynamics, removing the need for dedicated force sensors on the payload. Second, a 6-DoF admittance controller converts the estimated human wrench into payload motion, producing smooth and intuitive interaction. Third, a human-aware force distribution exploits the internal redundancy of the cable-suspended multi-robot system to enforce separation constraints—such as keeping robots and the human apart—without affecting payload trajectory tracking or interaction quality.

Validation combines extensive simulation with real-world experiments. Scenarios include the robot team helping a human transport and manipulate a load, and the human guiding the robot team through the environment. The authors report the first experimental demonstration, to their knowledge, of a quadrotor team physically collaborating with a human to manipulate a payload in all 6 DoF.

## Key Contributions

- Control method that exploits multi-robot redundancy to perform secondary tasks such as human-robot distancing and inter-robot separation during payload manipulation.
- Collaborative external wrench estimator that infers human forces/moments on the payload without dedicated force sensors.
- 6-DoF admittance controller enabling intuitive human-aerial-robot collaborative transportation and manipulation.
- First experimental demonstration, to the authors' knowledge, of a quadrotor team physically collaborating with a human to manipulate a payload in all 6 DoF.

## Relevance to Humanoid Robotics

Although the experiments use aerial robots, the control primitives are directly transferable to humanoid systems. Force-sensorless wrench estimation, 6-DoF admittance control, and human-aware redundant force distribution address core challenges in humanoid collaborative manipulation, such as co-carrying large objects and safely sharing workspace with human workers. The same redundancy-aware force allocation could be reused on humanoid arms or mobile manipulators for factory-floor material handling, where intuitive physical guidance and guaranteed human-robot separation are critical.
