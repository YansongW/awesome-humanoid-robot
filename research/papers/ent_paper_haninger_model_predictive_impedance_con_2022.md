---
$id: ent_paper_haninger_model_predictive_impedance_con_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Model Predictive Impedance Control with Gaussian Processes for Human and Environment Interaction
  zh: 基于高斯过程的人与环境交互模型预测阻抗控制
  ko: 인간 및 환경 상호작용을 위한 가우시안 프로세스 기반 모델 예측 임피던스 제어
summary:
  en: This paper proposes a nonlinear model predictive control framework that jointly optimizes robot trajectory and impedance
    online. It learns uncertainty-aware task models from a few demonstrations using Gaussian Processes and handles discrete
    and continuous uncertainties in physical human-robot interaction tasks such as co-manipulation, polishing, and assembly.
  zh: 本文提出一种非线性模型预测控制框架，可在线联合优化机器人轨迹与阻抗。该框架利用高斯过程从少量演示中学习不确定性感知任务模型，并处理物理人机交互任务（如协同操作、抛光、装配）中的离散与连续不确定性。
  ko: 본 논문은 로봇 궤적과 임피던스를 온라인으로 공동 최적화하는 비선형 모델 예측 제어 프레임워크를 제안한다. 소량의 시연으로부터 가우시안 프로세스를 이용해 불확실성 인식 작업 모델을 학습하고, 공동 조작, 폴리싱,
    조립 등의 물리적 인간-로봇 상호작용 작업에서 이산 및 연속 불확실성을 처리한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 04_assembly_integration_testing
- 03_manufacturing_processes
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- model_predictive_control
- impedance_control
- gaussian_processes
- human_robot_interaction
- physical_interaction
- learning_from_demonstration
- trajectory_optimization
- contact_stability
- uncertainty_modeling
- co_manipulation
- collaborative_assembly
- collaborative_polishing
- admittance_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2208.07035v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (746 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Model Predictive Impedance Control with Gaussian Processes for Human and Environment Interaction
  url: https://arxiv.org/abs/2208.07035
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
现有方法通常孤立处理机器人轨迹或阻抗的适应性调整，无法应对多种不确定性并存的任务。本文提出的MPC框架能同时规划轨迹与阻抗，考虑离散与连续不确定性，包含安全约束，并高效适应新任务。该框架通过高斯过程从不超过3次演示中学习不确定性感知任务模型，并在非线性MPC问题中优化机器人轨迹与阻抗，依据对人类目标、运动学、安全约束、接触稳定性和频域扰动抑制的信念进行决策。该公式被引入、分析凸性，并在多目标协同操作、协作抛光与装配任务中验证。

## 核心内容
### 方法
- 提出一种非线性模型预测控制（MPC）框架，在线联合优化机器人轨迹与阻抗。
- 利用高斯过程（Gaussian Processes）从少量（≤3次）演示中学习不确定性感知任务模型。
- 该框架可处理多种不确定性来源：接触约束变化、人类目标不确定性、任务扰动。

### 架构
- MPC问题包含：基于对人类离散目标的信念、人类运动学、安全约束、接触稳定性、频域扰动抑制的优化。
- 轨迹与阻抗作为决策变量，在非线性优化中同时求解。

### 实验设置
- 验证任务：多目标协同操作（co-manipulation with multiple goals）、协作抛光（collaborative polishing）、协作装配（collaborative assembly）。
- 演示次数：每个任务不超过3次。

### 关键数字
- 演示次数：≤3次。
- 不确定性类型：离散（人类目标）与连续（接触约束、扰动）。
- 安全约束：显式包含在MPC公式中。

### 结论
- 该框架能有效处理物理人机交互中的多种不确定性，提升任务适应性与安全性。
- 通过凸性分析确保优化问题的可解性，并在实际任务中验证了性能。

## Overview
Robotic tasks which involve uncertainty--due to variation in goal, environment configuration, or confidence in task model--may require human input to instruct or adapt the robot. In tasks with physical contact, several existing methods for adapting robot trajectory or impedance according to individual uncertainties have been proposed, e.g., realizing intention detection or uncertainty-aware learning from demonstration. However, isolated methods cannot address the wide range of uncertainties jointly present in many tasks.   To improve generality, this paper proposes a model predictive control (MPC) framework which plans both trajectory and impedance online, can consider discrete and continuous uncertainties, includes safety constraints, and can be efficiently applied to a new task. This framework can consider uncertainty from: contact constraint variation, uncertainty in human goals, or task disturbances. An uncertainty-aware task model is learned from a few ($\leq3$) demonstrations using Gaussian Processes. This task model is used in a nonlinear MPC problem to optimize robot trajectory and impedance according to belief in discrete human goals, human kinematics, safety constraints, contact stability, and frequency-domain disturbance rejection. This MPC formulation is introduced, analyzed with respect to convexity, and validated in co-manipulation with multiple goals, a collaborative polishing task, and a collaborative assembly task.

## 参考
- http://arxiv.org/abs/2208.07035v2

## 개요
기존 방법들은 일반적으로 로봇 궤적 또는 임피던스의 적응적 조정을 개별적으로 처리하여, 여러 불확실성이 공존하는 작업에는 대응할 수 없습니다. 본 논문에서 제안하는 MPC 프레임워크는 궤적과 임피던스를 동시에 계획하고, 이산적 및 연속적 불확실성을 고려하며, 안전 제약을 포함하고, 새로운 작업에 효율적으로 적응할 수 있습니다. 이 프레임워크는 가우시안 프로세스를 통해 3회 이하의 시연에서 불확실성 인식 작업 모델을 학습하고, 비선형 MPC 문제에서 로봇 궤적과 임피던스를 최적화하며, 인간의 목표, 운동학, 안전 제약, 접촉 안정성 및 주파수 영역 외란 억제에 대한 신념을 기반으로 결정을 내립니다. 이 공식은 도입되고, 볼록성이 분석되며, 다중 목표 협동 조작, 협동 연마 및 조립 작업에서 검증됩니다.

## 핵심 내용
### 방법
- 비선형 모델 예측 제어(MPC) 프레임워크를 제안하여, 로봇 궤적과 임피던스를 온라인으로 동시에 최적화합니다.
- 가우시안 프로세스(Gaussian Processes)를 활용하여 소량(≤3회)의 시연에서 불확실성 인식 작업 모델을 학습합니다.
- 이 프레임워크는 접촉 제약 변화, 인간 목표 불확실성, 작업 외란 등 다양한 불확실성 원인을 처리할 수 있습니다.

### 구조
- MPC 문제는 인간의 이산적 목표에 대한 신념, 인간 운동학, 안전 제약, 접촉 안정성, 주파수 영역 외란 억제에 기반한 최적화를 포함합니다.
- 궤적과 임피던스는 결정 변수로 설정되어 비선형 최적화에서 동시에 해결됩니다.

### 실험 설정
- 검증 작업: 다중 목표 협동 조작(co-manipulation with multiple goals), 협동 연마(collaborative polishing), 협동 조립(collaborative assembly).
- 시연 횟수: 각 작업당 3회 이하.

### 주요 수치
- 시연 횟수: ≤3회.
- 불확실성 유형: 이산적(인간 목표) 및 연속적(접촉 제약, 외란).
- 안전 제약: MPC 공식에 명시적으로 포함됨.

### 결론
- 이 프레임워크는 물리적 인간-로봇 상호작용에서 발생하는 다양한 불확실성을 효과적으로 처리하며, 작업 적응성과 안전성을 향상시킵니다.
- 볼록성 분석을 통해 최적화 문제의 해결 가능성을 보장하고, 실제 작업에서 성능을 검증했습니다.
