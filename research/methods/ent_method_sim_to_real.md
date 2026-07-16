---
$id: ent_method_sim_to_real
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Sim-to-Real Transfer
  zh: Sim-to-Real迁移
  ko: 시뮬-실제 전이
summary:
  en: Techniques for transferring policies or controllers trained in simulation to physical robots, typically using domain
    randomization, system identification, or adaptation.
  zh: 将仿真中训练的策略或控制器迁移到真实机器人的技术，常用域随机化、系统辨识或自适应方法。
  ko: 시뮬레이션에서 학습한 정책·컨트롤러를 실제 로봇으로 전이하는 기술; 도메인 랜덤화·시스템 동정·적응 등을 사용.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_15
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
将仿真中训练的策略或控制器迁移到真实机器人的技术，常用域随机化、系统辨识或自适应方法。

## 核心内容
### Sim-to-Real迁移的定义与定位
Sim-to-Real迁移属于 **方法** 类型。 所属领域包括：AI 模型与算法。 价值链层级：智能层。 将仿真中训练的策略或控制器迁移到真实机器人的技术，常用域随机化、系统辨识或自适应方法。 英文名称为 *Sim-to-Real Transfer*。 韩文名称为 *시뮬-실제 전이*。

### Sim-to-Real迁移的数学与原理基础
Sim-to-Real迁移建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，Sim-to-Real迁移通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现Sim-to-Real迁移时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
Sim-to-Real迁移可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- method
- chapter_15
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，Sim-to-Real迁移在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction

## Overview
Techniques for transferring policies or controllers trained in simulation to real robots, commonly using domain randomization, system identification, or adaptive methods.

## Content
### Definition and Positioning of Sim-to-Real Transfer
Sim-to-Real Transfer belongs to the **method** type. Its domain includes: AI models and algorithms. Value chain level: intelligence layer. It refers to techniques for transferring policies or controllers trained in simulation to real robots, commonly using domain randomization, system identification, or adaptive methods. The English name is *Sim-to-Real Transfer*. The Korean name is *시뮬-실제 전이*.

### Mathematical and Theoretical Foundations of Sim-to-Real Transfer
Sim-to-Real Transfer is built upon relevant mathematical theories and physical laws. Understanding its underlying assumptions, constraints, and derivation processes is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and convergence or stability guarantees.
In humanoid robots—a high-dimensional, underactuated, and strongly coupled system—Sim-to-Real Transfer typically requires balancing real-time performance, precision, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing Sim-to-Real Transfer in practice, it is necessary to specify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable operation on real platforms.

### Typical Applications and Limitations
Sim-to-Real Transfer can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptation capability remain key issues to address in practical deployment.

### Related Tags
- method
- chapter_15
- wiki_gap

### Role in the Humanoid Robot System
As one of the key methods in the humanoid robot industry chain, Sim-to-Real Transfer plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall robot performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
시뮬레이션에서 훈련된 정책이나 제어기를 실제 로봇으로 전이하는 기술로, 일반적으로 도메인 무작위화, 시스템 식별 또는 적응 방법이 사용됩니다.

## 핵심 내용
### Sim-to-Real 전이의 정의와 위치
Sim-to-Real 전이는 **방법** 유형에 속합니다. 소속 분야는 AI 모델 및 알고리즘입니다. 가치 사슬 계층은 지능 계층입니다. 시뮬레이션에서 훈련된 정책이나 제어기를 실제 로봇으로 전이하는 기술로, 일반적으로 도메인 무작위화, 시스템 식별 또는 적응 방법이 사용됩니다. 영어 명칭은 *Sim-to-Real Transfer*입니다. 한국어 명칭은 *시뮬-실제 전이*입니다.

### Sim-to-Real 전이의 수학적 및 원리적 기초
Sim-to-Real 전이는 관련 수학 이론과 물리 법칙에 기반합니다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수 및 수렴성 또는 안정성 보장에 주목해야 합니다.
인간형 로봇과 같은 고차원, 저구동, 강결합 시스템에서 Sim-to-Real 전이는 일반적으로 실시간성, 정밀도 및 강건성 사이의 균형을 유지해야 합니다.

### 알고리즘 단계와 구현 요점
Sim-to-Real 전이를 실제로 구현할 때는 초기화 조건, 반복 규칙, 중단 기준 및 매개변수 최적화 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 엔지니어링 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 합니다.

### 대표적인 응용과 한계
Sim-to-Real 전이는 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있습니다.
그러나 계산 복잡도, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- method
- chapter_15
- wiki_gap

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인에서 핵심 방법 중 하나로서 Sim-to-Real 전이는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
