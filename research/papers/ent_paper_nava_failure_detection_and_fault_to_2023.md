---
$id: ent_paper_nava_failure_detection_and_fault_to_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Failure Detection and Fault Tolerant Control of a Jet-Powered Flying Humanoid
    Robot
  zh: 喷气动力飞行人形机器人的故障检测与容错控制
  ko: 제트 동력 비행 휴머노이드 로봇의 고장 감지 및 결허용 제어
summary:
  en: This paper proposes an RPM-based failure detector, a momentum-based flight controller,
    and an offline reference generator for the jet-powered humanoid robot iRonCub
    to detect and recover from the complete loss of a single turbine during simulated
    flight.
  zh: 该论文为喷气动力人形机器人 iRonCub 提出了一种基于 RPM 的故障检测器、基于动量的飞行控制器以及离线参考轨迹生成器，用于在仿真飞行中检测并恢复单台涡轮机的完全失效。
  ko: 본 논문은 제트 동력 휴머노이드 로봇 iRonCub의 시뮬레이션 비행 중 단일 터빈의 완전한 손실을 감지하고 복구하기 위해 RPM 기반
    고장 감지기, 모멘텀 기반 비행 제어기, 오프라인 참조 생성기를 제안한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 08_software_middleware
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- fault_detection
- fault_tolerant_control
- momentum_based_control
- jet_powered_humanoid
- ironcub
- aerial_humanoid
- thruster_failure
- qp_control
- trajectory_generation
- gazebo_simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: Failure Detection and Fault Tolerant Control of a Jet-Powered Flying Humanoid
    Robot
  url: https://arxiv.org/abs/2305.16075
  date: '2023'
  accessed_at: '2026-06-26'
---

## Overview

The paper addresses safety-critical failure detection and fault-tolerant control for the jet-powered flying humanoid robot iRonCub. The authors propose an integrated framework that detects a complete loss of one turbine, reconfigures the flight controller during the transient, and generates updated attitude and posture references offline to maintain stable flight. The failure detector monitors turbine rotational speed (RPM) to identify fault and shutdown states. The flight controller is formulated as a quadratic program (QP) over thrust rates and joint velocities, with modified input bounds and weight scheduling to account for the faulty turbine. The offline reference generator produces far-from-singularities configurations while avoiding self and jet-exhaust collisions.

The proposed framework is validated through repeated simulations in Gazebo and MATLAB for failures of arm and back turbines. Simulation results demonstrate the ability of the controller to maintain hovering and trajectory tracking after a thruster failure. The authors also publicly release the simulation code repository.

## Key Contributions

- RPM-based turbine failure detector that identifies fault and shutdown states
- Failure-aware momentum-based flight controller using smooth thrust-bound saturation and QP weight scheduling
- Offline reference generator producing far-from-singularities, collision-free posture and attitude references after a fault
- Validation in repeated Gazebo/MATLAB simulations for arm and back turbine failures
- Public release of the simulation code repository

## Relevance to Humanoid Robotics

This work is highly relevant to humanoid robotics because it directly targets the safety and reliability of a complex aerial humanoid platform. Jet-powered flying humanoids such as iRonCub combine multi-body dynamics with high-risk propulsion systems, making thruster failures a critical concern. By enabling fast failure detection and controller reconfiguration, the framework moves such platforms closer to robust real-world deployment. The methods also highlight how control architectures for humanoid robots must address both whole-body posture and aerial stability under actuator faults.
