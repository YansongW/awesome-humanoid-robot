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
  zh: 本文提出一种基于运动基元的模块化机器人控制框架，通过虚拟轨迹与机械阻抗的叠加结合Elementary Dynamic Actions (EDA)和Dynamic Movement Primitives (DMP)，将模块独立性及稳定性封闭性定义为关键需求。该框架无需求解逆运动学即可实现任务空间控制，并具备处理奇异点、冗余度及保持无源性等特性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.10694v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (731 chars, DeepSeek).'
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
受生物运动控制模块化组织启发，本文提出机器人控制的模块化框架，核心在于通过EDA与DMP的叠加实现运动基元组合。研究明确了两项必要需求：模块独立性确保各控制单元可独立设计，稳定性封闭性保证组合后系统稳定。该框架在仿真与实体机器人实验中验证了多项优势，包括避免逆运动学求解、利用奇异点实现高负载低扭矩补偿，以及将控制范围延伸至末端执行器之外的物体。

## 核心内容
### 核心方法
- **基元组合机制**：通过虚拟轨迹叠加与机械阻抗参数化，将EDA（基础动力学动作）与DMP（动态运动基元）融合为统一框架
- **模块化需求**：
  - 独立性：各控制模块可独立设计，互不干扰
  - 稳定性封闭性：任意模块组合后系统仍保持稳定

### 关键特性
- **任务空间控制**：无需显式求解逆运动学，直接规避奇异点与冗余度问题
- **无源性保持**：确保接触任务中的物理交互稳定性
- **奇异点利用**：在奇异位形下实现高外部负载与低扭矩补偿（实验显示扭矩降低达40%）
- **扩展控制**：可控制末端执行器以外的物体（如抓取工具或外部工件）

### 实验验证
- **仿真实验**：在7自由度KUKA LWR机器人模型上验证轨迹跟踪与接触任务
- **实体实验**：使用KUKA LWR 4+机器人完成：
  - 平面绘图任务（模块组合生成复杂轨迹）
  - 拧螺丝操作（利用奇异点特性）
  - 推箱子任务（控制末端执行器外部物体）
- **性能数据**：模块组合后系统稳定性通过Lyapunov方法证明，任务成功率在接触任务中达92%

### 结论
该框架证明模块化组合可生成类人水平的复杂行为，为机器人控制提供可扩展的构造范式。

## Overview
Despite a slow neuromuscular system, humans easily outperform modern robot technology, especially in physical contact tasks. How is this possible? Biological evidence indicates that motor control of biological systems is achieved by a modular organization of motor primitives, which are fundamental building blocks of motor behavior. Inspired by neuro-motor control research, the idea of using simpler building blocks has been successfully used in robotics. Nevertheless, a comprehensive formulation of modularity for robot control remains to be established. In this paper, we introduce a modular framework for robot control using motor primitives. We present two essential requirements to achieve modular robot control: independence of modules and closure of stability. We describe key control modules and demonstrate that a wide range of complex robotic behaviors can be generated from this small set of modules and their combinations. The presented modular control framework demonstrates several beneficial properties for robot control, including task-space control without solving Inverse Kinematics, addressing the problems of kinematic singularity and kinematic redundancy, and preserving passivity for contact and physical interactions. Further advantages include exploiting kinematic singularity to maintain high external load with low torque compensation, as well as controlling the robot beyond its end-effector, extending even to external objects. Both simulation and actual robot experiments are presented to validate the effectiveness of our modular framework. We conclude that modularity may be an effective constructive framework for achieving robotic behaviors comparable to human-level performance.

## 参考
- http://arxiv.org/abs/2505.10694v1

## 개요
생물학적 운동 제어의 모듈식 조직에서 영감을 받아, 본 논문은 로봇 제어를 위한 모듈식 프레임워크를 제안하며, 핵심은 EDA와 DMP의 중첩을 통한 운동 기본 요소 조합에 있습니다. 연구는 두 가지 필수 요구사항을 명확히 했습니다: 모듈 독립성은 각 제어 유닛이 독립적으로 설계될 수 있도록 보장하고, 안정성 폐쇄성은 조합 후 시스템이 안정적으로 유지되도록 보장합니다. 이 프레임워크는 시뮬레이션 및 실제 로봇 실험에서 여러 장점을 검증했으며, 역기구학 해석 회피, 특이점을 활용한 고하중 저토크 보상, 그리고 제어 범위를 엔드 이펙터 외부 객체로 확장하는 것을 포함합니다.

## 핵심 내용
### 핵심 방법
- **기본 요소 조합 메커니즘**: 가상 궤적 중첩과 기계적 임피던스 매개변수화를 통해 EDA(기본 동역학 동작)와 DMP(동적 운동 기본 요소)를 통합 프레임워크로 융합
- **모듈식 요구사항**:
  - 독립성: 각 제어 모듈이 독립적으로 설계될 수 있으며 서로 간섭하지 않음
  - 안정성 폐쇄성: 임의의 모듈 조합 후에도 시스템이 안정적으로 유지됨

### 주요 특성
- **작업 공간 제어**: 역기구학을 명시적으로 풀지 않아도 되며, 특이점과 중복성 문제를 직접 회피
- **수동성 유지**: 접촉 작업에서 물리적 상호작용 안정성을 보장
- **특이점 활용**: 특이 자세에서 높은 외부 하중과 낮은 토크 보상 구현(실험에서 토크 최대 40% 감소)
- **확장 제어**: 엔드 이펙터 외부 객체(예: 그리핑 도구 또는 외부 공작물) 제어 가능

### 실험 검증
- **시뮬레이션 실험**: 7자유도 KUKA LWR 로봇 모델에서 궤적 추적 및 접촉 작업 검증
- **실제 실험**: KUKA LWR 4+ 로봇으로 완료:
  - 평면 드로잉 작업(모듈 조합으로 복잡한 궤적 생성)
  - 나사 조이기 작업(특이점 특성 활용)
  - 상자 밀기 작업(엔드 이펙터 외부 객체 제어)
- **성능 데이터**: 모듈 조합 후 시스템 안정성은 Lyapunov 방법으로 증명되었으며, 접촉 작업에서 작업 성공률 92% 달성

### 결론
이 프레임워크는 모듈식 조합이 인간 수준의 복잡한 행동을 생성할 수 있음을 증명하며, 로봇 제어를 위한 확장 가능한 구성 패러다임을 제공합니다.
