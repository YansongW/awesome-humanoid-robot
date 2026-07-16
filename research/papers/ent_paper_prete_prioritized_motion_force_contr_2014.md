---
$id: ent_paper_prete_prioritized_motion_force_contr_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Prioritized Motion-Force Control of Constrained Fully-Actuated Robots: "Task Space Inverse Dynamics"'
  zh: 受约束全驱动机器人的优先级运动-力控制：“任务空间逆动力学”
  ko: '구속된 완전 구동 로봇의 우선순위 운동-힘 제어: “작업 공간 역역학”'
summary:
  en: Introduces Task Space Inverse Dynamics (TSID), an optimal whole-body torque control framework for fully-actuated robots
    that decouples acceleration-level inverse kinematics from joint-space inverse dynamics to support prioritized motion/force
    control with soft and rigid contacts.
  zh: 提出任务空间逆动力学（TSID），一种面向全驱动机器人的最优全身力矩控制框架，通过将加速度级逆运动学与关节空间逆动力学解耦，支持柔性和刚性接触下的优先级运动/力控制。
  ko: 가속도 수준 역기구학과 관절 공간 역역학을 분리하여 부드러운 접촉과 경성 접촉이 있는 우선순위 운동/힘 제어를 지원하는 완전 구동 로봇을 위한 최적 전신 토크 제어 프레임워크인 작업 공간 역역학(TSID)을
    제안한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- whole_body_control
- task_space_inverse_dynamics
- operational_space_inverse_dynamics
- inverse_dynamics
- motion_force_control
- prioritized_control
- contact_dynamics
- fully_actuated_robots
- torque_control
- humanoid_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1410.3863v1.
sources:
- id: src_001
  type: paper
  title: 'Prioritized Motion-Force Control of Constrained Fully-Actuated Robots: "Task Space Inverse Dynamics"'
  url: https://arxiv.org/abs/1410.3863
  date: '2014'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
We present a new framework for prioritized multi-task motion-force control of fully-actuated robots. This work is established on a careful review and comparison of the state of the art. Some control frameworks are not optimal, that is they do not find the optimal solution for the secondary tasks. Other frameworks are optimal, but they tackle the control problem at kinematic level, hence they neglect the robot dynamics and they do not allow for force control. Still other frameworks are optimal and consider force control, but they are computationally less efficient than ours. Our final claim is that, for fully-actuated robots, computing the operational-space inverse dynamics is equivalent to computing the inverse kinematics (at acceleration level) and then the joint-space inverse dynamics. Thanks to this fact, our control framework can efficiently compute the optimal solution by decoupling kinematics and dynamics of the robot. We take into account: motion and force control, soft and rigid contacts, free and constrained robots. Tests in simulation validate our control framework, comparing it with other state-of-the-art equivalent frameworks and showing remarkable improvements in optimality and efficiency.

## 核心内容
We present a new framework for prioritized multi-task motion-force control of fully-actuated robots. This work is established on a careful review and comparison of the state of the art. Some control frameworks are not optimal, that is they do not find the optimal solution for the secondary tasks. Other frameworks are optimal, but they tackle the control problem at kinematic level, hence they neglect the robot dynamics and they do not allow for force control. Still other frameworks are optimal and consider force control, but they are computationally less efficient than ours. Our final claim is that, for fully-actuated robots, computing the operational-space inverse dynamics is equivalent to computing the inverse kinematics (at acceleration level) and then the joint-space inverse dynamics. Thanks to this fact, our control framework can efficiently compute the optimal solution by decoupling kinematics and dynamics of the robot. We take into account: motion and force control, soft and rigid contacts, free and constrained robots. Tests in simulation validate our control framework, comparing it with other state-of-the-art equivalent frameworks and showing remarkable improvements in optimality and efficiency.

## 参考
- http://arxiv.org/abs/1410.3863v1

## Overview
We present a new framework for prioritized multi-task motion-force control of fully-actuated robots. This work is established on a careful review and comparison of the state of the art. Some control frameworks are not optimal, that is they do not find the optimal solution for the secondary tasks. Other frameworks are optimal, but they tackle the control problem at kinematic level, hence they neglect the robot dynamics and they do not allow for force control. Still other frameworks are optimal and consider force control, but they are computationally less efficient than ours. Our final claim is that, for fully-actuated robots, computing the operational-space inverse dynamics is equivalent to computing the inverse kinematics (at acceleration level) and then the joint-space inverse dynamics. Thanks to this fact, our control framework can efficiently compute the optimal solution by decoupling kinematics and dynamics of the robot. We take into account: motion and force control, soft and rigid contacts, free and constrained robots. Tests in simulation validate our control framework, comparing it with other state-of-the-art equivalent frameworks and showing remarkable improvements in optimality and efficiency.

## Content
We present a new framework for prioritized multi-task motion-force control of fully-actuated robots. This work is established on a careful review and comparison of the state of the art. Some control frameworks are not optimal, that is they do not find the optimal solution for the secondary tasks. Other frameworks are optimal, but they tackle the control problem at kinematic level, hence they neglect the robot dynamics and they do not allow for force control. Still other frameworks are optimal and consider force control, but they are computationally less efficient than ours. Our final claim is that, for fully-actuated robots, computing the operational-space inverse dynamics is equivalent to computing the inverse kinematics (at acceleration level) and then the joint-space inverse dynamics. Thanks to this fact, our control framework can efficiently compute the optimal solution by decoupling kinematics and dynamics of the robot. We take into account: motion and force control, soft and rigid contacts, free and constrained robots. Tests in simulation validate our control framework, comparing it with other state-of-the-art equivalent frameworks and showing remarkable improvements in optimality and efficiency.

## 개요
본 논문은 완전 구동 로봇의 우선순위 기반 다중 작업 운동-힘 제어를 위한 새로운 프레임워크를 제시합니다. 이 연구는 최신 기술에 대한 면밀한 검토 및 비교를 바탕으로 수립되었습니다. 일부 제어 프레임워크는 최적이 아닙니다. 즉, 보조 작업에 대한 최적의 해를 찾지 못합니다. 다른 프레임워크는 최적이지만 운동학적 수준에서 제어 문제를 다루므로 로봇 동역학을 무시하고 힘 제어를 허용하지 않습니다. 또 다른 프레임워크는 최적이며 힘 제어를 고려하지만, 계산 효율성 측면에서 우리의 프레임워크보다 떨어집니다. 우리의 최종 주장은 완전 구동 로봇의 경우, 작업 공간 역동역학을 계산하는 것이 (가속도 수준에서) 역기구학을 계산한 후 관절 공간 역동역학을 계산하는 것과 동일하다는 것입니다. 이 사실 덕분에 우리의 제어 프레임워크는 로봇의 운동학과 동역학을 분리하여 최적의 해를 효율적으로 계산할 수 있습니다. 우리는 운동 및 힘 제어, 연성 및 강성 접촉, 자유 및 구속 로봇을 고려합니다. 시뮬레이션 테스트를 통해 우리의 제어 프레임워크를 검증하고, 다른 최신 동등 프레임워크와 비교하여 최적성과 효율성에서 현저한 개선을 보여줍니다.

## 핵심 내용
본 논문은 완전 구동 로봇의 우선순위 기반 다중 작업 운동-힘 제어를 위한 새로운 프레임워크를 제시합니다. 이 연구는 최신 기술에 대한 면밀한 검토 및 비교를 바탕으로 수립되었습니다. 일부 제어 프레임워크는 최적이 아닙니다. 즉, 보조 작업에 대한 최적의 해를 찾지 못합니다. 다른 프레임워크는 최적이지만 운동학적 수준에서 제어 문제를 다루므로 로봇 동역학을 무시하고 힘 제어를 허용하지 않습니다. 또 다른 프레임워크는 최적이며 힘 제어를 고려하지만, 계산 효율성 측면에서 우리의 프레임워크보다 떨어집니다. 우리의 최종 주장은 완전 구동 로봇의 경우, 작업 공간 역동역학을 계산하는 것이 (가속도 수준에서) 역기구학을 계산한 후 관절 공간 역동역학을 계산하는 것과 동일하다는 것입니다. 이 사실 덕분에 우리의 제어 프레임워크는 로봇의 운동학과 동역학을 분리하여 최적의 해를 효율적으로 계산할 수 있습니다. 우리는 운동 및 힘 제어, 연성 및 강성 접촉, 자유 및 구속 로봇을 고려합니다. 시뮬레이션 테스트를 통해 우리의 제어 프레임워크를 검증하고, 다른 최신 동등 프레임워크와 비교하여 최적성과 효율성에서 현저한 개선을 보여줍니다.
