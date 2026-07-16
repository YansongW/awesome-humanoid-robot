---
$id: ent_flow_matching
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Flow matching
  zh: 流匹配
  ko: 흐름 매칭
summary:
  en: A generative modeling method that directly regresses a vector field whose flow maps a simple source distribution to
    a target data distribution.
  zh: 一种生成建模方法，直接回归一个向量场，使其流将简单源分布映射到目标数据分布。
  ko: 간단한 소스 분포를 목표 데이터 분포로 매핑하는 흐름을 가진 벡터 필드를 직접 회귀하는 생성 모델링 방법.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- generative_modeling
- flow_matching
- ode
- vector_field
- normalizing_flow
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_lipman_2023
  type: paper
  title: Y. Lipman et al., 'Flow Matching for Generative Modeling', ICLR, 2023
  url: https://openreview.net/forum?id=PqvMRDCJT9t
  date: '2023-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_continuity_equation
  relationship: builds_on
  description:
    en: Flow matching explicitly constructs vector fields whose probability paths satisfy the continuity equation.
    zh: 流匹配显式构造其概率路径满足连续性方程的向量场。
    ko: 흐름 매칭은 확률 경로가 연속 방정식을 만족하는 벡터 필드를 명시적으로 구성합니다.
- id: ent_score_matching
  relationship: builds_on
  description:
    en: Like score matching, flow matching learns a vector field over data space, but it directly regresses a velocity rather
      than a score.
    zh: 与分数匹配类似，流匹配也学习数据空间上的向量场，但它直接回归速度而非分数。
    ko: 점수 매칭과 마찬가지로 흐름 매칭은 데이터 공간에 대한 벡터 필드를 학습하지만, 점수가 아닌 속도를 직접 회귀합니다.
- id: ent_ddpm_reverse_process
  relationship: is_alternative_to
  description:
    en: Flow matching offers a deterministic ODE-based alternative to the stochastic reverse diffusion chain used by DDPM.
    zh: 流匹配为 DDPM 使用的随机逆扩散链提供了一种基于确定性 ODE 的替代方案。
    ko: 흐름 매칭은 DDPM에서 사용하는 확률적 역 확산 체인에 대한 결정론적 ODE 기반 대안을 제공합니다.
---

## 概述
一种生成建模方法，直接回归一个向量场，使其流将简单源分布映射到目标数据分布。

## 核心内容
### 流匹配的定义与定位
流匹配属于 **方法** 类型。 所属领域包括：基础学科。 价值链层级：基础层。 一种生成建模方法，直接回归一个向量场，使其流将简单源分布映射到目标数据分布。 英文名称为 *Flow matching*。 韩文名称为 *흐름 매칭*。

### 流匹配的数学与原理基础
流匹配建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，流匹配通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现流匹配时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
流匹配可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- generative_modeling
- flow_matching
- ode
- vector_field
- normalizing_flow

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，流匹配在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Y. Lipman et al., 'Flow Matching for Generative Modeling', ICLR, 2023](https://openreview.net/forum?id=PqvMRDCJT9t)

## Overview
A generative modeling method that directly regresses a vector field, whose flow maps a simple source distribution to the target data distribution.

## Content
### Definition and Positioning of Flow Matching
Flow matching belongs to the **method** type. Its related fields include: basic disciplines. Value chain level: foundational layer. A generative modeling method that directly regresses a vector field, whose flow maps a simple source distribution to the target data distribution. Its English name is *Flow matching*. Its Korean name is *흐름 매칭*.

### Mathematical and Theoretical Foundations of Flow Matching
Flow matching is built upon relevant mathematical theories and physical laws. Understanding its assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and convergence or stability guarantees.
In humanoid robots, which are high-dimensional, underactuated, and strongly coupled systems, flow matching typically requires a balance between real-time performance, accuracy, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing flow matching in practice, it is necessary to clarify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
Flow matching can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptability remain key issues to address in practical deployment.

### Related Tags
- generative_modeling
- flow_matching
- ode
- vector_field
- normalizing_flow

### Role in Humanoid Robot Systems
As one of the key methods in the humanoid robot industry chain, flow matching plays an important role in system design, performance optimization, and industrial application. It couples with multiple subsystems such as perception, decision-making, execution, energy, structure, and verification, collectively determining overall machine performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
단순한 소스 분포를 목표 데이터 분포로 매핑하는 흐름을 생성하는 벡터 필드를 직접 회귀하는 생성 모델링 방법입니다.

## 핵심 내용
### 흐름 매칭의 정의와 위치
흐름 매칭은 **방법** 유형에 속합니다. 관련 분야는 기초 학문을 포함합니다. 가치 사슬 계층: 기초 계층. 단순한 소스 분포를 목표 데이터 분포로 매핑하는 흐름을 생성하는 벡터 필드를 직접 회귀하는 생성 모델링 방법입니다. 영어 명칭은 *Flow matching*입니다. 한국어 명칭은 *흐름 매칭*입니다.

### 흐름 매칭의 수학적 및 원리적 기초
흐름 매칭은 관련 수학 이론과 물리 법칙에 기반합니다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수 및 수렴성 또는 안정성 보장에 주목해야 합니다.
휴머노이드 로봇이라는 고차원, 저구동, 강결합 시스템에서 흐름 매칭은 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 유지해야 합니다.

### 알고리즘 단계 및 구현 요점
흐름 매칭을 실제로 구현할 때는 초기화 조건, 반복 규칙, 중단 기준 및 매개변수 튜닝 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 공학적 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 합니다.

### 대표적인 응용 및 한계
흐름 매칭은 휴머노이드 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 측면에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- generative_modeling
- flow_matching
- ode
- vector_field
- normalizing_flow

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인에서 핵심 방법 중 하나로서 흐름 매칭은 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
