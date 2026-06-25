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
  en: This paper introduces a modular robot control framework that combines Elementary
    Dynamic Actions (EDA) and Dynamic Movement Primitives (DMP) through superposition
    of virtual trajectories and mechanical impedances, formalizing independence of
    modules and closure of stability as essential requirements.
  zh: 本文提出了一种模块化机器人控制框架，通过虚拟轨迹和机械阻抗的叠加结合基本动态动作（EDA）与动态运动基元（DMP），并将模块独立性与稳定性封闭性形式化为核心要求。
  ko: 본 논문은 가상 궤적과 기계적 임피던스의 중첩을 통해 기본 동작 요소(EDA)와 동적 운동 프리미티브(DMP)를 결합하는 모듈형 로봇 제어
    프레임워크를 제안하며, 모듈의 독립성과 안정성 폐쇄성을 필수 요건으로 형식화한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and provided metadata; full-text verification
    needed before final acceptance.
sources:
- id: src_001
  type: paper
  title: Modular Robot Control with Motor Primitives
  url: https://arxiv.org/abs/2505.10694
  date: '2025'
  accessed_at: '2026-06-26'
  doi: 10.1177/ToBeAssigned
---


## Overview

This paper addresses the gap between human motor performance and modern robotic systems in physical contact tasks by proposing a modular control framework inspired by biological motor primitives. The authors argue that biological systems achieve robust and dexterous behavior through a modular organization of fundamental motor building blocks, and that robot control can benefit from a similarly principled decomposition. The framework combines Elementary Dynamic Actions (EDA) and Dynamic Movement Primitives (DMP) using a Norton equivalent network model, where modules contribute virtual trajectories and mechanical impedances that superpose to generate the overall control command.

The authors formalize two essential requirements for such modularity: independence of modules, meaning each module can be designed without detailed knowledge of others, and closure of stability, meaning the combination of stable modules remains stable. They introduce four basic control modules covering joint-space control, task-space position control, and task-space orientation control on both SO(3) and quaternion manifolds. By relying on Jacobian transpose controllers and impedance superposition rather than inverse kinematics, the framework naturally handles kinematic singularities and redundancy while preserving passivity during contact and physical interaction with passive environments.

The paper reports both simulation and real robot experiments demonstrating diverse behaviors, including the combination of discrete and rhythmic movements, exploiting kinematic singularities to hold large external loads with low torque, and controlling robots through external objects rather than only at the end-effector.

## Key Contributions

- Formalizes two requirements for modular robot control: independence of modules and closure of stability.
- Introduces four basic control modules for joint-space, task-space position, and task-space orientation (SO(3) and quaternion).
- Achieves task-space control without solving inverse kinematics, while handling kinematic singularities and redundancy.
- Proves preservation of passivity during contact and physical interaction with passive environments.
- Demonstrates combination of discrete and rhythmic movements through superposition of virtual trajectories and impedances.
- Shows that kinematic singularities can be exploited to maintain high external load with low torque compensation, and that control can extend beyond the end-effector to external objects.

## Relevance to Humanoid Robotics

The proposed framework is relevant to humanoid robotics because it offers a scalable, torque-level control methodology that avoids the computational and robustness limitations of inverse kinematics. Handling redundancy and singularities is especially important for humanoids with many degrees of freedom and complex kinematic chains. The passivity guarantee supports safe physical interaction, which is critical for humanoids operating near people or in unstructured environments. Additionally, the modular structure could simplify control synthesis for mass-produced humanoid platforms by enabling reuse and combination of elementary behaviors.
