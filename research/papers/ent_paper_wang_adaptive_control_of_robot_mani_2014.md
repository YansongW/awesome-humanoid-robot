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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1403.5204v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: en/ko
    body retranslated from zh deep-read (596 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1403.5204v3

## Overview
This paper investigates the adaptive control problem for robotic manipulators when both kinematic and dynamic parameters are uncertain, and proposes two control schemes to achieve task-space trajectory tracking. Both controllers adopt an inverse Jacobian feedback structure and are designed with separate adaptive loops to handle kinematic and dynamic uncertainties, respectively. The study shows that the first controller, after appropriate modification, can achieve better control performance without adopting conservative gain selection. Numerical simulation results verify the effectiveness of the proposed controllers.

## Content
### Method
- For robotic manipulators, uncertainties in both kinematic parameters (such as link lengths, joint offsets) and dynamic parameters (such as mass, inertia tensor) are considered simultaneously.
- Two adaptive control schemes are proposed, both adopting an inverse Jacobian feedback structure and designed with separate adaptive loops: one loop for estimating kinematic parameters and another for estimating dynamic parameters.
- The first scheme is a standard adaptive controller; the second scheme appropriately modifies the first to aim at improving performance without sacrificing conservative gain selection.

### Experimental Setup
- The performance of the controllers is verified through numerical simulations, where both kinematic and dynamic parameters of the robotic manipulator are set as unknown.
- The performance of the two control schemes in task-space trajectory tracking is compared, evaluating tracking errors and convergence of adaptive parameters.

### Key Figures and Conclusions
- After modification, the first controller significantly reduces tracking errors without requiring high gains (conservative gain selection).
- Although the second controller has a simpler structure, its performance is slightly inferior to the modified first scheme.
- Numerical simulation results confirm that both controllers can achieve task-space trajectory tracking, and the separate adaptive loops effectively handle kinematic and dynamic uncertainties.

## 개요
본 논문은 로봇 조작기의 운동학적 및 동역학적 매개변수가 모두 불확실한 경우의 적응 제어 문제를 연구하며, 작업 공간 궤적 추적을 달성하기 위한 두 가지 제어 방안을 제안한다. 두 제어기는 모두 역 야코비 피드백 구조를 채택하고, 운동학적 및 동역학적 불확실성을 각각 처리하기 위해 분리된 적응 루프를 설계한다. 연구 결과, 첫 번째 제어기는 적절히 수정된 후 보수적 이득 선택을 사용하지 않고도 더 우수한 제어 성능을 얻을 수 있음을 보여준다. 수치 시뮬레이션 결과는 제안된 제어기의 유효성을 검증한다.

## 핵심 내용
### 방법
- 로봇 조작기를 대상으로 운동학적 매개변수(예: 링크 길이, 관절 오프셋)와 동역학적 매개변수(예: 질량, 관성 텐서)의 불확실성을 동시에 고려한다.
- 두 가지 적응 제어 방안을 제안하며, 모두 역 야코비 피드백 구조를 채택하고 분리된 적응 루프를 설계한다: 하나의 루프는 운동학적 매개변수를 추정하고, 다른 하나는 동역학적 매개변수를 추정한다.
- 첫 번째 방안은 표준 적응 제어기이며, 두 번째 방안은 첫 번째를 적절히 수정하여 보수적 이득 선택을 희생하지 않으면서 성능을 향상시키는 것을 목표로 한다.

### 실험 설정
- 수치 시뮬레이션을 통해 제어기 성능을 검증하며, 시뮬레이션에서는 로봇 조작기의 운동학적 및 동역학적 매개변수가 모두 알려지지 않은 것으로 설정한다.
- 두 제어 방안의 작업 공간 궤적 추적 성능을 비교하고, 추적 오차와 적응 매개변수 수렴을 평가한다.

### 주요 수치 및 결론
- 첫 번째 제어기를 수정한 후 추적 오차가 현저히 감소하며, 높은 이득(보수적 이득 선택)을 사용할 필요가 없다.
- 두 번째 제어기는 구조가 더 간단하지만 성능은 수정된 첫 번째 방안보다 다소 떨어진다.
- 수치 시뮬레이션 결과는 두 제어기가 모두 작업 공간 궤적 추적을 달성할 수 있으며, 분리된 적응 루프가 운동학적 및 동역학적 불확실성을 효과적으로 처리함을 확인한다.
