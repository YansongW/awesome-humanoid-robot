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
  zh: 本文提出了一种非线性模型预测控制框架，能够在线联合优化机器人轨迹与阻抗。该框架利用高斯过程从少量示教中学习不确定性感知任务模型，处理物理人机交互任务（如协同搬运、抛光与装配）中的离散与连续不确定性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2208.07035v2.
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
Robotic tasks which involve uncertainty--due to variation in goal, environment configuration, or confidence in task model--may require human input to instruct or adapt the robot. In tasks with physical contact, several existing methods for adapting robot trajectory or impedance according to individual uncertainties have been proposed, e.g., realizing intention detection or uncertainty-aware learning from demonstration. However, isolated methods cannot address the wide range of uncertainties jointly present in many tasks.   To improve generality, this paper proposes a model predictive control (MPC) framework which plans both trajectory and impedance online, can consider discrete and continuous uncertainties, includes safety constraints, and can be efficiently applied to a new task. This framework can consider uncertainty from: contact constraint variation, uncertainty in human goals, or task disturbances. An uncertainty-aware task model is learned from a few ($\leq3$) demonstrations using Gaussian Processes. This task model is used in a nonlinear MPC problem to optimize robot trajectory and impedance according to belief in discrete human goals, human kinematics, safety constraints, contact stability, and frequency-domain disturbance rejection. This MPC formulation is introduced, analyzed with respect to convexity, and validated in co-manipulation with multiple goals, a collaborative polishing task, and a collaborative assembly task.

## 核心内容
Robotic tasks which involve uncertainty--due to variation in goal, environment configuration, or confidence in task model--may require human input to instruct or adapt the robot. In tasks with physical contact, several existing methods for adapting robot trajectory or impedance according to individual uncertainties have been proposed, e.g., realizing intention detection or uncertainty-aware learning from demonstration. However, isolated methods cannot address the wide range of uncertainties jointly present in many tasks.   To improve generality, this paper proposes a model predictive control (MPC) framework which plans both trajectory and impedance online, can consider discrete and continuous uncertainties, includes safety constraints, and can be efficiently applied to a new task. This framework can consider uncertainty from: contact constraint variation, uncertainty in human goals, or task disturbances. An uncertainty-aware task model is learned from a few ($\leq3$) demonstrations using Gaussian Processes. This task model is used in a nonlinear MPC problem to optimize robot trajectory and impedance according to belief in discrete human goals, human kinematics, safety constraints, contact stability, and frequency-domain disturbance rejection. This MPC formulation is introduced, analyzed with respect to convexity, and validated in co-manipulation with multiple goals, a collaborative polishing task, and a collaborative assembly task.

## 参考
- http://arxiv.org/abs/2208.07035v2

