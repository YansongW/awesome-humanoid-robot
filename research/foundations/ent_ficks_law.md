---
$id: ent_ficks_law
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Fick's law
  zh: 菲克定律
  ko: 픽의 법칙
summary:
  en: A constitutive principle stating that the diffusive flux of a species is proportional to the negative gradient of its
    concentration.
  zh: 一种本构原理，指出物质的扩散通量与其浓度梯度的负值成正比。
  ko: 종의 확산 선속이 농도 기울기의 음수에 비례한다는 구성 원리.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- principle
tags:
- diffusion
- mass_transport
- ficks_law
- concentration
- flux
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_crank_1975
  type: other
  title: J. Crank, The Mathematics of Diffusion, 2nd ed., Oxford University Press, 1975
  url: https://doi.org/10.1093/oso/9780198534112.001.0001
  date: '1975-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_nernst_planck_equation
  relationship: is_prerequisite_for
  description:
    en: The Nernst-Planck equation generalizes Fick's law by adding migration flux due to an electric field.
    zh: 能斯特-普朗克方程在菲克定律基础上增加了电场引起的迁移通量，是其推广。
    ko: 넬스트-플랑크 방정식은 전기장에 의한 이동 선속을 추가하여 픽의 법칙을 일반화합니다.
---

## 概述
一种本构原理，指出物质的扩散通量与其浓度梯度的负值成正比。

## 核心内容
### 菲克定律的定义与定位
菲克定律属于 **原理** 类型。 所属领域包括：基础学科。 价值链层级：基础层。 一种本构原理，指出物质的扩散通量与其浓度梯度的负值成正比。 英文名称为 *Fick's law*。 韩文名称为 *픽의 법칙*。

### 菲克定律的数学与原理基础
菲克定律建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，菲克定律通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现菲克定律时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
菲克定律可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- diffusion
- mass_transport
- ficks_law
- concentration
- flux

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键原理之一，菲克定律在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [J. Crank, The Mathematics of Diffusion, 2nd ed., Oxford University Press, 1975](https://doi.org/10.1093/oso/9780198534112.001.0001)

## Overview
A constitutive principle stating that the diffusion flux of a substance is proportional to the negative gradient of its concentration.

## Content
### Definition and Positioning of Fick's Law
Fick's law belongs to the **principle** type. Its fields include: basic disciplines. Value chain level: foundational layer. A constitutive principle stating that the diffusion flux of a substance is proportional to the negative gradient of its concentration. The English name is *Fick's law*. The Korean name is *픽의 법칙*.

### Mathematical and Theoretical Foundations of Fick's Law
Fick's law is built upon relevant mathematical theories and physical laws. Understanding its underlying assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and convergence or stability guarantees.
In humanoid robots—a high-dimensional, underactuated, and strongly coupled system—Fick's law typically requires a balance between real-time performance, accuracy, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing Fick's law in practice, it is necessary to clarify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
Fick's law can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptability remain key issues to address in practical deployment.

### Related Tags
- diffusion
- mass_transport
- ficks_law
- concentration
- flux

### Role in Humanoid Robot Systems
As one of the key principles in the humanoid robot industry chain, Fick's law plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall system performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요  
물질의 확산 플럭스가 농도 구배의 음의 값에 비례한다는 구성 원리.

## 핵심 내용  
### 픽의 법칙의 정의와 위치  
픽의 법칙은 **원리** 유형에 속한다. 소속 분야는 기초 학문을 포함한다. 가치 사슬 계층: 기초 계층. 물질의 확산 플럭스가 농도 구배의 음의 값에 비례한다는 구성 원리. 영문 명칭은 *Fick's law*이다. 한문 명칭은 *픽의 법칙*이다.

### 픽의 법칙의 수학적 및 원리적 기초  
픽의 법칙은 관련 수학 이론과 물리 법칙 위에 구축된다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제이다.  
구체적으로, 입력 공간, 출력 공간, 목적 함수 및 수렴성 또는 안정성 보장에 주목해야 한다.  
인간형 로봇이라는 고차원, 저구동, 강결합 시스템에서 픽의 법칙은 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 이루어야 한다.

### 알고리즘 단계와 구현 요점  
실제로 픽의 법칙을 구현할 때는 초기화 조건, 반복 규칙, 중지 기준 및 매개변수 최적화 전략을 명확히 해야 한다.  
수치 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있다.  
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 공학적 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 한다.

### 전형적인 응용과 한계  
픽의 법칙은 인간형 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있다.  
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제이다.

### 관련 태그  
- diffusion  
- mass_transport  
- ficks_law  
- concentration  
- flux  

### 인간형 로봇 시스템에서의 역할  
인간형 로봇 산업 체인에서 핵심 원리 중 하나로서 픽의 법칙은 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 한다. 이는 인지, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정한다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있다.
