---
$id: ent_method_field_oriented_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Field-Oriented Control
  zh: 磁场定向控制
  ko: 전계 지향 제어
summary:
  en: A motor control technique that transforms three-phase stator currents into a rotating d-q reference frame aligned with
    the rotor flux, enabling independent torque and flux control.
  zh: 一种电机控制技术，将三相定子电流变换到与转子磁链对齐的旋转 d-q 坐标系，实现转矩与磁链的解耦控制。
  ko: 3상 정자 전류를 회전자 자속에 맞춘 d-q 좌표계로 변환하여 토크와 자속을 독립적으로 제어하는 모터 제어 기법.
domains:
- 02_components
- 07_ai_models_algorithms
layers:
- upstream
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- motor
- pmsm
- bldc
- servo
- current_control
- actuator
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-04.md#4.5.2 磁场定向控制（FOC）的数学结构 by scripts/backfill_nonpaper_entries.py. Body backfilled
    from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_mohan_2003
  type: other
  title: 'N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013'
  url: https://doi.org/10.1002/9781118704810
  date: '2013-01-01'
  accessed_at: '2026-07-09'
- id: src_krause_wasynczuk_sudhoff_2013
  type: other
  title: P. C. Krause, O. Wasynczuk, and S. D. Sudhoff, Analysis of Electric Machinery and Drive Systems, 3rd ed., IEEE Press/Wiley,
    2013
  url: https://doi.org/10.1002/9781118526030
  date: '2013-01-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_component_rotary_actuator_2024
  relationship: applies_to
  description:
    en: FOC is widely used inside rotary actuator servo drives for PMSM/BLDC motors in humanoid joints.
    zh: FOC 广泛用于人形机器人关节旋转执行器中的 PMSM/BLDC 伺服驱动。
- id: ent_method_pid_control
  relationship: requires
  description:
    en: FOC typically uses PI/PID current controllers in the d-q frame to regulate flux and torque currents.
    zh: FOC 通常在 d-q 坐标系中使用 PI/PID 电流控制器调节磁链电流与转矩电流。
---

## 概述
一种电机控制技术，将三相定子电流变换到与转子磁链对齐的旋转 d-q 坐标系，实现转矩与磁链的解耦控制。

## 核心内容
### 磁场定向控制的定义与定位
磁场定向控制属于 **方法** 类型。 所属领域包括：零部件, AI 模型与算法。 价值链层级：上游。 一种电机控制技术，将三相定子电流变换到与转子磁链对齐的旋转 d-q 坐标系，实现转矩与磁链的解耦控制。 英文名称为 *Field-Oriented Control*。 韩文名称为 *전계 지향 제어*。

### 磁场定向控制的数学与原理基础
磁场定向控制建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，磁场定向控制通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现磁场定向控制时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
磁场定向控制可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- motor
- pmsm
- bldc
- servo
- current_control
- actuator

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，磁场定向控制在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013](https://doi.org/10.1002/9781118704810)
- [P. C. Krause, O. Wasynczuk, and S. D. Sudhoff, Analysis of Electric Machinery and Drive Systems, 3rd ed., IEEE Press/Wiley, 2013](https://doi.org/10.1002/9781118526030)

## Overview
A motor control technique that transforms three-phase stator currents into a rotating d-q coordinate system aligned with the rotor flux, achieving decoupled control of torque and flux.

## Content
### Definition and Positioning of Field-Oriented Control
Field-Oriented Control belongs to the **method** type. Its domains include: components, AI models and algorithms. Value chain level: upstream. A motor control technique that transforms three-phase stator currents into a rotating d-q coordinate system aligned with the rotor flux, achieving decoupled control of torque and flux. The English name is *Field-Oriented Control*. The Korean name is *전계 지향 제어*.

### Mathematical and Theoretical Foundations of Field-Oriented Control
Field-Oriented Control is built upon relevant mathematical theories and physical laws. Understanding its assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and guarantees of convergence or stability.
In humanoid robots, which are high-dimensional, underactuated, and strongly coupled systems, Field-Oriented Control typically requires a balance among real-time performance, precision, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing Field-Oriented Control in practice, it is necessary to define initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
Field-Oriented Control can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptability remain key issues to address in practical deployment.

### Related Tags
- motor
- pmsm
- bldc
- servo
- current_control
- actuator

### Role in Humanoid Robot Systems
As one of the key methods in the humanoid robot industry chain, Field-Oriented Control plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall machine performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
3상 고정자 전류를 회전자 자속과 정렬된 회전 d-q 좌표계로 변환하여 토크와 자속의 디커플링 제어를 구현하는 전동기 제어 기술입니다.

## 핵심 내용
### 전계 지향 제어의 정의와 위치
전계 지향 제어는 **방법** 유형에 속합니다. 소속 분야는 부품, AI 모델 및 알고리즘을 포함합니다. 가치 사슬 계층: 상류. 3상 고정자 전류를 회전자 자속과 정렬된 회전 d-q 좌표계로 변환하여 토크와 자속의 디커플링 제어를 구현하는 전동기 제어 기술입니다. 영문 명칭은 *Field-Oriented Control*입니다. 한글 명칭은 *전계 지향 제어*입니다.

### 전계 지향 제어의 수학적 및 원리적 기초
전계 지향 제어는 관련 수학 이론과 물리 법칙에 기반합니다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수 및 수렴성 또는 안정성 보장에 주목해야 합니다.
인간형 로봇이라는 고차원, 저구동, 강결합 시스템에서 전계 지향 제어는 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 맞춰야 합니다.

### 알고리즘 단계와 구현 요점
전계 지향 제어를 실제로 구현할 때는 초기화 조건, 반복 규칙, 정지 기준 및 파라미터 튜닝 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화 등의 엔지니어링 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 합니다.

### 전형적인 응용과 한계
전계 지향 제어는 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- motor
- pmsm
- bldc
- servo
- current_control
- actuator

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인에서 핵심 방법 중 하나로서 전계 지향 제어는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계의 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
