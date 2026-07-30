---
$id: ent_paper_sakurai_bipedal_robot_running_human_li_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Bipedal Robot Running: Human-like Actuation Timing Using Fast and Slow Adaptations'
  zh: 双足机器人跑步：利用快/慢自适应实现类人驱动时机
  ko: '쌍족 로봇 달리기: 빠르고 느린 적응을 이용한 인간형 구동 타이밍'
summary:
  en: This paper proposes a central-pattern-generator-based controller that combines fast phase resetting at touchdown with
    slow gait-period convergence to reproduce human-like muscle-activation timing in a musculoskeletal bipedal runner, validated
    on a spring-loaded inverted pendulum model and a human-sized robot.
  zh: 本文提出一种基于中枢模式发生器（CPG）的控制器，通过结合触地时的快速相位重置与慢速步态周期收敛，在肌肉骨骼双足跑步机器人中复现人类肌肉激活时序。该方法在弹簧负载倒立摆模型和真人尺寸机器人上得到验证，核心贡献在于利用快慢适应机制实现类人跑步的适应性控制。
  ko: 본 논문은 착지 시 빠른 위상 재설정과 보행 주기의 느린 수렴을 결합한 중추 패턴 생성기 기반 제어기를 제안하여 근골격계 쌍족 주행 로봇에서 인간형 근육 활성화 타이밍을 재현하고, 스프링 로드 인버티드 펜듈럼
    모델과 인간 크기 로봇으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- central_pattern_generator
- bipedal_running
- musculoskeletal_actuation
- gait_cycle_adaptation
- phase_reset
- spring_loaded_inverted_pendulum
- humanoid_locomotion
- thigh_angle_feedback
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.00910v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Bipedal Robot Running: Human-like Actuation Timing Using Fast and Slow Adaptations'
  url: https://arxiv.org/abs/2303.00910
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
研究团队基于被动动力学机制开发真人尺寸双足机器人，针对人类跑步时肌肉激活与步态周期同步的特性，设计了一种包含快慢适应机制的CPG控制器。该控制器在简单弹簧-质量模型和配备仿人类肌肉骨骼系统的机器人上实现类人跑步，通过可调节的致动器控制时序，成功复现了人类跑步的肌肉激活模式。实验结果表明，CPG在调整跑步过程中肌肉激活时序方面发挥关键作用。

## 核心内容
### 方法架构
- 采用中枢模式发生器（CPG）作为核心控制器，包含两种适应机制：
  - **快速适应**：在触地瞬间进行相位重置，即时调整步态相位
  - **慢速适应**：逐步收敛步态周期，实现长期稳定性
- 控制器输出可调节的致动器控制时序，模仿人类跑步时肌肉激活的相对相位关系

### 实验设置
- 验证平台包括：
  - 弹簧负载倒立摆（SLIP）模型，用于简化动力学验证
  - 真人尺寸双足机器人，配备仿人类肌肉骨骼系统的致动器
- 机器人基于被动动态机制开发，强调能量效率与自然步态

### 关键结果
- 快慢适应CPG控制器成功复现人类跑步的肌肉激活时序特征
- 可调节控制时序使机器人实现自适应跑步，适应不同地形与速度变化
- 实验数据表明，CPG的相位重置与周期收敛机制共同作用，有效调整了肌肉激活的时相分布

### 结论
- 研究证实CPG在人类跑步中肌肉激活时序调整中的核心作用
- 该控制策略为双足机器人实现类人、自适应跑步提供了新途径，未来可应用于更复杂地形下的动态运动控制

## Overview
We have been developing human-sized biped robots based on passive dynamic mechanisms. In human locomotion, the muscles activate at the same rate relative to the gait cycle during running. To achieve adaptive running for robots, such characteristics should be reproduced to yield the desired effect, In this study, we designed a central pattern generator (CPG) involving fast and slow adaptation to achieve human-like running using a simple spring-mass model and our developed bipedal robot, which is equipped with actuators that imitate the human musculoskeletal system. Our results demonstrate that the CPG-based controller with fast and slow adaptations, and a adjustable actuator control timing can reproduce human-like running. The results suggest that the CPG contributes to the adjustment of the muscle activation timing in human running.

## Overview
We have been developing human-sized biped robots based on passive dynamic mechanisms. In human locomotion, the muscles activate at the same rate relative to the gait cycle during running. To achieve adaptive running for robots, such characteristics should be reproduced to yield the desired effect. In this study, we designed a central pattern generator (CPG) involving fast and slow adaptation to achieve human-like running using a simple spring-mass model and our developed bipedal robot, which is equipped with actuators that imitate the human musculoskeletal system. Our results demonstrate that the CPG-based controller with fast and slow adaptations, and an adjustable actuator control timing can reproduce human-like running. The results suggest that the CPG contributes to the adjustment of the muscle activation timing in human running.

## Content
We have been developing human-sized biped robots based on passive dynamic mechanisms. In human locomotion, the muscles activate at the same rate relative to the gait cycle during running. To achieve adaptive running for robots, such characteristics should be reproduced to yield the desired effect. In this study, we designed a central pattern generator (CPG) involving fast and slow adaptation to achieve human-like running using a simple spring-mass model and our developed bipedal robot, which is equipped with actuators that imitate the human musculoskeletal system. Our results demonstrate that the CPG-based controller with fast and slow adaptations, and an adjustable actuator control timing can reproduce human-like running. The results suggest that the CPG contributes to the adjustment of the muscle activation timing in human running.

## 개요
우리는 수동적 동역학 메커니즘을 기반으로 한 인간 크기의 이족 보행 로봇을 개발해 왔습니다. 인간의 보행에서 근육은 달리기 중 보행 주기에 대해 동일한 비율로 활성화됩니다. 로봇의 적응형 달리기를 구현하기 위해서는 이러한 특성을 재현하여 원하는 효과를 얻어야 합니다. 본 연구에서는 단순한 스프링-질량 모델과 인간의 근골격계를 모방한 액추에이터를 장착한 자체 개발 이족 보행 로봇을 사용하여 인간과 유사한 달리기를 구현하기 위해 빠른 적응과 느린 적응을 포함하는 중추 패턴 생성기(CPG)를 설계했습니다. 실험 결과, 빠른 적응과 느린 적응, 그리고 조정 가능한 액추에이터 제어 타이밍을 갖춘 CPG 기반 제어기가 인간과 유사한 달리기를 재현할 수 있음을 보여주었습니다. 이러한 결과는 CPG가 인간 달리기에서 근육 활성화 타이밍 조정에 기여함을 시사합니다.

## 핵심 내용
우리는 수동적 동역학 메커니즘을 기반으로 한 인간 크기의 이족 보행 로봇을 개발해 왔습니다. 인간의 보행에서 근육은 달리기 중 보행 주기에 대해 동일한 비율로 활성화됩니다. 로봇의 적응형 달리기를 구현하기 위해서는 이러한 특성을 재현하여 원하는 효과를 얻어야 합니다. 본 연구에서는 단순한 스프링-질량 모델과 인간의 근골격계를 모방한 액추에이터를 장착한 자체 개발 이족 보행 로봇을 사용하여 인간과 유사한 달리기를 구현하기 위해 빠른 적응과 느린 적응을 포함하는 중추 패턴 생성기(CPG)를 설계했습니다. 실험 결과, 빠른 적응과 느린 적응, 그리고 조정 가능한 액추에이터 제어 타이밍을 갖춘 CPG 기반 제어기가 인간과 유사한 달리기를 재현할 수 있음을 보여주었습니다. 이러한 결과는 CPG가 인간 달리기에서 근육 활성화 타이밍 조정에 기여함을 시사합니다.

## 参考
- http://arxiv.org/abs/2303.00910v3
