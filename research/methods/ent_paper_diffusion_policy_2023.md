---
$id: ent_paper_diffusion_policy_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Diffusion Policy
  zh: 扩散策略
  ko: Diffusion Policy
summary:
  en: Visuomotor policy represented as a conditional denoising diffusion process, enabling multimodal action distributions.
  zh: 以条件去噪扩散过程表示的视觉运动策略，可实现多模态动作分布。
  ko: 조건적 노이즈 제거 확산 프로세스로 표현된 시각욱동 정책, 다중 모드 동작 분포 가능.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion
- imitation_learning
- method
- policy
- visuomotor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-02'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: Diffusion Policy
  url: https://diffusion-policy.cs.columbia.edu/
  date: '2023'
  accessed_at: '2026-07-02'
---

## 概述
以条件去噪扩散过程表示的视觉运动策略，可实现多模态动作分布。

## 核心内容
### 扩散策略的定义与定位
扩散策略属于 **方法** 类型。 所属领域包括：AI 模型与算法。 价值链层级：智能层。 以条件去噪扩散过程表示的视觉运动策略，可实现多模态动作分布。 英文名称为 *Diffusion Policy*。 韩文名称为 *Diffusion Policy*。

### 扩散策略的数学与原理基础
扩散策略建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，扩散策略通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现扩散策略时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
扩散策略可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- diffusion
- imitation_learning
- method
- policy
- visuomotor

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，扩散策略在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/)

## Overview
A visual motor policy represented by a conditional denoising diffusion process, enabling multimodal action distributions.

## Content
### Definition and Positioning of Diffusion Policy
Diffusion Policy belongs to the **method** category. Its domain includes: AI models and algorithms. Value chain level: intelligence layer. A visual motor policy represented by a conditional denoising diffusion process, enabling multimodal action distributions. Its English name is *Diffusion Policy*. Its Korean name is *Diffusion Policy*.

### Mathematical and Theoretical Foundations of Diffusion Policy
Diffusion Policy is built upon relevant mathematical theories and physical principles. Understanding its assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and guarantees of convergence or stability.
In humanoid robots, which are high-dimensional, underactuated, and strongly coupled systems, Diffusion Policy typically requires a balance between real-time performance, precision, and robustness.

### Algorithm Steps and Implementation Key Points
In the practical implementation of Diffusion Policy, it is necessary to clarify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Reasonable selection of numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable operation of the algorithm on real platforms.

### Typical Applications and Limitations
Diffusion Policy can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptation capabilities remain key issues to address in practical deployment.

### Related Tags
- diffusion
- imitation_learning
- method
- policy
- visuomotor

### Role in Humanoid Robot Systems
As one of the key methods in the humanoid robot industry chain, Diffusion Policy plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, execution, energy, structure, and verification, collectively determining overall system performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
조건부 잡음 제거 확산 과정으로 표현된 시각 운동 정책은 다중 모드 동작 분포를 구현할 수 있습니다.

## 핵심 내용
### 확산 정책의 정의와 위치
확산 정책은 **방법** 유형에 속합니다. 관련 분야는 AI 모델 및 알고리즘입니다. 가치 사슬 계층은 지능 계층입니다. 조건부 잡음 제거 확산 과정으로 표현된 시각 운동 정책은 다중 모드 동작 분포를 구현할 수 있습니다. 영문 명칭은 *Diffusion Policy*입니다. 한글 명칭은 *Diffusion Policy*입니다.

### 확산 정책의 수학적 및 원리적 기초
확산 정책은 관련 수학 이론과 물리 법칙에 기반을 둡니다. 그 전제 조건, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수 및 수렴성 또는 안정성 보장에 주목해야 합니다.
인간형 로봇과 같은 고차원, 저구동, 강결합 시스템에서 확산 정책은 일반적으로 실시간성, 정밀도 및 견고성 사이에서 균형을 맞춰야 합니다.

### 알고리즘 단계와 구현 요점
실제로 확산 정책을 구현할 때는 초기화 조건, 반복 규칙, 중단 기준 및 매개변수 최적화 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 적절히 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 잡음 및 액추에이터 포화와 같은 엔지니어링 제약 조건을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 합니다.

### 대표적인 응용과 한계
확산 정책은 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- diffusion
- imitation_learning
- method
- policy
- visuomotor

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인에서 핵심 방법 중 하나로서 확산 정책은 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증과 같은 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
