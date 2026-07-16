---
$id: ent_score_matching
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Score matching
  zh: 分数匹配
  ko: 점수 매칭
summary:
  en: A parameter-estimation technique that learns the gradient of an unknown log-probability density, called the score, without
    requiring normalized probability densities.
  zh: 一种参数估计技术，学习未知对数概率密度的梯度（称为分数），而无需归一化的概率密度。
  ko: 정규화된 확률 밀도 없이도 미지의 로그 확률 밀도의 기울기(점수)를 학습하는 매개변수 추정 기법.
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
- score_estimation
- score_matching
- diffusion
- hyvarinen
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_hyvarinen_2005
  type: paper
  title: A. Hyvärinen, 'Estimation of Non-Normalized Statistical Models by Score Matching', J. Machine Learning Research,
    vol. 6, pp. 695–709, 2005
  url: https://jmlr.org/papers/v6/hyvarinen05a.html
  date: '2005-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_ddpm_reverse_process
  relationship: is_prerequisite_for
  description:
    en: DDPM trains a score-like noise model via denoising score matching and uses it to reverse the diffusion process.
    zh: DDPM 通过去噪分数匹配训练类分数的噪声模型，并用其逆转扩散过程。
    ko: DDPM은 노이즈 제거 점수 매칭을 통해 점수와 유사한 노이즈 모델을 훈련하고 이를 사용하여 확산 과정을 역전시킵니다.
- id: ent_flow_matching
  relationship: builds_on
  description:
    en: Both score matching and flow matching learn vector fields that guide samples between distributions, but flow matching
      directly regresses a velocity field.
    zh: 分数匹配与流匹配都学习引导样本在分布间转移的向量场，但流匹配直接回归速度场。
    ko: 점수 매칭과 흐름 매칭 모두 분포 사이에서 샘플을 안내하는 벡터 필드를 학습하지만, 흐름 매칭은 속도 필드를 직접 회귀합니다.
---

## 概述
一种参数估计技术，学习未知对数概率密度的梯度（称为分数），而无需归一化的概率密度。

## 核心内容
### 分数匹配的定义与定位
分数匹配属于 **算法** 类型。 所属领域包括：基础学科。 价值链层级：基础层。 一种参数估计技术，学习未知对数概率密度的梯度（称为分数），而无需归一化的概率密度。 英文名称为 *Score matching*。 韩文名称为 *점수 매칭*。

### 分数匹配的数学与原理基础
分数匹配建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，分数匹配通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现分数匹配时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
分数匹配可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- generative_modeling
- score_estimation
- score_matching
- diffusion
- hyvarinen

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键算法之一，分数匹配在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [A. Hyvärinen, 'Estimation of Non-Normalized Statistical Models by Score Matching', J. Machine Learning Research, vol. 6, pp. 695–709, 2005](https://jmlr.org/papers/v6/hyvarinen05a.html)

## Overview
A parameter estimation technique that learns the gradient of an unknown log probability density (referred to as the score) without requiring a normalized probability density.

## Content
### Definition and Positioning of Score Matching
Score matching belongs to the **algorithm** type. Its domains include: foundational disciplines. Value chain level: foundational layer. A parameter estimation technique that learns the gradient of an unknown log probability density (referred to as the score) without requiring a normalized probability density. English name: *Score matching*. Korean name: *점수 매칭*.

### Mathematical and Theoretical Foundations of Score Matching
Score matching is built upon relevant mathematical theories and physical principles. Understanding its assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and convergence or stability guarantees.
In humanoid robots, which are high-dimensional, underactuated, and strongly coupled systems, score matching typically requires balancing real-time performance, accuracy, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing score matching in practice, it is necessary to clarify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly enhance computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
Score matching can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptation capability remain key issues to address in practical deployment.

### Related Tags
- generative_modeling
- score_estimation
- score_matching
- diffusion
- hyvarinen

### Role in Humanoid Robot Systems
As one of the key algorithms in the humanoid robot industry chain, score matching plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall machine performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
정규화되지 않은 확률 밀도 없이 미지의 로그 확률 밀도의 기울기(점수라고 함)를 학습하는 매개변수 추정 기술.

## 핵심 내용
### 점수 매칭의 정의와 위치
점수 매칭은 **알고리즘** 유형에 속합니다. 소속 분야는 기초 학문을 포함합니다. 가치 사슬 계층: 기초 계층. 정규화되지 않은 확률 밀도 없이 미지의 로그 확률 밀도의 기울기(점수라고 함)를 학습하는 매개변수 추정 기술. 영어 명칭은 *Score matching*입니다. 한국어 명칭은 *점수 매칭*입니다.

### 점수 매칭의 수학적 및 원리적 기초
점수 매칭은 관련 수학 이론과 물리 법칙에 기반을 둡니다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것은 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수 및 수렴성 또는 안정성 보장에 주목해야 합니다.
인간형 로봇과 같은 고차원, 저구동, 강결합 시스템에서 점수 매칭은 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 맞춰야 합니다.

### 알고리즘 단계와 구현 요점
점수 매칭을 실제로 구현할 때는 초기화 조건, 반복 규칙, 중단 기준 및 매개변수 최적화 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 잡음 및 액추에이터 포화와 같은 공학적 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 해야 합니다.

### 전형적인 응용과 한계
점수 매칭은 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 부분에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- generative_modeling
- score_estimation
- score_matching
- diffusion
- hyvarinen

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인에서 핵심 알고리즘 중 하나로서 점수 매칭은 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
