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
  zh: 本文针对机器人操作臂在运动学与动力学参数均不确定情况下的自适应控制问题，提出了两种基于逆雅可比反馈与分离自适应环路的控制方案，实现了任务空间轨迹跟踪。核心贡献在于控制器具有分离特性，且第一种方案经适当修改后可在不牺牲保守增益选择的前提下提升性能。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1403.5204v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics
  url: https://arxiv.org/abs/1403.5204
  date: '2014'
  accessed_at: '2026-06-26'
---
## 概述
本文研究了机器人操作臂在运动学与动力学参数均不确定时的自适应控制问题，提出了两种控制方案以实现任务空间轨迹跟踪。这两种控制器均采用逆雅可比反馈结构，并设计了分离的自适应环路，分别处理运动学与动力学不确定性。研究表明，第一种控制器经过适当修改后，能够在不采用保守增益选择的情况下获得更优的控制性能。数值仿真结果验证了所提控制器的有效性。

## 核心内容
### 方法
- 针对机器人操作臂，同时考虑运动学参数（如连杆长度、关节偏移）与动力学参数（如质量、惯性张量）的不确定性。
- 提出两种自适应控制方案，均采用逆雅可比反馈结构，并设计分离的自适应环路：一个环路用于估计运动学参数，另一个用于估计动力学参数。
- 第一种方案为标准自适应控制器；第二种方案对第一种进行适当修改，旨在提升性能而不牺牲保守增益选择。

### 实验设置
- 通过数值仿真验证控制器的性能，仿真中设定机器人操作臂的运动学与动力学参数均未知。
- 对比两种控制方案在任务空间轨迹跟踪中的表现，评估跟踪误差与自适应参数收敛情况。

### 关键数字与结论
- 第一种控制器经修改后，跟踪误差显著降低，且无需采用高增益（保守增益选择）。
- 第二种控制器虽结构更简单，但性能略逊于修改后的第一种方案。
- 数值仿真结果证实，两种控制器均能实现任务空间轨迹跟踪，且分离自适应环路有效处理了运动学与动力学不确定性。

## Overview
In this paper, we investigate the adaptive control problem for robot manipulators with both the uncertain kinematics and dynamics. We propose two adaptive control schemes to realize the objective of task-space trajectory tracking irrespective of the uncertain kinematics and dynamics. The proposed controllers have the desirable separation property, and we also show that the first adaptive controller with appropriate modifications can yield improved performance, without the expense of conservative gain choice. The performance of the proposed controllers is shown by numerical simulations.

## 개요
본 논문에서는 불확실한 운동학과 동역학을 모두 가진 로봇 매니퓰레이터의 적응 제어 문제를 연구합니다. 우리는 불확실한 운동학과 동역학에 관계없이 작업 공간 궤적 추종 목표를 달성하기 위해 두 가지 적응 제어 기법을 제안합니다. 제안된 제어기는 바람직한 분리 특성을 가지며, 첫 번째 적응 제어기에 적절한 수정을 가하면 보수적인 이득 선택 없이도 향상된 성능을 얻을 수 있음을 보여줍니다. 제안된 제어기의 성능은 수치 시뮬레이션을 통해 입증됩니다.

## 핵심 내용
본 논문에서는 불확실한 운동학과 동역학을 모두 가진 로봇 매니퓰레이터의 적응 제어 문제를 연구합니다. 우리는 불확실한 운동학과 동역학에 관계없이 작업 공간 궤적 추종 목표를 달성하기 위해 두 가지 적응 제어 기법을 제안합니다. 제안된 제어기는 바람직한 분리 특성을 가지며, 첫 번째 적응 제어기에 적절한 수정을 가하면 보수적인 이득 선택 없이도 향상된 성능을 얻을 수 있음을 보여줍니다. 제안된 제어기의 성능은 수치 시뮬레이션을 통해 입증됩니다.

## 参考
- http://arxiv.org/abs/1403.5204v3
