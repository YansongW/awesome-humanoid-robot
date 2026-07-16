---
$id: ent_method_foc_motor_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Field-Oriented Control (FOC)
  zh: 磁场定向控制（FOC）
  ko: 자장 지향 제어(FOC)
summary:
  en: A motor-control method that transforms three-phase currents into a rotating dq reference frame to enable independent
    control of torque and flux, similar to a DC machine.
  zh: 将三相电流变换到旋转的dq坐标系，分别控制转矩与磁通，使交流电机获得类似直流电机的调速性能。
  ko: 삼상 전류를 회전하는 dq 좌표계로 변환하여 토크와 자속을 독립 제어하는 모터 제어 방식.
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#4.5.2 磁场定向控制（FOC）的数学结构 by scripts/backfill_nonpaper_entries.py. Body backfilled
    from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
将三相电流变换到旋转的dq坐标系，分别控制转矩与磁通，使交流电机获得类似直流电机的调速性能。

## 核心内容
### 磁场定向控制（FOC）的定义与定位
磁场定向控制（FOC）属于 **方法** 类型。 所属领域包括：零部件。 价值链层级：中游。 将三相电流变换到旋转的dq坐标系，分别控制转矩与磁通，使交流电机获得类似直流电机的调速性能。 英文名称为 *Field-Oriented Control (FOC)*。 韩文名称为 *자장 지향 제어(FOC)*。

### 磁场定向控制（FOC）的数学与原理基础
磁场定向控制（FOC）建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，磁场定向控制（FOC）通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现磁场定向控制（FOC）时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
磁场定向控制（FOC）可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- method
- chapter_4
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，磁场定向控制（FOC）在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction

## Overview
Transform three-phase currents into a rotating dq coordinate system to independently control torque and flux, enabling AC motors to achieve speed regulation performance similar to that of DC motors.

## Content
### Definition and Positioning of Field-Oriented Control (FOC)
Field-Oriented Control (FOC) belongs to the **method** type. Its domain includes components. The value chain level is midstream. It transforms three-phase currents into a rotating dq coordinate system to independently control torque and flux, allowing AC motors to achieve speed regulation performance similar to DC motors. The English name is *Field-Oriented Control (FOC)*. The Korean name is *자장 지향 제어(FOC)*.

### Mathematical and Theoretical Foundations of Field-Oriented Control (FOC)
Field-Oriented Control (FOC) is built upon relevant mathematical theories and physical laws. Understanding its assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and convergence or stability guarantees.
In humanoid robots, which are high-dimensional, underactuated, and strongly coupled systems, Field-Oriented Control (FOC) typically requires balancing real-time performance, precision, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing Field-Oriented Control (FOC) in practice, it is necessary to clarify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
Field-Oriented Control (FOC) can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptability remain key issues to address in practical deployment.

### Related Tags
- method
- chapter_4
- wiki_gap

### Role in Humanoid Robot Systems
As one of the key methods in the humanoid robot industry chain, Field-Oriented Control (FOC) plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall machine performance. Related research and applications are continuously advancing to further enhance its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
3상 전류를 회전하는 dq 좌표계로 변환하여 토크와 자속을 각각 제어함으로써, 교류 전동기가 직류 전동기와 유사한 속도 제어 성능을 얻을 수 있도록 합니다.

## 핵심 내용
### 자장 지향 제어(FOC)의 정의와 위치
자장 지향 제어(FOC)는 **방법** 유형에 속합니다. 소속 분야는 부품을 포함합니다. 가치 사슬 계층: 중류. 3상 전류를 회전하는 dq 좌표계로 변환하여 토크와 자속을 각각 제어함으로써, 교류 전동기가 직류 전동기와 유사한 속도 제어 성능을 얻을 수 있도록 합니다. 영문 명칭은 *Field-Oriented Control (FOC)*입니다. 한문 명칭은 *자장 지향 제어(FOC)*입니다.

### 자장 지향 제어(FOC)의 수학적 및 원리적 기초
자장 지향 제어(FOC)는 관련 수학 이론과 물리 법칙에 기반합니다. 그 전제 조건, 제약 조건 및 유도 과정을 이해하는 것은 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수, 그리고 수렴성 또는 안정성 보장에 주목해야 합니다.
휴머노이드 로봇이라는 고차원, 저구동, 강결합 시스템에서 자장 지향 제어(FOC)는 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 이루어야 합니다.

### 알고리즘 단계 및 구현 요점
자장 지향 제어(FOC)를 실제로 구현할 때는 초기화 조건, 반복 규칙, 중지 기준 및 매개변수 튜닝 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 엔지니어링 제약 조건을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 해야 합니다.

### 대표적인 응용 분야와 한계
자장 지향 제어(FOC)는 휴머노이드 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 측면에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- method
- chapter_4
- wiki_gap

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인에서 핵심 방법 중 하나로서, 자장 지향 제어(FOC)는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계의 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
