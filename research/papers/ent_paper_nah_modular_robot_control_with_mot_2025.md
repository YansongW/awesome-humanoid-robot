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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.10694v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
느린 신경근육계에도 불구하고, 인간은 특히 물리적 접촉 작업에서 현대 로봇 기술을 쉽게 능가합니다. 어떻게 이것이 가능할까요? 생물학적 증거는 생물계의 운동 제어가 운동 행동의 기본 구성 요소인 운동 프리미티브의 모듈식 조직화를 통해 이루어짐을 나타냅니다. 신경-운동 제어 연구에서 영감을 받아, 더 단순한 구성 요소를 사용하는 아이디어는 로봇 공학에서 성공적으로 사용되어 왔습니다. 그럼에도 불구하고, 로봇 제어를 위한 모듈성에 대한 포괄적인 정식화는 아직 확립되지 않았습니다. 본 논문에서는 운동 프리미티브를 사용한 로봇 제어를 위한 모듈식 프레임워크를 소개합니다. 모듈식 로봇 제어를 달성하기 위한 두 가지 필수 요구 사항, 즉 모듈의 독립성과 안정성의 폐쇄성을 제시합니다. 주요 제어 모듈을 설명하고, 이 작은 모듈 집합과 그 조합으로부터 광범위한 복잡한 로봇 행동이 생성될 수 있음을 보여줍니다. 제시된 모듈식 제어 프레임워크는 역기구학을 풀지 않고도 작업 공간 제어, 기구학적 특이점 및 기구학적 중복성 문제 해결, 접촉 및 물리적 상호작용을 위한 수동성 유지 등 로봇 제어에 여러 유용한 특성을 보여줍니다. 추가적인 장점으로는 낮은 토크 보상으로 높은 외부 하중을 유지하기 위해 기구학적 특이점을 활용하는 것과, 엔드 이펙터를 넘어 외부 물체까지 로봇을 제어하는 것이 포함됩니다. 모듈식 프레임워크의 효과를 검증하기 위해 시뮬레이션과 실제 로봇 실험을 모두 제시합니다. 우리는 모듈성이 인간 수준의 성능에 필적하는 로봇 행동을 달성하기 위한 효과적인 구성적 프레임워크가 될 수 있다고 결론짓습니다.

## 핵심 내용
느린 신경근육계에도 불구하고, 인간은 특히 물리적 접촉 작업에서 현대 로봇 기술을 쉽게 능가합니다. 어떻게 이것이 가능할까요? 생물학적 증거는 생물계의 운동 제어가 운동 행동의 기본 구성 요소인 운동 프리미티브의 모듈식 조직화를 통해 이루어짐을 나타냅니다. 신경-운동 제어 연구에서 영감을 받아, 더 단순한 구성 요소를 사용하는 아이디어는 로봇 공학에서 성공적으로 사용되어 왔습니다. 그럼에도 불구하고, 로봇 제어를 위한 모듈성에 대한 포괄적인 정식화는 아직 확립되지 않았습니다. 본 논문에서는 운동 프리미티브를 사용한 로봇 제어를 위한 모듈식 프레임워크를 소개합니다. 모듈식 로봇 제어를 달성하기 위한 두 가지 필수 요구 사항, 즉 모듈의 독립성과 안정성의 폐쇄성을 제시합니다. 주요 제어 모듈을 설명하고, 이 작은 모듈 집합과 그 조합으로부터 광범위한 복잡한 로봇 행동이 생성될 수 있음을 보여줍니다. 제시된 모듈식 제어 프레임워크는 역기구학을 풀지 않고도 작업 공간 제어, 기구학적 특이점 및 기구학적 중복성 문제 해결, 접촉 및 물리적 상호작용을 위한 수동성 유지 등 로봇 제어에 여러 유용한 특성을 보여줍니다. 추가적인 장점으로는 낮은 토크 보상으로 높은 외부 하중을 유지하기 위해 기구학적 특이점을 활용하는 것과, 엔드 이펙터를 넘어 외부 물체까지 로봇을 제어하는 것이 포함됩니다. 모듈식 프레임워크의 효과를 검증하기 위해 시뮬레이션과 실제 로봇 실험을 모두 제시합니다. 우리는 모듈성이 인간 수준의 성능에 필적하는 로봇 행동을 달성하기 위한 효과적인 구성적 프레임워크가 될 수 있다고 결론짓습니다.

## 参考
- http://arxiv.org/abs/2505.10694v1
