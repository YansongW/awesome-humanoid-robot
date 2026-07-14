---
$id: ent_paper_nava_failure_detection_and_fault_to_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Failure Detection and Fault Tolerant Control of a Jet-Powered Flying Humanoid Robot
  zh: 喷气动力飞行人形机器人的故障检测与容错控制
  ko: 제트 동력 비행 휴머노이드 로봇의 고장 감지 및 결허용 제어
summary:
  en: This paper proposes an RPM-based failure detector, a momentum-based flight controller, and an offline reference generator
    for the jet-powered humanoid robot iRonCub to detect and recover from the complete loss of a single turbine during simulated
    flight.
  zh: 该论文为喷气动力人形机器人 iRonCub 提出了一种基于 RPM 的故障检测器、基于动量的飞行控制器以及离线参考轨迹生成器，用于在仿真飞行中检测并恢复单台涡轮机的完全失效。
  ko: 본 논문은 제트 동력 휴머노이드 로봇 iRonCub의 시뮬레이션 비행 중 단일 터빈의 완전한 손실을 감지하고 복구하기 위해 RPM 기반 고장 감지기, 모멘텀 기반 비행 제어기, 오프라인 참조 생성기를 제안한다.
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
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.16075v1.
sources:
- id: src_001
  type: paper
  title: Failure Detection and Fault Tolerant Control of a Jet-Powered Flying Humanoid Robot
  url: https://arxiv.org/abs/2305.16075
  date: '2023'
  accessed_at: '2026-06-26'
---
## 概述
Failure detection and fault tolerant control are fundamental safety features of any aerial vehicle. With the emergence of complex, multi-body flying systems such as jet-powered humanoid robots, it becomes of crucial importance to design fault detection and control strategies for these systems, too. In this paper we propose a fault detection and control framework for the flying humanoid robot iRonCub in case of loss of one turbine. The framework is composed of a failure detector based on turbines rotational speed, a momentum-based flight control for fault response, and an offline reference generator that produces far-from-singularities configurations and accounts for self and jet exhausts collision avoidance. Simulation results with Gazebo and MATLAB prove the effectiveness of the proposed control strategy.

## 核心内容
Failure detection and fault tolerant control are fundamental safety features of any aerial vehicle. With the emergence of complex, multi-body flying systems such as jet-powered humanoid robots, it becomes of crucial importance to design fault detection and control strategies for these systems, too. In this paper we propose a fault detection and control framework for the flying humanoid robot iRonCub in case of loss of one turbine. The framework is composed of a failure detector based on turbines rotational speed, a momentum-based flight control for fault response, and an offline reference generator that produces far-from-singularities configurations and accounts for self and jet exhausts collision avoidance. Simulation results with Gazebo and MATLAB prove the effectiveness of the proposed control strategy.

## 参考
- http://arxiv.org/abs/2305.16075v1

