---
$id: ent_principle_newton_euler_equations
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Newton-Euler Equations of Motion
  zh: 牛顿-欧拉运动方程
  ko: 뉴턴-오일러 운동 방정식
summary:
  en: The coupled translational and rotational equations that describe how forces and torques produce linear and angular accelerations
    of a rigid body.
  zh: 描述力和力矩如何产生刚体平动和转动加速度的耦合平移与旋转方程。
  ko: 힘과 토크가 강체의 직선 및 각 가속도를 어떻게 생성하는지 기술하는 결합된 평행이동 및 회전 방정식이다.
domains:
- 00_foundations
- 06_design_engineering
layers:
- foundations
- midstream
functional_roles:
- knowledge
tags:
- newton_euler
- rigid_body_dynamics
- equations_of_motion
- classical_mechanics
- humanoid_control
theoretical_depth:
- principle
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard classical-mechanics principle. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: paper
  title: Featherstone, Rigid Body Dynamics Algorithms
  url: https://www.springer.com/gp/book/9780387743141
  date: '2014'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_foundation_classical_mechanics
  relationship: has_prerequisite
  description:
    en: Newton-Euler equations are derived from Newton's second law and Euler's rotation equations.
    zh: 牛顿-欧拉方程由牛顿第二定律和欧拉旋转方程推导而来。
    ko: 뉴턴-오일러 방정식은 뉴턴의 제2법칙과 오일러 회전 방정식에서 유도된다.
---

## 概述
描述力和力矩如何产生刚体平动和转动加速度的耦合平移与旋转方程。

## 核心内容
### 牛顿-欧拉运动方程的定义与定位
牛顿-欧拉运动方程属于 **原理** 类型。 所属领域包括：基础学科, 设计工程。 价值链层级：基础层, midstream。 描述力和力矩如何产生刚体平动和转动加速度的耦合平移与旋转方程。 英文名称为 *Newton-Euler Equations of Motion*。 韩文名称为 *뉴턴-오일러 운동 방정식*。

### 牛顿-欧拉运动方程的数学与原理基础
牛顿-欧拉运动方程建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，牛顿-欧拉运动方程通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现牛顿-欧拉运动方程时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
牛顿-欧拉运动方程可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- newton_euler
- rigid_body_dynamics
- equations_of_motion
- classical_mechanics
- humanoid_control

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键原理之一，牛顿-欧拉运动方程在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Featherstone, Rigid Body Dynamics Algorithms](https://www.springer.com/gp/book/9780387743141)

## Overview
Describes the coupled translational and rotational equations of motion that explain how forces and torques generate linear and angular accelerations of a rigid body.

## Content
### Definition and Positioning of the Newton-Euler Equations of Motion
The Newton-Euler equations of motion belong to the **principle** type. Their fields include: fundamental disciplines, design engineering. Value chain level: foundational layer, midstream. They describe the coupled translational and rotational equations of motion for how forces and torques generate rigid body linear and angular accelerations. The English name is *Newton-Euler Equations of Motion*. The Korean name is *뉴턴-오일러 운동 방정식*.

### Mathematical and Theoretical Foundations of the Newton-Euler Equations of Motion
The Newton-Euler equations of motion are built upon related mathematical theories and physical laws. Understanding their underlying assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to their input space, output space, objective function, and guarantees of convergence or stability.
In humanoid robots—a high-dimensional, underactuated, and strongly coupled system—the Newton-Euler equations of motion often require a balance between real-time performance, accuracy, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing the Newton-Euler equations of motion in practice, it is necessary to clarify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation must be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
The Newton-Euler equations of motion can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, their computational complexity, dependence on model accuracy, and online adaptability remain key issues to address in practical deployment.

### Related Tags
- newton_euler
- rigid_body_dynamics
- equations_of_motion
- classical_mechanics
- humanoid_control

### Role in Humanoid Robot Systems
As one of the key principles in the humanoid robot industry chain, the Newton-Euler equations of motion play an important role in system design, performance optimization, and industrial application. They interact with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall robot performance. Related research and applications are continuously advancing to further improve their reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
힘과 토크가 강체의 병진 및 회전 가속도를 어떻게 결합시키는지 설명하는 병진-회전 결합 방정식.

## 핵심 내용
### 뉴턴-오일러 운동 방정식의 정의와 위치
뉴턴-오일러 운동 방정식은 **원리** 유형에 속합니다. 관련 분야는 기초 학문, 설계 공학을 포함합니다. 가치 사슬 계층은 기초 계층, 중류(midstream)입니다. 힘과 토크가 강체의 병진 및 회전 가속도를 어떻게 결합시키는지 설명하는 병진-회전 결합 방정식입니다. 영문 명칭은 *Newton-Euler Equations of Motion*입니다. 한글 명칭은 *뉴턴-오일러 운동 방정식*입니다.

### 뉴턴-오일러 운동 방정식의 수학적 및 원리적 기초
뉴턴-오일러 운동 방정식은 관련 수학 이론과 물리 법칙에 기반합니다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수 및 수렴성 또는 안정성 보장에 주목해야 합니다.
인간형 로봇과 같은 고차원, 저구동, 강결합 시스템에서 뉴턴-오일러 운동 방정식은 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 맞춰야 합니다.

### 알고리즘 단계와 구현 요점
뉴턴-오일러 운동 방정식을 실제로 구현할 때는 초기화 조건, 반복 규칙, 중단 기준 및 매개변수 최적화 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 공학적 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 합니다.

### 전형적인 응용과 한계
뉴턴-오일러 운동 방정식은 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- newton_euler
- rigid_body_dynamics
- equations_of_motion
- classical_mechanics
- humanoid_control

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인에서 핵심 원리 중 하나로서 뉴턴-오일러 운동 방정식은 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
