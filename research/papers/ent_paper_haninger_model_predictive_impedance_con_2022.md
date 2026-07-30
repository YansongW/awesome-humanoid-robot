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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2208.07035v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
목표의 변동, 환경 구성의 변화, 또는 작업 모델에 대한 신뢰도 차이로 인해 불확실성이 수반되는 로봇 작업은 로봇을 지시하거나 적응시키기 위해 인간의 입력이 필요할 수 있습니다. 물리적 접촉이 있는 작업에서는 개별 불확실성에 따라 로봇의 궤적이나 임피던스를 적응시키는 여러 기존 방법이 제안되었습니다. 예를 들어, 의도 감지 또는 시연을 통한 불확실성 인식 학습이 있습니다. 그러나 개별적인 방법만으로는 많은 작업에서 공동으로 존재하는 다양한 불확실성을 처리할 수 없습니다. 일반성을 향상시키기 위해, 본 논문은 궤적과 임피던스를 온라인으로 계획하고, 이산적 및 연속적 불확실성을 고려하며, 안전 제약 조건을 포함하고, 새로운 작업에 효율적으로 적용할 수 있는 모델 예측 제어(MPC) 프레임워크를 제안합니다. 이 프레임워크는 접촉 제약 변동, 인간 목표의 불확실성, 또는 작업 교란으로 인한 불확실성을 고려할 수 있습니다. 불확실성 인식 작업 모델은 가우시안 프로세스를 사용하여 소수($\leq3$)의 시연으로부터 학습됩니다. 이 작업 모델은 비선형 MPC 문제에서 사용되어 이산적 인간 목표, 인간 운동학, 안전 제약 조건, 접촉 안정성 및 주파수 영역 교란 억제에 대한 신념에 따라 로봇 궤적과 임피던스를 최적화합니다. 이 MPC 공식이 소개되고, 볼록성 측면에서 분석되며, 다중 목표 협력 조작, 협력 연마 작업 및 협력 조립 작업에서 검증됩니다.

## 핵심 내용
목표의 변동, 환경 구성의 변화, 또는 작업 모델에 대한 신뢰도 차이로 인해 불확실성이 수반되는 로봇 작업은 로봇을 지시하거나 적응시키기 위해 인간의 입력이 필요할 수 있습니다. 물리적 접촉이 있는 작업에서는 개별 불확실성에 따라 로봇의 궤적이나 임피던스를 적응시키는 여러 기존 방법이 제안되었습니다. 예를 들어, 의도 감지 또는 시연을 통한 불확실성 인식 학습이 있습니다. 그러나 개별적인 방법만으로는 많은 작업에서 공동으로 존재하는 다양한 불확실성을 처리할 수 없습니다. 일반성을 향상시키기 위해, 본 논문은 궤적과 임피던스를 온라인으로 계획하고, 이산적 및 연속적 불확실성을 고려하며, 안전 제약 조건을 포함하고, 새로운 작업에 효율적으로 적용할 수 있는 모델 예측 제어(MPC) 프레임워크를 제안합니다. 이 프레임워크는 접촉 제약 변동, 인간 목표의 불확실성, 또는 작업 교란으로 인한 불확실성을 고려할 수 있습니다. 불확실성 인식 작업 모델은 가우시안 프로세스를 사용하여 소수($\leq3$)의 시연으로부터 학습됩니다. 이 작업 모델은 비선형 MPC 문제에서 사용되어 이산적 인간 목표, 인간 운동학, 안전 제약 조건, 접촉 안정성 및 주파수 영역 교란 억제에 대한 신념에 따라 로봇 궤적과 임피던스를 최적화합니다. 이 MPC 공식이 소개되고, 볼록성 측면에서 분석되며, 다중 목표 협력 조작, 협력 연마 작업 및 협력 조립 작업에서 검증됩니다.

## 参考
- http://arxiv.org/abs/2208.07035v2
