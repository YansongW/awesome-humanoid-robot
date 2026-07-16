---
$id: ent_method_whole_body_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Whole-Body Control (WBC)
  zh: 全身控制（WBC）
  ko: 전신 제어(WBC)
summary:
  en: A control framework that coordinates all joints and contacts of a humanoid to achieve multiple tasks such as balance,
    gaze, and manipulation.
  zh: 协调人形机器人所有关节与接触点，以同时实现平衡、注视、操作等多任务的统一控制框架。
  ko: 휴로봇의 모든 관절과 접촉점을 조율하여 균형·시선·조작 등 다중 작업을 동시에 수행하는 제어 프레임워크.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_14
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-08.md#8.4.10 全身控制 by scripts/backfill_nonpaper_entries.py. Body backfilled from entity
    metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
协调人形机器人所有关节与接触点，以同时实现平衡、注视、操作等多任务的统一控制框架。

## 核心内容
### 全身控制（WBC）的定义与定位
全身控制（WBC）属于 **方法** 类型。 所属领域包括：AI 模型与算法。 价值链层级：智能层。 协调人形机器人所有关节与接触点，以同时实现平衡、注视、操作等多任务的统一控制框架。 英文名称为 *Whole-Body Control (WBC)*。 韩文名称为 *전신 제어(WBC)*。

### 全身控制（WBC）的数学与原理基础
全身控制（WBC）建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，全身控制（WBC）通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现全身控制（WBC）时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
全身控制（WBC）可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- method
- chapter_14
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，全身控制（WBC）在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction

## Overview
A unified control framework that coordinates all joints and contact points of a humanoid robot to simultaneously achieve multiple tasks such as balance, gaze, and manipulation.

## Content
### Definition and Positioning of Whole-Body Control (WBC)
Whole-Body Control (WBC) belongs to the **method** type. Its related fields include: AI models and algorithms. Value chain level: intelligence layer. It coordinates all joints and contact points of a humanoid robot to achieve a unified control framework for multiple tasks such as balance, gaze, and manipulation. The English name is *Whole-Body Control (WBC)*. The Korean name is *전신 제어(WBC)*.

### Mathematical and Theoretical Foundations of Whole-Body Control (WBC)
Whole-Body Control (WBC) is built upon relevant mathematical theories and physical laws. Understanding its underlying assumptions, constraints, and derivation processes is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and guarantees of convergence or stability.
In humanoid robots, which are high-dimensional, underactuated, and strongly coupled systems, Whole-Body Control (WBC) typically requires a balance between real-time performance, precision, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing Whole-Body Control (WBC) in practice, it is necessary to specify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
Whole-Body Control (WBC) can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptability remain key issues that need to be addressed in practical deployment.

### Related Tags
- method
- chapter_14
- wiki_gap

### Role in Humanoid Robot Systems
As one of the key methods in the humanoid robot industry chain, Whole-Body Control (WBC) plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, execution, energy, structure, and verification, collectively determining overall robot performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
인간형 로봇의 모든 관절과 접촉점을 조정하여 균형, 응시, 조작 등 여러 작업을 동시에 실현하는 통합 제어 프레임워크.

## 핵심 내용
### 전신 제어(WBC)의 정의와 위치
전신 제어(WBC)는 **방법** 유형에 속합니다. 관련 분야는 AI 모델 및 알고리즘입니다. 가치 사슬 계층: 지능 계층. 인간형 로봇의 모든 관절과 접촉점을 조정하여 균형, 응시, 조작 등 여러 작업을 동시에 실현하는 통합 제어 프레임워크. 영문 명칭은 *Whole-Body Control (WBC)*입니다. 한글 명칭은 *전신 제어(WBC)*입니다.

### 전신 제어(WBC)의 수학적 및 원리적 기초
전신 제어(WBC)는 관련 수학 이론과 물리 법칙에 기반합니다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수 및 수렴성 또는 안정성 보장에 주목해야 합니다.
인간형 로봇이라는 고차원, 저구동, 강결합 시스템에서 전신 제어(WBC)는 일반적으로 실시간성, 정밀도 및 강건성 사이의 균형을 유지해야 합니다.

### 알고리즘 단계 및 구현 요점
전신 제어(WBC)를 실제로 구현할 때는 초기화 조건, 반복 규칙, 중지 기준 및 매개변수 튜닝 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 엔지니어링 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 합니다.

### 대표적인 응용 및 한계
전신 제어(WBC)는 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- method
- chapter_14
- wiki_gap

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인에서 핵심 방법 중 하나로서 전신 제어(WBC)는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
