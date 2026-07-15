---
$id: ent_paper_wang_adaptive_control_of_robot_mani_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics
  zh: 具有不确定运动学和动力学的机器人机械臂自适应控制
  ko: 불확실한 기구학과 동역학을 가진 로봇 매니퓰레이터의 적응 제어
summary:
  en: This paper proposes two adaptive control schemes that achieve task-space trajectory tracking for robot manipulators
    when both kinematic and dynamic parameters are uncertain, using inverse-Jacobian feedback with separated adaptation loops.
  zh: In this paper, we investigate the adaptive control problem for robot manipulators with both the uncertain kinematics
    and dynamics. We propose two adaptive control schemes to realize the objective of task-space trajectory tracking irrespective
    of the uncertain kinematics and dynamics. The proposed controllers have the desirable separation property, and we also
    show that the first adaptive controller with appropriate modifications can yield improved performance, without the expense
    of conservative gain choice. The performance of the proposed controllers is shown by numerical simulations.
  ko: 본 논문은 운동학적 및 동역학적 매개변수가 모두 불확실한 로봇 매니퓰레이터의 작업 공간 궤적 추적을 분리된 적응 루프와 역-야코비안 피드백을 사용하여 달성하는 두 가지 적응 제어 기법을 제안한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- adaptive_control
- task_space_tracking
- uncertain_kinematics
- uncertain_dynamics
- robot_manipulator
- inverse_jacobian_feedback
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1403.5204v3.
sources:
- id: src_001
  type: paper
  title: Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics
  url: https://arxiv.org/abs/1403.5204
  date: '2014'
  accessed_at: '2026-06-26'
---

## 概述
In this paper, we investigate the adaptive control problem for robot manipulators with both the uncertain kinematics and dynamics. We propose two adaptive control schemes to realize the objective of task-space trajectory tracking irrespective of the uncertain kinematics and dynamics. The proposed controllers have the desirable separation property, and we also show that the first adaptive controller with appropriate modifications can yield improved performance, without the expense of conservative gain choice. The performance of the proposed controllers is shown by numerical simulations.

## 核心内容
In this paper, we investigate the adaptive control problem for robot manipulators with both the uncertain kinematics and dynamics. We propose two adaptive control schemes to realize the objective of task-space trajectory tracking irrespective of the uncertain kinematics and dynamics. The proposed controllers have the desirable separation property, and we also show that the first adaptive controller with appropriate modifications can yield improved performance, without the expense of conservative gain choice. The performance of the proposed controllers is shown by numerical simulations.

## 参考
- http://arxiv.org/abs/1403.5204v3


