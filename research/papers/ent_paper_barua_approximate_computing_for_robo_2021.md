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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.05773v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
근사 컴퓨팅(Approximate computing)은 시간과 에너지를 품질과 교환할 수 있는 계산 영역으로, 따라서 임베디드 시스템에서 유용합니다. 에너지는 로봇과 같은 배터리 구동 임베디드 시스템에서 주요 자원입니다. 근사 컴퓨팅은 로봇의 제어 기능에 대한 근사 버전을 생성하는 기술로 사용될 수 있으며, 품질 저하를 대가로 계산에 필요한 에너지를 절약할 수 있게 합니다. 일반적으로 기능의 프로그래머는 시스템 전체 안전에 무해한 성능 저하 정도를 지정합니다. 그러나 여러 하위 시스템이 공존하고 각각의 일부 기능이 근사화된 협업 환경에서는 전체 시스템의 안전이 손상될 수 있습니다. 본 논문에서는 창고에서 여러 대의 동일한 로봇이 작동하고 로봇의 경로 계획 기능이 근사화된 경우를 고려합니다. 계획된 경로가 개별 로봇에 대해 안전하더라도(즉, 랙과 충돌하지 않음), 이로 인해 로봇 간 충돌이 발생함을 보여줍니다. 따라서 이러한 상황에서는 이 새로운 패러다임이 미래에 주류가 되기 위해 그 전체 잠재력을 활용하려면 제어된 근사화가 수행되어야 합니다.

## 핵심 내용
근사 컴퓨팅(Approximate computing)은 시간과 에너지를 품질과 교환할 수 있는 계산 영역으로, 따라서 임베디드 시스템에서 유용합니다. 에너지는 로봇과 같은 배터리 구동 임베디드 시스템에서 주요 자원입니다. 근사 컴퓨팅은 로봇의 제어 기능에 대한 근사 버전을 생성하는 기술로 사용될 수 있으며, 품질 저하를 대가로 계산에 필요한 에너지를 절약할 수 있게 합니다. 일반적으로 기능의 프로그래머는 시스템 전체 안전에 무해한 성능 저하 정도를 지정합니다. 그러나 여러 하위 시스템이 공존하고 각각의 일부 기능이 근사화된 협업 환경에서는 전체 시스템의 안전이 손상될 수 있습니다. 본 논문에서는 창고에서 여러 대의 동일한 로봇이 작동하고 로봇의 경로 계획 기능이 근사화된 경우를 고려합니다. 계획된 경로가 개별 로봇에 대해 안전하더라도(즉, 랙과 충돌하지 않음), 이로 인해 로봇 간 충돌이 발생함을 보여줍니다. 따라서 이러한 상황에서는 이 새로운 패러다임이 미래에 주류가 되기 위해 그 전체 잠재력을 활용하려면 제어된 근사화가 수행되어야 합니다.

## 参考
- http://arxiv.org/abs/2104.05773v2
