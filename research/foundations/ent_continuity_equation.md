---
$id: ent_continuity_equation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Continuity equation
  zh: 连续性方程
  ko: 연속 방정식
summary:
  en: A partial differential equation expressing local conservation of a quantity by equating its rate of change to the negative
    divergence of its flux.
  zh: 一种偏微分方程，通过将某物理量的变化率等于其通量散度的负值来表达局部守恒。
  ko: 어떤 물리량의 변화율을 그 선속의 발산의 음수와 같게 하여 국소 보존을 표현하는 편미분 방정식.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- principle
tags:
- conservation
- pde
- continuity_equation
- mass_transport
- probability
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_evans_2010
  type: other
  title: L. C. Evans, Partial Differential Equations, 2nd ed., American Mathematical Society, 2010
  url: https://doi.org/10.1090/gsm/019
  date: '2010-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_ficks_law
  relationship: builds_on
  description:
    en: Substituting Fick's flux into the continuity equation gives the diffusion equation.
    zh: 将菲克通量代入连续性方程可得到扩散方程。
    ko: 픽의 선속을 연속 방정식에 대입하면 확산 방정식을 얻습니다.
- id: ent_flow_matching
  relationship: is_prerequisite_for
  description:
    en: Flow matching constructs probability paths that satisfy the continuity equation by design.
    zh: 流匹配按设计构造满足连续性方程的概率路径。
    ko: 흐름 매칭은 설계상 연속 방정식을 만족하는 확률 경로를 구성합니다.
- id: ent_ddpm_reverse_process
  relationship: is_prerequisite_for
  description:
    en: The continuous-time probability flow of diffusion models satisfies a Fokker-Planck continuity equation.
    zh: 扩散模型的连续时间概率流满足 Fokker-Planck 连续性方程。
    ko: 확산 모델의 연속 시간 확률 흐름은 포커-플랑크 연속 방정식을 만족합니다.
---

## 概述
一种偏微分方程，通过将某物理量的变化率等于其通量散度的负值来表达局部守恒。

## 核心内容
### 连续性方程的定义与定位
连续性方程属于 **方程** 类型。 所属领域包括：基础学科。 价值链层级：基础层。 一种偏微分方程，通过将某物理量的变化率等于其通量散度的负值来表达局部守恒。 英文名称为 *Continuity equation*。 韩文名称为 *연속 방정식*。

### 连续性方程的数学与原理基础
连续性方程建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，连续性方程通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现连续性方程时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
连续性方程可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- conservation
- pde
- continuity_equation
- mass_transport
- probability

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方程之一，连续性方程在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [L. C. Evans, Partial Differential Equations, 2nd ed., American Mathematical Society, 2010](https://doi.org/10.1090/gsm/019)

## Overview
A partial differential equation that expresses local conservation by equating the rate of change of a physical quantity to the negative divergence of its flux.

## Content
### Definition and Positioning of the Continuity Equation
The continuity equation belongs to the **equation** type. Its fields include: foundational disciplines. Value chain level: foundational layer. A partial differential equation that expresses local conservation by equating the rate of change of a physical quantity to the negative divergence of its flux. Its English name is *Continuity equation*. Its Korean name is *연속 방정식*.

### Mathematical and Theoretical Foundations of the Continuity Equation
The continuity equation is built upon relevant mathematical theories and physical laws. Understanding its underlying assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and guarantees of convergence or stability.
In humanoid robots—a high-dimensional, underactuated, and strongly coupled system—the continuity equation typically requires a balance among real-time performance, accuracy, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing the continuity equation in practice, it is necessary to specify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
The continuity equation can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptability remain key issues that need to be addressed in practical deployment.

### Related Tags
- conservation
- pde
- continuity_equation
- mass_transport
- probability

### Role in Humanoid Robot Systems
As one of the key equations in the humanoid robot industry chain, the continuity equation plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall robot performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
어떤 물리량의 변화율을 그 플럭스(flux)의 발산(divergence)의 음의 값과 같게 설정하여 국소적 보존을 표현하는 편미분 방정식.

## 핵심 내용
### 연속 방정식의 정의와 위치
연속 방정식은 **방정식** 유형에 속한다. 소속 분야는 기초 학문을 포함한다. 가치 사슬 계층: 기초 계층. 어떤 물리량의 변화율을 그 플럭스의 발산의 음의 값과 같게 설정하여 국소적 보존을 표현하는 편미분 방정식. 영어 명칭은 *Continuity equation*이다. 한국어 명칭은 *연속 방정식*이다.

### 연속 방정식의 수학적 및 원리적 기초
연속 방정식은 관련 수학 이론과 물리 법칙 위에 구축된다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것은 이 방법을 올바르게 적용하기 위한 전제 조건이다.
구체적으로는 입력 공간, 출력 공간, 목적 함수, 그리고 수렴성 또는 안정성 보장에 주목할 필요가 있다.
인간형 로봇이라는 고차원, 저구동, 강결합 시스템에서 연속 방정식은 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 맞춰야 한다.

### 알고리즘 단계와 구현 요점
연속 방정식을 실제로 구현할 때는 초기화 조건, 반복 규칙, 중단 기준 및 매개변수 최적화 전략을 명확히 해야 한다.
수치적 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 공학적 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 한다.

### 대표적 응용과 한계
연속 방정식은 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제이다.

### 관련 태그
- conservation
- pde
- continuity_equation
- mass_transport
- probability

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인에서 핵심 방정식 중 하나로서, 연속 방정식은 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 한다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정한다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있다.
