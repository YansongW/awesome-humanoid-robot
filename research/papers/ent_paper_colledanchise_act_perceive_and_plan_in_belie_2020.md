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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2002.08124v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (597 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2002.08124v3

## 개요
기존 위치 추정 방법은 점, 선, 면과 같은 저수준 기하학적 특징에 의존하며, 정확도는 높지만 초기 추정이 부정확할 때 수렴이 느리다. 본 논문은 교차 실행 및 계획 프레임워크를 제안하며, 작업 계획기가 동작 및 인식 작업 시퀀스를 계산하여 객체 인식이나 방향 질문과 같은 정보를 환경에서 능동적으로 획득한다. 이 방법은 대규모 상태 공간과 실제 환경에서 검증되어 확장성과 실용성을 입증하며, 완전성, 확률적 완전성 및 실제 처리 가능성을 갖춘다.

## 핵심 내용
### 방법 개요
- 신념 공간에서 로봇은 구동 및 인식 동작을 교차 실행하며 위치 불확실성을 능동적으로 줄인다.
- 엔트로피 기반 휴리스틱을 사용한 최상 우선 탐색(best-first search)을 채택하여, 계획기가 가장 정보량이 큰 동작 시퀀스를 선택하도록 유도한다.
- 인식 동작에는 객체 인식이나 방향 질문과 같은 의미론적 수준의 작업이 포함되어, 전통적인 특징(점, 선, 면) 기반 위치 추정의 한계를 보완한다.

### 이론적 보장
- 알고리즘은 **완전성**(sound)과 **확률적 완전성**(probabilistically complete)을 갖는 것으로 증명되었으며, 즉 유한 시간 내에 해를 찾을 수 있다(존재하는 경우).
- 실제 시나리오에서 **처리 가능성**(tractable)을 가지며, 계산 복잡도가 통제 가능하다.

### 실험 설정 및 결과
- **시뮬레이션 환경**: 대규모 상태 공간에서 테스트하여 규모 확장 시 성능을 검증한다.
- **실제 로봇**: IIT-R1 휴머노이드 로봇에 배포하여 대칭 복도, 반복 텍스처 영역과 같은 모호한 환경에서의 효과를 보여준다.
- 주요 발견: 능동적 의미 인식은 특히 초기 위치 불확실성이 클 때 위치 추정 수렴 시간을 크게 줄이며, 순수 기하학적 특징 방법보다 더 빠르게 안정적인 정확도에 도달한다.
