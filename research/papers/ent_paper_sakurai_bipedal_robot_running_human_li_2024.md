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
  zh: 本文提出一种基于中枢模式发生器的控制器，通过触地时的快速相位重置与步态周期的慢速收敛来复现类人肌肉激活时机，并在弹簧负载倒立摆模型与一台人形尺寸双足机器人上进行了验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.00910v3.
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
We have been developing human-sized biped robots based on passive dynamic mechanisms. In human locomotion, the muscles activate at the same rate relative to the gait cycle during running. To achieve adaptive running for robots, such characteristics should be reproduced to yield the desired effect, In this study, we designed a central pattern generator (CPG) involving fast and slow adaptation to achieve human-like running using a simple spring-mass model and our developed bipedal robot, which is equipped with actuators that imitate the human musculoskeletal system. Our results demonstrate that the CPG-based controller with fast and slow adaptations, and a adjustable actuator control timing can reproduce human-like running. The results suggest that the CPG contributes to the adjustment of the muscle activation timing in human running.

## 核心内容
We have been developing human-sized biped robots based on passive dynamic mechanisms. In human locomotion, the muscles activate at the same rate relative to the gait cycle during running. To achieve adaptive running for robots, such characteristics should be reproduced to yield the desired effect, In this study, we designed a central pattern generator (CPG) involving fast and slow adaptation to achieve human-like running using a simple spring-mass model and our developed bipedal robot, which is equipped with actuators that imitate the human musculoskeletal system. Our results demonstrate that the CPG-based controller with fast and slow adaptations, and a adjustable actuator control timing can reproduce human-like running. The results suggest that the CPG contributes to the adjustment of the muscle activation timing in human running.

## 参考
- http://arxiv.org/abs/2303.00910v3

