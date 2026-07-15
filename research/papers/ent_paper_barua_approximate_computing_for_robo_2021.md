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
  zh: Approximate computing is a computation domain which can be used to trade time and energy with quality and therefore
    is useful in embedded systems. Energy is the prime resource in battery-driven embedded systems, like robots. Approximate
    computing can be used as a technique to generate approximate version of the control functionalities of a robot, enabling
    it to ration energy for computation at the cost of degraded quality. Usually, the programmer of the function specifies
    the extent of degradation that is safe for the overall safety of the system. However, in a collaborative environment,
    where
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.05773v2.
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
Approximate computing is a computation domain which can be used to trade time and energy with quality and therefore is useful in embedded systems. Energy is the prime resource in battery-driven embedded systems, like robots. Approximate computing can be used as a technique to generate approximate version of the control functionalities of a robot, enabling it to ration energy for computation at the cost of degraded quality. Usually, the programmer of the function specifies the extent of degradation that is safe for the overall safety of the system. However, in a collaborative environment, where several sub-systems co-exist and some of the functionality of each of them have been approximated, the safety of the overall system may be compromised. In this paper, we consider multiple identical robots operate in a warehouse, and the path planning function of the robot is approximated. Although the planned paths are safe for individual robots (i.e. they do not collide with the racks), we show that this leads to a collision among the robots. So, a controlled approximation needs to be carried out in such situations to harness the full power of this new paradigm if it needs to be a mainstream paradigm in future.

## 核心内容
Approximate computing is a computation domain which can be used to trade time and energy with quality and therefore is useful in embedded systems. Energy is the prime resource in battery-driven embedded systems, like robots. Approximate computing can be used as a technique to generate approximate version of the control functionalities of a robot, enabling it to ration energy for computation at the cost of degraded quality. Usually, the programmer of the function specifies the extent of degradation that is safe for the overall safety of the system. However, in a collaborative environment, where several sub-systems co-exist and some of the functionality of each of them have been approximated, the safety of the overall system may be compromised. In this paper, we consider multiple identical robots operate in a warehouse, and the path planning function of the robot is approximated. Although the planned paths are safe for individual robots (i.e. they do not collide with the racks), we show that this leads to a collision among the robots. So, a controlled approximation needs to be carried out in such situations to harness the full power of this new paradigm if it needs to be a mainstream paradigm in future.

## 参考
- http://arxiv.org/abs/2104.05773v2


