---
$id: ent_paper_barua_approximate_computing_for_robo_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Approximate Computing for Robotic Path Planning: Experimentation, Case Study and Practical Implications'
  zh: 机器人路径规划中的近似计算：实验、案例研究与实际意义
  ko: '로봇 경로 계획을 위한 근사 컴퓨팅: 실험, 사례 연구 및 실용적 함의'
summary:
  en: This paper applies loop perforation to approximate the A* path planning algorithm for battery-driven mobile warehouse
    robots, and demonstrates that individually safe approximations can cause inter-robot collisions in collaborative multi-robot
    fleets.
  zh: 本文研究将近似计算中的循环穿孔技术应用于电池驱动的移动仓库机器人的A*路径规划算法，以节省能量。实验表明，虽然单个机器人的近似路径规划是安全的，但在多机器人协作场景中，这种独立安全近似会导致机器人之间的碰撞。研究揭示了在协作系统中进行受控近似的必要性。
  ko: 본 논문은 배터리 구동의 이동식 창고 로봇을 위한 A* 경로 계획 알고리즘을 근사화하기 위해 루프 퍼포레이션을 적용하고, 개별 로봇에게는 안전한 근사가 협업 다중 로봇 군집에서 로봇 간 충돌을 유발할 수 있음을
    보여준다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- approximate_computing
- loop_perforation
- a_star
- path_planning
- multi_robot_coordination
- energy_aware_control
- warehouse_robots
- safety
- graph_search
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.05773v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (745 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Approximate Computing for Robotic path planning - Experimentation, Case Study and Practical Implications
  url: https://arxiv.org/abs/2104.05773
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
本文聚焦于电池驱动的移动仓库机器人，利用近似计算中的循环穿孔技术对A*路径规划算法进行近似化处理，以在牺牲一定路径质量的前提下降低计算能耗。作者指出，在单机器人场景下，近似后的路径规划仍能保证机器人不与货架碰撞，即个体安全。然而，当多个这样的机器人协同工作时，每个机器人独立进行的“安全”近似路径规划，却可能导致机器人之间发生碰撞。因此，该研究强调，在协作多机器人系统中，必须对近似计算进行全局控制，才能在不牺牲系统整体安全性的前提下发挥其节能优势。

## 核心内容
### 研究背景与动机
- 近似计算是一种通过牺牲计算质量来换取时间和能量效率的技术，特别适用于电池驱动的嵌入式系统（如机器人）。
- 机器人控制功能的近似版本可以节省能量，但程序员通常需要设定一个“安全”的质量退化阈值，以确保单机安全。

### 方法与实验
- **核心方法**：采用循环穿孔（loop perforation）技术对A*路径规划算法进行近似。循环穿孔通过跳过部分循环迭代来加速计算，从而降低能耗。
- **实验场景**：模拟多个相同的移动机器人在仓库环境中运行，每个机器人使用近似后的A*算法规划路径。
- **关键发现**：
  - 在单机器人测试中，近似路径规划不会导致机器人撞上货架，即个体安全得到保证。
  - 在多机器人协作场景中，尽管每个机器人的路径对自身是安全的，但机器人之间的路径冲突未被考虑，导致相互碰撞。

### 结论与启示
- 个体安全的近似在协作系统中可能引发全局安全问题，因此需要“受控近似”（controlled approximation）。
- 未来若要将近似计算作为主流范式应用于机器人领域，必须开发能够协调多智能体近似行为的机制，以避免系统级风险。

## Overview
Approximate computing is a computation domain which can be used to trade time and energy with quality and therefore is useful in embedded systems. Energy is the prime resource in battery-driven embedded systems, like robots. Approximate computing can be used as a technique to generate approximate version of the control functionalities of a robot, enabling it to ration energy for computation at the cost of degraded quality. Usually, the programmer of the function specifies the extent of degradation that is safe for the overall safety of the system. However, in a collaborative environment, where several sub-systems co-exist and some of the functionality of each of them have been approximated, the safety of the overall system may be compromised. In this paper, we consider multiple identical robots operate in a warehouse, and the path planning function of the robot is approximated. Although the planned paths are safe for individual robots (i.e. they do not collide with the racks), we show that this leads to a collision among the robots. So, a controlled approximation needs to be carried out in such situations to harness the full power of this new paradigm if it needs to be a mainstream paradigm in future.

## 参考
- http://arxiv.org/abs/2104.05773v2

## 개요
본 논문은 배터리로 구동되는 이동형 창고 로봇에 초점을 맞추며, 근사 계산의 루프 천공(loop perforation) 기법을 활용하여 A* 경로 계획 알고리즘을 근사화함으로써, 일정 수준의 경로 품질을 희생하는 대신 계산 에너지를 절감하는 것을 목표로 한다. 저자는 단일 로봇 시나리오에서 근사화된 경로 계획이 여전히 로봇이 선반과 충돌하지 않도록 보장한다는 점, 즉 개체 안전성을 지적한다. 그러나 여러 대의 이러한 로봇이 협력하여 작업할 때, 각 로봇이 독립적으로 수행하는 "안전한" 근사 경로 계획은 로봇 간 충돌을 초래할 수 있다. 따라서 본 연구는 협력적 다중 로봇 시스템에서 시스템 전체의 안전성을 희생하지 않으면서 에너지 절감 이점을 활용하려면 근사 계산에 대한 전역적 제어가 필수적임을 강조한다.

## 핵심 내용
### 연구 배경 및 동기
- 근사 계산은 계산 품질을 희생하여 시간 및 에너지 효율성을 얻는 기술로, 배터리로 구동되는 임베디드 시스템(예: 로봇)에 특히 적합하다.
- 로봇 제어 기능의 근사 버전은 에너지를 절약할 수 있지만, 프로그래머는 일반적으로 단일 기계 안전성을 보장하기 위해 "안전한" 품질 저하 임계값을 설정해야 한다.

### 방법 및 실험
- **핵심 방법**: 루프 천공(loop perforation) 기법을 사용하여 A* 경로 계획 알고리즘을 근사화한다. 루프 천공은 일부 루프 반복을 건너뛰어 계산을 가속화함으로써 에너지 소비를 줄인다.
- **실험 시나리오**: 동일한 이동형 로봇 여러 대가 창고 환경에서 작동하는 상황을 시뮬레이션하며, 각 로봇은 근사화된 A* 알고리즘을 사용하여 경로를 계획한다.
- **주요 발견**:
  - 단일 로봇 테스트에서 근사 경로 계획은 로봇이 선반에 충돌하지 않도록 하여 개체 안전성이 보장된다.
  - 다중 로봇 협력 시나리오에서는 각 로봇의 경로가 자체적으로는 안전하지만, 로봇 간 경로 충돌이 고려되지 않아 상호 충돌이 발생한다.

### 결론 및 시사점
- 개체 안전 근사는 협력 시스템에서 전역적 안전 문제를 유발할 수 있으므로 "제어된 근사"(controlled approximation)가 필요하다.
- 향후 근사 계산을 로봇 분야의 주류 패러다임으로 적용하려면 시스템 수준의 위험을 피하기 위해 다중 에이전트의 근사 동작을 조정할 수 있는 메커니즘을 개발해야 한다.
