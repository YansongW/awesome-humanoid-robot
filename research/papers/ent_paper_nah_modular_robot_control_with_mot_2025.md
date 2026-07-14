---
$id: ent_paper_nah_modular_robot_control_with_mot_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Modular Robot Control with Motor Primitives
  zh: 基于运动原语的模块化机器人控制
  ko: 모터 프리미티브를 이용한 모듈형 로봇 제어
summary:
  en: This paper introduces a modular robot control framework that combines Elementary Dynamic Actions (EDA) and Dynamic Movement
    Primitives (DMP) through superposition of virtual trajectories and mechanical impedances, formalizing independence of
    modules and closure of stability as essential requirements.
  zh: 本文提出了一种模块化机器人控制框架，通过虚拟轨迹和机械阻抗的叠加结合基本动态动作（EDA）与动态运动基元（DMP），并将模块独立性与稳定性封闭性形式化为核心要求。
  ko: 본 논문은 가상 궤적과 기계적 임피던스의 중첩을 통해 기본 동작 요소(EDA)와 동적 운동 프리미티브(DMP)를 결합하는 모듈형 로봇 제어 프레임워크를 제안하며, 모듈의 독립성과 안정성 폐쇄성을 필수 요건으로
    형식화한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- modular_control
- motor_primitives
- dynamic_movement_primitives
- elementary_dynamic_actions
- impedance_control
- passivity
- task_space_control
- torque_control
- jacobian_transpose
- contact_interaction
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.10694v1.
sources:
- id: src_001
  type: paper
  title: Modular Robot Control with Motor Primitives
  url: https://arxiv.org/abs/2505.10694
  date: '2025'
  accessed_at: '2026-06-26'
  doi: 10.1177/ToBeAssigned
theoretical_depth:
- system
---
## 概述
Despite a slow neuromuscular system, humans easily outperform modern robot technology, especially in physical contact tasks. How is this possible? Biological evidence indicates that motor control of biological systems is achieved by a modular organization of motor primitives, which are fundamental building blocks of motor behavior. Inspired by neuro-motor control research, the idea of using simpler building blocks has been successfully used in robotics. Nevertheless, a comprehensive formulation of modularity for robot control remains to be established. In this paper, we introduce a modular framework for robot control using motor primitives. We present two essential requirements to achieve modular robot control: independence of modules and closure of stability. We describe key control modules and demonstrate that a wide range of complex robotic behaviors can be generated from this small set of modules and their combinations. The presented modular control framework demonstrates several beneficial properties for robot control, including task-space control without solving Inverse Kinematics, addressing the problems of kinematic singularity and kinematic redundancy, and preserving passivity for contact and physical interactions. Further advantages include exploiting kinematic singularity to maintain high external load with low torque compensation, as well as controlling the robot beyond its end-effector, extending even to external objects. Both simulation and actual robot experiments are presented to validate the effectiveness of our modular framework. We conclude that modularity may be an effective constructive framework for achieving robotic behaviors comparable to human-level performance.

## 核心内容
Despite a slow neuromuscular system, humans easily outperform modern robot technology, especially in physical contact tasks. How is this possible? Biological evidence indicates that motor control of biological systems is achieved by a modular organization of motor primitives, which are fundamental building blocks of motor behavior. Inspired by neuro-motor control research, the idea of using simpler building blocks has been successfully used in robotics. Nevertheless, a comprehensive formulation of modularity for robot control remains to be established. In this paper, we introduce a modular framework for robot control using motor primitives. We present two essential requirements to achieve modular robot control: independence of modules and closure of stability. We describe key control modules and demonstrate that a wide range of complex robotic behaviors can be generated from this small set of modules and their combinations. The presented modular control framework demonstrates several beneficial properties for robot control, including task-space control without solving Inverse Kinematics, addressing the problems of kinematic singularity and kinematic redundancy, and preserving passivity for contact and physical interactions. Further advantages include exploiting kinematic singularity to maintain high external load with low torque compensation, as well as controlling the robot beyond its end-effector, extending even to external objects. Both simulation and actual robot experiments are presented to validate the effectiveness of our modular framework. We conclude that modularity may be an effective constructive framework for achieving robotic behaviors comparable to human-level performance.

## 参考
- http://arxiv.org/abs/2505.10694v1

