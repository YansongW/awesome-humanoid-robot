---
$id: ent_paper_khazoom_tailoring_solution_accuracy_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Tailoring Solution Accuracy for Fast Whole-body Model Predictive Control of Legged Robots
  zh: 针对腿式机器人快速全身模型预测控制的求解精度定制
  ko: 족보 로봇을 위한 고속 전신 모델 예측 제어의 해 정확도 조정
summary:
  en: Presents a whole-body nonlinear model predictive control framework that uses one SQP iteration per control step with
    an ADMM-based QP solver to achieve real-time rates on the MIT Humanoid, and enforces self-collision constraints via control
    barrier functions at the initial timestep.
  zh: 本文提出一种用于腿式机器人的全身非线性模型预测控制框架，通过每控制步仅执行一次SQP迭代并采用基于ADMM的QP求解器，在MIT Humanoid上实现了实时控制。该框架利用初始时间步的控制障碍函数强制执行自碰撞约束，将自碰撞次数降低26倍，同时支持复杂腿部交叉和手臂运动以增强行走稳定性。
  ko: ADMM 기반 QP 솔버를 사용하여 제어 단계당 하나의 SQP 반복으로 전신 비선형 모델 예측 제어 프레임워크를 제시하여 MIT 휴머노이드에서 실시간 속도를 달성하고, 초기 시간 단계에서 제어 장벽 함수를 통해
    자기 충돌 제약을 강제합니다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- model_predictive_control
- nonlinear_mpc
- whole_body_control
- legged_robots
- admm
- qp_solver
- osqp
- control_barrier_functions
- self_collision_avoidance
- mit_humanoid
- real_time_control
- sequential_quadratic_programming
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.10789v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (846 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Tailoring Solution Accuracy for Fast Whole-body Model Predictive Control of Legged Robots
  url: https://arxiv.org/abs/2407.10789
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3455907
theoretical_depth:
- method
---
## 概述
针对高维系统实时不等式约束的挑战，该研究放弃追求高精度最优解，转而采用交替方向乘子法快速生成低精度二次规划子问题解。仿真与硬件实验表明，由于动力学离散化误差、惯性建模误差和延迟，真实机器人往往无法从高精度解中获益。控制器在90 Hz频率下稳定运行，处理包含32个时间步、2004个变量和3768个约束的问题，使MIT Humanoid能够规划复杂的交叉腿和手臂动作，在行走和抵抗大扰动时提升稳定性。

## 核心内容
### 方法架构
- 采用**单次SQP迭代**（sequential quadratic programming）每控制步，结合**ADMM**（alternating direction method of multipliers）求解QP子问题，避免传统多迭代方案的计算瓶颈。
- 在NMPC初始时间步嵌入**控制障碍函数（CBF）**处理自碰撞约束，无需额外计算开销即可实现约束满足。

### 实验设置
- 硬件平台：MIT Humanoid，控制频率90 Hz。
- 问题规模：32个预测时间步，2004个优化变量，3768个约束条件。
- 对比基线：高精度NMPC求解器（多迭代收敛方案）。

### 关键发现
- **精度-实用性权衡**：高精度解因动力学离散化误差（discretization errors）、惯性建模误差（inertial modeling errors）和系统延迟（delays）无法提升实际机器人性能，低精度解反而更鲁棒。
- **自碰撞约束效果**：CBF方法使自碰撞次数减少**26倍**，且未增加计算负担。
- **运动能力提升**：控制器支持复杂交叉腿（crossed-leg）和手臂（arm）动作规划，显著增强行走稳定性及大扰动恢复能力（如推搡后快速调整姿态）。

### 结论
该工作证明在全身NMPC中主动牺牲求解精度可换取实时性，同时通过CBF高效处理安全约束，为高维腿式机器人的实时控制提供了可行方案。

## Overview
Thanks to recent advancements in accelerating non-linear model predictive control (NMPC), it is now feasible to deploy whole-body NMPC at real-time rates for humanoid robots. However, enforcing inequality constraints in real time for such high-dimensional systems remains challenging due to the need for additional iterations. This paper presents an implementation of whole-body NMPC for legged robots that provides low-accuracy solutions to NMPC with general equality and inequality constraints. Instead of aiming for highly accurate optimal solutions, we leverage the alternating direction method of multipliers to rapidly provide low-accuracy solutions to quadratic programming subproblems. Our extensive simulation results indicate that real robots often cannot benefit from highly accurate solutions due to dynamics discretization errors, inertial modeling errors and delays. We incorporate control barrier functions (CBFs) at the initial timestep of the NMPC for the self-collision constraints, resulting in up to a 26-fold reduction in the number of self-collisions without adding computational burden. The controller is reliably deployed on hardware at 90 Hz for a problem involving 32 timesteps, 2004 variables, and 3768 constraints. The NMPC delivers sufficiently accurate solutions, enabling the MIT Humanoid to plan complex crossed-leg and arm motions that enhance stability when walking and recovering from significant disturbances.

## 参考
- http://arxiv.org/abs/2407.10789v2

## 개요
고차원 시스템의 실시간 부등식 제약 조건 문제를 해결하기 위해, 본 연구는 높은 정밀도의 최적해를 추구하는 대신 교대 방향 승수법(ADMM)을 사용하여 저정밀도 2차 계획법(QP) 하위 문제 해를 빠르게 생성하는 방식을 채택한다. 시뮬레이션 및 하드웨어 실험은 동역학 이산화 오차, 관성 모델링 오차 및 지연으로 인해 실제 로봇이 고정밀도 해로부터 이점을 얻지 못하는 경우가 많음을 보여준다. 제어기는 90Hz 주파수에서 안정적으로 작동하며, 32개의 시간 스텝, 2004개의 변수, 3768개의 제약 조건을 포함하는 문제를 처리하여 MIT 휴머노이드가 복잡한 다리 교차 및 팔 동작을 계획하고, 보행 및 큰 외란 저항 시 안정성을 향상시킬 수 있게 한다.

## 핵심 내용
### 방법 아키텍처
- 각 제어 스텝마다 **단일 SQP 반복**(순차 2차 계획법)을 채택하고, **ADMM**(교대 방향 승수법)을 사용하여 QP 하위 문제를 해결함으로써 기존 다중 반복 방식의 계산 병목 현상을 피한다.
- NMPC 초기 시간 스텝에 **제어 장벽 함수(CBF)**를 내장하여 자체 충돌 제약 조건을 처리하며, 추가 계산 비용 없이 제약 조건 충족을 달성한다.

### 실험 설정
- 하드웨어 플랫폼: MIT 휴머노이드, 제어 주파수 90Hz.
- 문제 규모: 32개의 예측 시간 스텝, 2004개의 최적화 변수, 3768개의 제약 조건.
- 비교 기준: 고정밀도 NMPC 솔버(다중 반복 수렴 방식).

### 주요 발견
- **정밀도-실용성 절충**: 고정밀도 해는 동역학 이산화 오차(discretization errors), 관성 모델링 오차(inertial modeling errors) 및 시스템 지연(delays)으로 인해 실제 로봇 성능을 향상시키지 못하며, 저정밀도 해가 오히려 더 강건하다.
- **자체 충돌 제약 효과**: CBF 방법은 자체 충돌 횟수를 **26배** 줄였으며, 계산 부담은 증가하지 않았다.
- **운동 능력 향상**: 제어기는 복잡한 다리 교차(crossed-leg) 및 팔(arm) 동작 계획을 지원하여 보행 안정성과 큰 외란 회복 능력(예: 밀림 후 빠른 자세 조정)을 크게 향상시킨다.

### 결론
본 연구는 전신 NMPC에서 해의 정밀도를 능동적으로 희생하여 실시간성을 확보할 수 있음을 입증하고, CBF를 통해 안전 제약 조건을 효율적으로 처리함으로써 고차원 보행 로봇의 실시간 제어를 위한 실현 가능한 방안을 제시한다.
