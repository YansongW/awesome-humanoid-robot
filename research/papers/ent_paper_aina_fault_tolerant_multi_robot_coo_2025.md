---
$id: ent_paper_aina_fault_tolerant_multi_robot_coo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Fault-Tolerant Multi-Robot Coordination with Limited Sensing within Confined
    Environments
  zh: 受限环境下有限感知的多机器人容错协调
  ko: 제한된 환경에서 제한된 감지를 가진 다중 로봇의 결함 허용 조정
summary:
  en: This paper proposes Active Contact Response (ACR), a decentralized fault-tolerance
    method in which robots maintain an egocentric dynamic contact map to estimate
    whether a contact is a faulty stationary peer and either actively push it to a
    less obstructive configuration or fall back to passive avoidance. Physical experiments
    with three active robots excavating cohesive model pellets in a confined tunnel
    show that ACR nearly doubles the number of pellets excavated compared with a passive
    baseline after 30 minutes.
  zh: 本文提出了主动接触响应（ACR），一种去中心化的容错方法：机器人维护以自我为中心的动态接触图，估计接触是否来自故障静止同伴，并主动将其推至阻碍较小的构型或退回到被动避碰。在封闭隧道中使用三个主动机器人挖掘粘性模型颗粒的物理实验表明，30分钟后ACR挖掘的颗粒数量几乎是被动基线的两倍。
  ko: 본 논문은 각 로봇이 자기 중심의 동적 접촉 맵을 유지하여 접촉이 고장 난 정지된 동료로부터 온 것인지 추정하고, 이를 덜 방해가 되는
    구성으로 적극 밀거나 수동 회피로 대응하는 분산형 결함 허용 방법인 Active Contact Response(ACR)를 제안한다. 제한된
    터널에서 세 대의 활성 로봇으로 응집성 모형 펠릿을 굴삭한 물리 실험 결과, 30분 후 ACR은 수동 기준 방법보다 거의 두 배의 펠릿을 굴삭했다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- active_contact_response
- fault_tolerance
- multi_robot_coordination
- decentralized_control
- contact_based_interaction
- swarm_robotics
- confined_environment
- collective_excavation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the full arXiv PDF text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Fault-Tolerant Multi-Robot Coordination with Limited Sensing within Confined
    Environments
  url: https://arxiv.org/abs/2505.15036
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper addresses decentralized fault tolerance in multi-robot teams that lack global state, direct communication, and rich sensing. The authors propose Active Contact Response (ACR), an algorithm in which each robot builds and updates an egocentric dynamic contact map from local collisions, infers the likelihood that a contact is a stationary faulty robot, and then either performs an active displacement maneuver to push the faulty robot to a less obstructive configuration or defaults to a passive collision-avoidance response. The approach is evaluated on a physical collective-excavation task in a narrow tunnel: three active wheel-driven ellipsoidal robots must retrieve cohesive model pellets while a fourth powered-off robot acts as an unannounced faulty obstacle.

The robot controller is a two-layer finite-state machine. The top layer probabilistically chooses between Active Mode (entering the tunnel to excavate) and Conservative Mode (resting at home). The bottom layer reacts to contact events detected by capacitive sensors, IMUs, encoders, force-sensing resistors, magnetometers, and terminal-rod capacitive sensors. When a robot-to-robot contact occurs, ACR updates the contact map with the contact type and longitudinal tunnel position, computes the likelihood Rc that the contact originated from a faulty robot, and selects among default maneuvers, reversal behavior, or the active ACR push. The baseline algorithm has the same hardware and controller but no contact map and no active response to suspected faulty robots.

In three 30-minute physical trials per method, ACR consistently pushed the faulty robot toward the home end of the tunnel and reoriented it closer to parallel with the walls, whereas the baseline often pushed it deeper into the tunnel and caused more severe perpendicular obstructions. The authors report that ACR excavated and deposited nearly twice as many pellets as the baseline by the end of the experiment.

## Key Contributions

- Introduces Active Contact Response (ACR), a fault-tolerance technique that exploits physical contact interactions without explicit fault detection or inter-robot communication.
- Develops an egocentric dynamic contact map that lets robots infer the likely location of a stationary faulty robot from local collision history.
- Enables active robots to collectively reposition faulty peers into less obstructive configurations while preserving decentralized control.
- Validates ACR on a physical multi-robot excavation task, showing nearly twice the pellets excavated compared with a baseline after 30 minutes.
- Demonstrates robust performance across different initial faulty-robot positions and orientations in a confined tunnel.

## Relevance to Humanoid Robotics

The work addresses scalable, decentralized fault tolerance and congestion recovery for robot teams in confined shared workspaces, which is directly relevant to coordinating fleets of humanoid robots during mass-production workflows or warehouse deployments where a failed unit must be cleared without global infrastructure or communication. ACR's reliance on local contact sensing rather than centralized state estimation aligns with scenarios in which humanoids operate in unstructured or communication-denied environments and must maintain collective throughput after a peer failure. The limitation is that the experiments use small wheel-driven robots in a pellet-excavation tunnel, so transfer to humanoid morphology, dynamics, and manipulation-rich tasks remains unverified.
