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

## Overview
Despite a slow neuromuscular system, humans easily outperform modern robot technology, especially in physical contact tasks. How is this possible? Biological evidence indicates that motor control of biological systems is achieved by a modular organization of motor primitives, which are fundamental building blocks of motor behavior. Inspired by neuro-motor control research, the idea of using simpler building blocks has been successfully used in robotics. Nevertheless, a comprehensive formulation of modularity for robot control remains to be established. In this paper, we introduce a modular framework for robot control using motor primitives. We present two essential requirements to achieve modular robot control: independence of modules and closure of stability. We describe key control modules and demonstrate that a wide range of complex robotic behaviors can be generated from this small set of modules and their combinations. The presented modular control framework demonstrates several beneficial properties for robot control, including task-space control without solving Inverse Kinematics, addressing the problems of kinematic singularity and kinematic redundancy, and preserving passivity for contact and physical interactions. Further advantages include exploiting kinematic singularity to maintain high external load with low torque compensation, as well as controlling the robot beyond its end-effector, extending even to external objects. Both simulation and actual robot experiments are presented to validate the effectiveness of our modular framework. We conclude that modularity may be an effective constructive framework for achieving robotic behaviors comparable to human-level performance.

## Content
Despite a slow neuromuscular system, humans easily outperform modern robot technology, especially in physical contact tasks. How is this possible? Biological evidence indicates that motor control of biological systems is achieved by a modular organization of motor primitives, which are fundamental building blocks of motor behavior. Inspired by neuro-motor control research, the idea of using simpler building blocks has been successfully used in robotics. Nevertheless, a comprehensive formulation of modularity for robot control remains to be established. In this paper, we introduce a modular framework for robot control using motor primitives. We present two essential requirements to achieve modular robot control: independence of modules and closure of stability. We describe key control modules and demonstrate that a wide range of complex robotic behaviors can be generated from this small set of modules and their combinations. The presented modular control framework demonstrates several beneficial properties for robot control, including task-space control without solving Inverse Kinematics, addressing the problems of kinematic singularity and kinematic redundancy, and preserving passivity for contact and physical interactions. Further advantages include exploiting kinematic singularity to maintain high external load with low torque compensation, as well as controlling the robot beyond its end-effector, extending even to external objects. Both simulation and actual robot experiments are presented to validate the effectiveness of our modular framework. We conclude that modularity may be an effective constructive framework for achieving robotic behaviors comparable to human-level performance.

## 개요
느린 신경근육계에도 불구하고, 인간은 특히 물리적 접촉 작업에서 현대 로봇 기술을 쉽게 능가합니다. 어떻게 이것이 가능할까요? 생물학적 증거는 생물계의 운동 제어가 운동 행동의 기본 구성 요소인 운동 프리미티브의 모듈식 조직화를 통해 이루어짐을 나타냅니다. 신경-운동 제어 연구에서 영감을 받아, 더 단순한 구성 요소를 사용하는 아이디어는 로봇 공학에서 성공적으로 사용되어 왔습니다. 그럼에도 불구하고, 로봇 제어를 위한 모듈성에 대한 포괄적인 정식화는 아직 확립되지 않았습니다. 본 논문에서는 운동 프리미티브를 사용한 로봇 제어를 위한 모듈식 프레임워크를 소개합니다. 모듈식 로봇 제어를 달성하기 위한 두 가지 필수 요구 사항, 즉 모듈의 독립성과 안정성의 폐쇄성을 제시합니다. 주요 제어 모듈을 설명하고, 이 작은 모듈 집합과 그 조합으로부터 광범위한 복잡한 로봇 행동이 생성될 수 있음을 보여줍니다. 제시된 모듈식 제어 프레임워크는 역기구학을 풀지 않고도 작업 공간 제어, 기구학적 특이점 및 기구학적 중복성 문제 해결, 접촉 및 물리적 상호작용을 위한 수동성 유지 등 로봇 제어에 여러 유용한 특성을 보여줍니다. 추가적인 장점으로는 낮은 토크 보상으로 높은 외부 하중을 유지하기 위해 기구학적 특이점을 활용하는 것과, 엔드 이펙터를 넘어 외부 물체까지 로봇을 제어하는 것이 포함됩니다. 모듈식 프레임워크의 효과를 검증하기 위해 시뮬레이션과 실제 로봇 실험을 모두 제시합니다. 우리는 모듈성이 인간 수준의 성능에 필적하는 로봇 행동을 달성하기 위한 효과적인 구성적 프레임워크가 될 수 있다고 결론짓습니다.

## 핵심 내용
느린 신경근육계에도 불구하고, 인간은 특히 물리적 접촉 작업에서 현대 로봇 기술을 쉽게 능가합니다. 어떻게 이것이 가능할까요? 생물학적 증거는 생물계의 운동 제어가 운동 행동의 기본 구성 요소인 운동 프리미티브의 모듈식 조직화를 통해 이루어짐을 나타냅니다. 신경-운동 제어 연구에서 영감을 받아, 더 단순한 구성 요소를 사용하는 아이디어는 로봇 공학에서 성공적으로 사용되어 왔습니다. 그럼에도 불구하고, 로봇 제어를 위한 모듈성에 대한 포괄적인 정식화는 아직 확립되지 않았습니다. 본 논문에서는 운동 프리미티브를 사용한 로봇 제어를 위한 모듈식 프레임워크를 소개합니다. 모듈식 로봇 제어를 달성하기 위한 두 가지 필수 요구 사항, 즉 모듈의 독립성과 안정성의 폐쇄성을 제시합니다. 주요 제어 모듈을 설명하고, 이 작은 모듈 집합과 그 조합으로부터 광범위한 복잡한 로봇 행동이 생성될 수 있음을 보여줍니다. 제시된 모듈식 제어 프레임워크는 역기구학을 풀지 않고도 작업 공간 제어, 기구학적 특이점 및 기구학적 중복성 문제 해결, 접촉 및 물리적 상호작용을 위한 수동성 유지 등 로봇 제어에 여러 유용한 특성을 보여줍니다. 추가적인 장점으로는 낮은 토크 보상으로 높은 외부 하중을 유지하기 위해 기구학적 특이점을 활용하는 것과, 엔드 이펙터를 넘어 외부 물체까지 로봇을 제어하는 것이 포함됩니다. 모듈식 프레임워크의 효과를 검증하기 위해 시뮬레이션과 실제 로봇 실험을 모두 제시합니다. 우리는 모듈성이 인간 수준의 성능에 필적하는 로봇 행동을 달성하기 위한 효과적인 구성적 프레임워크가 될 수 있다고 결론짓습니다.
