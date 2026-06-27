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
  en: This paper proposes a central-pattern-generator-based controller that combines
    fast phase resetting at touchdown with slow gait-period convergence to reproduce
    human-like muscle-activation timing in a musculoskeletal bipedal runner, validated
    on a spring-loaded inverted pendulum model and a human-sized robot.
  zh: 本文提出一种基于中枢模式发生器的控制器，通过触地时的快速相位重置与步态周期的慢速收敛来复现类人肌肉激活时机，并在弹簧负载倒立摆模型与一台人形尺寸双足机器人上进行了验证。
  ko: 본 논문은 착지 시 빠른 위상 재설정과 보행 주기의 느린 수렴을 결합한 중추 패턴 생성기 기반 제어기를 제안하여 근골격계 쌍족 주행 로봇에서
    인간형 근육 활성화 타이밍을 재현하고, 스프링 로드 인버티드 펜듈럼 모델과 인간 크기 로봇으로 검증하였다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; full-text verification
    and native-speaker review of translations are required before promotion to verified.
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

## Overview

The authors develop human-sized bipedal robots based on passive-dynamic mechanisms and target one hallmark of human running: muscles activate at fixed phases of the gait cycle regardless of speed. To embed this behavior in a robot, they design a central pattern generator (CPG) that has two timescales of adaptation. A fast adaptation resets the CPG phase at touchdown, while a slow adaptation gradually updates the estimated gait period in a rhythm generator. A pattern formulator then translates the CPG output into actuator commands, adjusting leg actuation timing using thigh-angle feedback.

The controller is first evaluated numerically on a simple spring-loaded inverted pendulum (SLIP) running model. The same control architecture is then implemented on the authors' musculoskeletal bipedal robot, which uses brushless hip motors, pneumatic vastus actuators, pressure sensors, springs, rubber bands, and a muscle-tendon wire-driven transmission. The robot is constrained to sagittal-plane motion during the experiments.

Results show that the CPG with fast and slow adaptations and adjustable actuator timing can reproduce human-like running. The authors also report that the robot and human kinematics share similar phase-dependent joint-angle peaks during running, suggesting that the CPG contributes to adjusting muscle activation timing in human running.

## Key Contributions

- Designed a CPG rhythm generator with fast adaptation via phase resetting at touchdown and slow adaptation via convergence of the estimated gait period.
- Implemented a pattern formulator that adjusts leg actuation timing based on thigh-angle feedback to sustain running.
- Validated the controller numerically on a spring-loaded inverted pendulum (SLIP) model.
- Demonstrated human-like running on a human-sized musculoskeletal bipedal robot constrained in the sagittal plane.
- Showed that robot and human kinematics exhibit similar phase-dependent joint-angle peaks during running.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it addresses adaptive, bio-inspired control of human-sized bipedal locomotion. Reproducing human-like activation timing relative to the gait cycle can improve running stability, energy efficiency, and robustness to speed variations in humanoid robots. The musculoskeletal-style actuation and CPG-based timing adjustment also bridge neuroscience insights and hardware implementation, offering a practical control method for legged humanoids intended for real-world deployment.
