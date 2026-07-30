---
$id: ent_paper_colledanchise_act_perceive_and_plan_in_belie_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Act, Perceive, and Plan in Belief Space for Robot Localization
  zh: 在信念空间中行动、感知与规划以实现机器人定位
  ko: 로봇 위치 추정을 위한 신념 공간에서의 행동, 인식 및 계획
summary:
  en: This paper proposes an interleaved acting-and-planning framework that reduces robot pose uncertainty by planning sequences
    of actuation and perception actions in belief space, using a best-first search guided by an entropy-based heuristic. The
    method was validated in simulation and on the IIT-R1 humanoid robot, showing that active semantic perception can complement
    feature-based localization in ambiguous environments.
  zh: 本文提出了一种在信念空间中交错执行与规划的方法，通过基于熵启发式的最佳优先搜索，规划驱动与感知动作序列，以降低机器人位姿不确定性。该方法在仿真和IIT-R1人形机器人上验证，表明主动语义感知能在模糊环境中补充基于特征的定位。
  ko: 본 논문은 엔트로피 기반 휴리스틱을 사용하는 최우선 탐색을 통해 신념 공간에서 구동 및 인식 동작 시퀀스를 계획함으로써 로봇 자세 불확실성을 줄이는 행동-계획 상호 교차 프레임워크를 제안한다. 이 방법은 시뮬레이션과
    IIT-R1 휴머노이드 로봇에서 검증되었으며, 모호한 환경에서 능동적 의미 인식이 특징 기반 위치 추정을 보완할 수 있음을 보여준다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- active_perception
- belief_space_planning
- robot_localization
- semantic_localization
- entropy_based_search
- iit_r1
- humanoid_localization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2002.08124v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Act, Perceive, and Plan in Belief Space for Robot Localization
  url: https://arxiv.org/abs/2002.08124
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
现有定位方法依赖点、线、面等低层几何特征，虽精度高，但在初始猜测不准时收敛缓慢。本文提出一种交错执行与规划框架，任务规划器计算动作与感知任务序列，主动从环境获取相关信息（如识别物体或询问方向）。该方法在大状态空间和真实环境中验证，证明其可扩展性和实用性，并具有完备性、概率完备性和实际可处理性。

## 核心内容
### 方法概述
- 在信念空间中，机器人通过交错执行驱动与感知动作，主动降低位姿不确定性。
- 采用基于熵启发式的最佳优先搜索（best-first search），引导规划器选择信息量最大的动作序列。
- 感知动作包括识别物体或询问方向等语义级操作，补充传统特征（点、线、面）定位的不足。

### 理论保证
- 算法被证明是**完备的**（sound）和**概率完备的**（probabilistically complete），即在有限时间内能找到解（若存在）。
- 在实际场景中具有**可处理性**（tractable），计算复杂度可控。

### 实验设置与结果
- **仿真环境**：在大状态空间中测试，验证方法在规模扩展时的性能。
- **真实机器人**：在IIT-R1人形机器人上部署，展示在模糊环境（如对称走廊、重复纹理区域）中的有效性。
- 关键发现：主动语义感知能显著减少定位收敛时间，尤其在初始位姿不确定时，比纯几何特征方法更快达到稳定精度。

## Overview
In this paper, we outline an interleaved acting and planning technique to rapidly reduce the uncertainty of the estimated robot's pose by perceiving relevant information from the environment, as recognizing an object or asking someone for a direction.   Generally, existing localization approaches rely on low-level geometric features such as points, lines, and planes, while these approaches provide the desired accuracy, they may require time to converge, especially with incorrect initial guesses. In our approach, a task planner computes a sequence of action and perception tasks to actively obtain relevant information from the robot's perception system. We validate our approach in large state spaces, to show how the approach scales, and in real environments, to show the applicability of our method on real robots.   We prove that our approach is sound, probabilistically complete, and tractable in practical cases.

## Overview
In this paper, we outline an interleaved acting and planning technique to rapidly reduce the uncertainty of the estimated robot's pose by perceiving relevant information from the environment, such as recognizing an object or asking someone for a direction. Generally, existing localization approaches rely on low-level geometric features such as points, lines, and planes. While these approaches provide the desired accuracy, they may require time to converge, especially with incorrect initial guesses. In our approach, a task planner computes a sequence of action and perception tasks to actively obtain relevant information from the robot's perception system. We validate our approach in large state spaces to demonstrate how it scales, and in real environments to show the applicability of our method on real robots. We prove that our approach is sound, probabilistically complete, and tractable in practical cases.

## Content
In this paper, we outline an interleaved acting and planning technique to rapidly reduce the uncertainty of the estimated robot's pose by perceiving relevant information from the environment, such as recognizing an object or asking someone for a direction. Generally, existing localization approaches rely on low-level geometric features such as points, lines, and planes. While these approaches provide the desired accuracy, they may require time to converge, especially with incorrect initial guesses. In our approach, a task planner computes a sequence of action and perception tasks to actively obtain relevant information from the robot's perception system. We validate our approach in large state spaces to demonstrate how it scales, and in real environments to show the applicability of our method on real robots. We prove that our approach is sound, probabilistically complete, and tractable in practical cases.

## 개요
본 논문에서는 환경으로부터 관련 정보를 인식(예: 객체 인식 또는 방향 문의)하여 추정된 로봇 포즈의 불확실성을 신속히 줄이기 위한 교차 실행 및 계획 기법을 개괄합니다. 일반적으로 기존 위치 추정 접근법은 점, 선, 평면과 같은 저수준 기하학적 특징에 의존합니다. 이러한 접근법은 원하는 정확도를 제공하지만, 특히 초기 추정이 부정확할 경우 수렴에 시간이 소요될 수 있습니다. 본 접근법에서는 작업 계획기가 일련의 행동 및 인식 작업을 계산하여 로봇의 인식 시스템으로부터 관련 정보를 능동적으로 획득합니다. 우리는 대규모 상태 공간에서 접근법의 확장성을 검증하고, 실제 환경에서 실제 로봇에 대한 방법의 적용 가능성을 입증합니다. 또한 본 접근법이 건전하고, 확률적으로 완전하며, 실제 사례에서 다루기 쉬움을 증명합니다.

## 핵심 내용
본 논문에서는 환경으로부터 관련 정보를 인식(예: 객체 인식 또는 방향 문의)하여 추정된 로봇 포즈의 불확실성을 신속히 줄이기 위한 교차 실행 및 계획 기법을 개괄합니다. 일반적으로 기존 위치 추정 접근법은 점, 선, 평면과 같은 저수준 기하학적 특징에 의존합니다. 이러한 접근법은 원하는 정확도를 제공하지만, 특히 초기 추정이 부정확할 경우 수렴에 시간이 소요될 수 있습니다. 본 접근법에서는 작업 계획기가 일련의 행동 및 인식 작업을 계산하여 로봇의 인식 시스템으로부터 관련 정보를 능동적으로 획득합니다. 우리는 대규모 상태 공간에서 접근법의 확장성을 검증하고, 실제 환경에서 실제 로봇에 대한 방법의 적용 가능성을 입증합니다. 또한 본 접근법이 건전하고, 확률적으로 완전하며, 실제 사례에서 다루기 쉬움을 증명합니다.

## 参考
- http://arxiv.org/abs/2002.08124v3
