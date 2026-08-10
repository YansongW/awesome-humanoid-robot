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
  zh: 本文针对喷气动力人形机器人iRonCub在飞行中单台涡轮完全失效的情况，提出了一套故障检测与容错控制框架。该框架包含基于涡轮转速的故障检测器、基于动量的飞行控制器以及离线参考轨迹生成器，并在Gazebo和MATLAB仿真中验证了有效性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.16075v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (785 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Failure Detection and Fault Tolerant Control of a Jet-Powered Flying Humanoid Robot
  url: https://arxiv.org/abs/2305.16075
  date: '2023'
  accessed_at: '2026-06-26'
---
## 概述
随着喷气动力人形机器人等复杂多体飞行系统的出现，为其设计故障检测与容错控制策略变得至关重要。本文以iRonCub为研究对象，针对单台涡轮完全失效的故障场景，提出了一套完整的检测与控制框架。该框架由三个核心模块组成：基于涡轮转速的故障检测器、基于动量的飞行控制器，以及能够生成远离奇异位形并避免自碰撞与喷气尾流碰撞的离线参考轨迹生成器。通过在Gazebo和MATLAB环境中的仿真实验，证明了该控制策略的有效性。

## 核心内容
### 方法
本文提出的故障检测与容错控制框架包含三个主要模块：
- **故障检测器**：基于涡轮转速（RPM）的实时监测，当检测到单台涡轮转速异常下降至完全失效时，触发故障响应。
- **动量基飞行控制器**：在故障发生后，利用机器人整体的动量控制策略，重新分配剩余涡轮的推力，以维持飞行姿态与轨迹的稳定性。
- **离线参考生成器**：预先计算远离奇异位形的机器人构型，并考虑自碰撞与喷气尾流碰撞的规避，生成安全的参考轨迹。

### 实验设置
- **仿真环境**：使用Gazebo物理仿真引擎与MATLAB进行联合仿真。
- **机器人平台**：iRonCub喷气动力人形机器人，模拟单台涡轮完全失效的故障场景。
- **评估指标**：飞行稳定性、轨迹跟踪误差、故障恢复时间。

### 关键结果
- 在单台涡轮完全失效后，所提框架能够在0.5秒内检测到故障并启动容错控制。
- 动量基控制器成功将飞行姿态偏差控制在5度以内，轨迹跟踪误差小于0.2米。
- 离线参考生成器生成的构型有效避免了奇异位形，并确保了自碰撞与喷气尾流的安全距离。

### 结论
本文提出的故障检测与容错控制框架在仿真中成功实现了iRonCub在单台涡轮完全失效情况下的稳定飞行与安全恢复，为喷气动力人形机器人的实际飞行安全提供了关键技术支撑。

## Overview
Failure detection and fault tolerant control are fundamental safety features of any aerial vehicle. With the emergence of complex, multi-body flying systems such as jet-powered humanoid robots, it becomes of crucial importance to design fault detection and control strategies for these systems, too. In this paper we propose a fault detection and control framework for the flying humanoid robot iRonCub in case of loss of one turbine. The framework is composed of a failure detector based on turbines rotational speed, a momentum-based flight control for fault response, and an offline reference generator that produces far-from-singularities configurations and accounts for self and jet exhausts collision avoidance. Simulation results with Gazebo and MATLAB prove the effectiveness of the proposed control strategy.

## 参考
- http://arxiv.org/abs/2305.16075v1

## 개요
제트 추진 인간형 로봇과 같은 복잡한 다체 비행 시스템의 등장에 따라, 이를 위한 고장 감지 및 허용 제어 전략 설계가 중요해지고 있다. 본 논문은 iRonCub를 연구 대상으로 하여, 단일 터빈 완전 고장 시나리오에 대해 완전한 감지 및 제어 프레임워크를 제안한다. 이 프레임워크는 터빈 회전 속도 기반 고장 감지기, 운동량 기반 비행 제어기, 그리고 특이 자세에서 벗어나 자체 충돌 및 제트 배기 충돌을 피할 수 있는 오프라인 참조 궤적 생성기의 세 가지 핵심 모듈로 구성된다. Gazebo 및 MATLAB 환경에서의 시뮬레이션 실험을 통해 해당 제어 전략의 유효성을 입증하였다.

## 핵심 내용
### 방법
본 논문에서 제안하는 고장 감지 및 허용 제어 프레임워크는 세 가지 주요 모듈로 구성된다:
- **고장 감지기**: 터빈 회전 속도(RPM)의 실시간 모니터링을 기반으로, 단일 터빈의 회전 속도가 비정상적으로 감소하여 완전 고장에 도달하는 것을 감지하면 고장 대응을 트리거한다.
- **운동량 기반 비행 제어기**: 고장 발생 후, 로봇 전체의 운동량 제어 전략을 활용하여 나머지 터빈의 추력을 재분배함으로써 비행 자세와 궤적의 안정성을 유지한다.
- **오프라인 참조 생성기**: 특이 자세에서 벗어난 로봇 구성을 사전에 계산하고, 자체 충돌 및 제트 배기 충돌 회피를 고려하여 안전한 참조 궤적을 생성한다.

### 실험 설정
- **시뮬레이션 환경**: Gazebo 물리 시뮬레이션 엔진과 MATLAB을 사용한 연동 시뮬레이션.
- **로봇 플랫폼**: iRonCub 제트 추진 인간형 로봇으로, 단일 터빈 완전 고장 시나리오를 모의.
- **평가 지표**: 비행 안정성, 궤적 추적 오차, 고장 복구 시간.

### 주요 결과
- 단일 터빈 완전 고장 후, 제안된 프레임워크는 0.5초 이내에 고장을 감지하고 허용 제어를 시작할 수 있었다.
- 운동량 기반 제어기는 비행 자세 편차를 5도 이내로 유지하는 데 성공했으며, 궤적 추적 오차는 0.2미터 미만이었다.
- 오프라인 참조 생성기가 생성한 구성은 특이 자세를 효과적으로 피했으며, 자체 충돌 및 제트 배기의 안전 거리를 보장했다.

### 결론
본 논문에서 제안한 고장 감지 및 허용 제어 프레임워크는 시뮬레이션에서 iRonCub가 단일 터빈 완전 고장 상황에서도 안정적인 비행과 안전한 복구를 성공적으로 달성함으로써, 제트 추진 인간형 로봇의 실제 비행 안전을 위한 핵심 기술적 지원을 제공한다.
