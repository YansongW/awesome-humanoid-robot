---
$id: ent_formalism_euler_lagrange_equations
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Euler-Lagrange Equations
  zh: 欧拉-拉格朗日方程
  ko: 오일러-라그랑주 방정식
summary:
  en: Second-order differential equations derived from the stationarity of the action integral, giving the equations of motion
    for mechanical systems in generalized coordinates.
  zh: 由作用量变分驻值条件导出的二阶微分方程组，给出广义坐标下机械系统的运动方程。
  ko: 작용 적분의 정지 조건에서 도출된 2차 미분방정식으로, 일반화 좌표에서 기계 시스템의 용동 방정식을 제공.
domains:
- 00_foundations
- 06_design_engineering
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- mechanics
- classical_mechanics
- variational_principle
- lagrangian
- dynamics
- equations_of_motion
- wiki_gap
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-08.md#8.4.2 拉格朗日动力学 by scripts/backfill_nonpaper_entries.py. Body backfilled from entity
    metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_goldstein_2002
  type: other
  title: H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, 3rd ed., Addison-Wesley, 2002
  url: https://doi.org/10.2307/2522307
  date: '2002-01-01'
  accessed_at: '2026-07-09'
- id: src_spong_hutchinson_vidyasagar_2006
  type: other
  title: M. W. Spong, S. Hutchinson, and M. Vidyasagar, Robot Modeling and Control, Wiley, 2006
  url: https://doi.org/10.1002/0470173876
  date: '2006-01-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_lagrangian
  relationship: derived_from
  description:
    en: The Euler-Lagrange equations follow from stationarity of the action integral of the Lagrangian.
    zh: 欧拉-拉格朗日方程由拉格朗日量的作用量变分取驻值导出。
- id: ent_newton_euler_equations
  relationship: mentions
  description:
    en: For rigid-body systems, Euler-Lagrange and Newton-Euler formulations yield the same equations of motion.
    zh: 对刚体系统，欧拉-拉格朗日与牛顿-欧拉两种形式等价。
---

## 概述
由作用量变分驻值条件导出的二阶微分方程组，给出广义坐标下机械系统的运动方程。

## 核心内容
### 欧拉-拉格朗日方程的定义与定位
欧拉-拉格朗日方程属于 **形式化方法** 类型。 所属领域包括：基础学科, 设计工程。 价值链层级：基础层。 由作用量变分驻值条件导出的二阶微分方程组，给出广义坐标下机械系统的运动方程。 英文名称为 *Euler-Lagrange Equations*。 韩文名称为 *오일러-라그랑주 방정식*。

### 欧拉-拉格朗日方程的数学与原理基础
欧拉-拉格朗日方程建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，欧拉-拉格朗日方程通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现欧拉-拉格朗日方程时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
欧拉-拉格朗日方程可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- mechanics
- classical_mechanics
- variational_principle
- lagrangian
- dynamics
- equations_of_motion
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键形式化方法之一，欧拉-拉格朗日方程在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, 3rd ed., Addison-Wesley, 2002](https://doi.org/10.2307/2522307)
- [M. W. Spong, S. Hutchinson, and M. Vidyasagar, Robot Modeling and Control, Wiley, 2006](https://doi.org/10.1002/0470173876)

## Overview
The second-order differential equations derived from the stationary condition of the action variation provide the equations of motion for mechanical systems in generalized coordinates.

## Content
### Definition and Positioning of the Euler-Lagrange Equations
The Euler-Lagrange equations belong to the **formal method** category. Their fields include: foundational disciplines, design engineering. Value chain level: foundational layer. The second-order differential equations derived from the stationary condition of the action variation provide the equations of motion for mechanical systems in generalized coordinates. The English name is *Euler-Lagrange Equations*. The Korean name is *오일러-라그랑주 방정식*.

### Mathematical and Theoretical Foundations of the Euler-Lagrange Equations
The Euler-Lagrange equations are built upon relevant mathematical theories and physical laws. Understanding their assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention should be paid to their input space, output space, objective function, and guarantees of convergence or stability.
In humanoid robots—high-dimensional, underactuated, and strongly coupled systems—the Euler-Lagrange equations often require a balance among real-time performance, accuracy, and robustness.

### Algorithm Steps and Implementation Considerations
When implementing the Euler-Lagrange equations in practice, it is necessary to clarify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable operation of the algorithm on real platforms.

### Typical Applications and Limitations
The Euler-Lagrange equations can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, their computational complexity, dependence on model accuracy, and online adaptability remain key issues to address in practical deployment.

### Related Tags
- mechanics
- classical_mechanics
- variational_principle
- lagrangian
- dynamics
- equations_of_motion
- wiki_gap

### Role in Humanoid Robot Systems
As one of the key formal methods in the humanoid robot industry chain, the Euler-Lagrange equations play an important role in system design, performance optimization, and industrial application. They interact with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall robot performance. Related research and applications are continuously advancing to further improve their reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
작용량 변분 정류 조건에서 유도된 2차 미분방정식 시스템으로, 일반화 좌표에서 기계 시스템의 운동 방정식을 제공합니다.

## 핵심 내용
### 오일러-라그랑주 방정식의 정의와 위치
오일러-라그랑주 방정식은 **형식화 방법** 유형에 속합니다. 관련 분야는 기초 학문, 설계 공학입니다. 가치 사슬 계층: 기초 계층. 작용량 변분 정류 조건에서 유도된 2차 미분방정식 시스템으로, 일반화 좌표에서 기계 시스템의 운동 방정식을 제공합니다. 영어 명칭은 *Euler-Lagrange Equations*입니다. 한국어 명칭은 *오일러-라그랑주 방정식*입니다.

### 오일러-라그랑주 방정식의 수학적 및 원리적 기초
오일러-라그랑주 방정식은 관련 수학 이론과 물리 법칙 위에 구축됩니다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수, 그리고 수렴성 또는 안정성 보장에 주목해야 합니다.
인간형 로봇이라는 고차원, 저구동, 강결합 시스템에서 오일러-라그랑주 방정식은 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 맞춰야 합니다.

### 알고리즘 단계와 구현 요점
오일러-라그랑주 방정식을 실제로 구현할 때는 초기화 조건, 반복 규칙, 중지 기준 및 매개변수 최적화 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 엔지니어링 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 합니다.

### 전형적인 응용과 한계
오일러-라그랑주 방정식은 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- mechanics
- classical_mechanics
- variational_principle
- lagrangian
- dynamics
- equations_of_motion
- wiki_gap

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인에서 핵심적인 형식화 방법 중 하나로서, 오일러-라그랑주 방정식은 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 지속적으로 추진되고 있으며, 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 노력하고 있습니다.
