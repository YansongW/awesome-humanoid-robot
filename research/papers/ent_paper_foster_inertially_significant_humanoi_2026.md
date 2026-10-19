---
$id: ent_paper_foster_inertially_significant_humanoi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation
  zh: Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation
  ko: Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation
summary:
  en: The effective deployment of humanoid robots in practical tasks of interest will require a capability of sensing and
    adapting to variations in inertial parameters, as occurs during heavy tool use or when carrying significant payload. Such
    payloads constitute a significant proportion of the combined payload-robot system, the effects of which cannot be ignored
    by delegating to feedback control. This ...
  zh: 该论文提出一种面向人形机器人遥操作的通用方案，将全身模型预测控制（WB-MPC）与扩展卡尔曼滤波（EKF）结合，在线估计随时间变化且物理一致的惯性参数。估计结果被送入 WB-MPC 的完整刚体动力学模型，从而在外部负载下生成更准确的前馈力矩。作者还提供
    VR 接口，让操作员无需考虑负载即可给出任务参考，动态平衡交由 WB-MPC 负责。该框架在人形系统上通过仿真与硬件实验得到验证。
  ko: The effective deployment of humanoid robots in practical tasks of interest will require a capability of sensing and
    adapting to variations in inertial parameters, as occurs during heavy tool use or when carrying significant payload. Such
    payloads constitute a significant proportion of the combined payload-robot system, the effects of which cannot be ignored
    by delegating to feedback control. This ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_teleoperation
- whole_body_model_predictive_control
- online_parameter_estimation
- extended_kalman_filter
- inertial_parameters
- vr_interface
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.22176);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.22176 Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online
    Parameter Estimation
  url: https://arxiv.org/abs/2610.22176
  date: '2026-10-15'
  accessed_at: '2026-10-19'
---

## 概述

人形机器人在使用重型工具或携带大质量载荷时，惯性参数会发生显著变化，这类载荷在机器人-载荷联合系统中占比很大，无法仅靠反馈控制忽略其影响。为此，作者将全身模型预测控制器与扩展卡尔曼滤波器集成，实现在线估计完全物理一致、随时间变化的惯性参数，并把估计值注入 WB-MPC 的完整刚体动力学模型，使任务需求下的前馈力矩更准确。系统还配备 VR 接口，操作员只需给出任务相关参考，无需关心载荷，动态平衡由 WB-MPC 承担。该框架在仿真和硬件实验中于人形系统上完成验证。

## 核心内容

### 问题背景
人形机器人要在实际任务中有效部署，需要具备感知并适应惯性参数变化的能力，例如使用重型工具或携带大质量载荷时。此类载荷在机器人-载荷联合系统中占比较大，其影响不能通过交给反馈控制来忽略。

### 方法
- 将全身模型预测控制器（WB-MPC）与扩展卡尔曼滤波（EKF）集成，在线估计完全物理一致、随时间变化的惯性参数。
- 将估计结果送入 WB-MPC 的完整刚体动力学模型，从而在外部负载下为任务需求生成更准确的前馈力矩。
- 提供虚拟现实（VR）接口，使操作员能够在不考虑载荷的情况下给出任务特定参考，并将动态平衡委托给 WB-MPC。

### 实验设置与结果
论文通过仿真与硬件实验在人形系统上验证了该框架。摘要未给出具体实验数字、对比基线或硬件型号。

### 结论
该工作展示了一种通用解决方案：通过 WB-MPC 与 EKF 在线惯性参数估计的结合，并配合 VR 遥操作接口，使人形机器人在外部负载变化下仍能获得更准确的前馈力矩并维持动态平衡。

## Overview

The effective deployment of humanoid robots in practical tasks of interest will require a capability of sensing and adapting to variations in inertial parameters, as occurs during heavy tool use or when carrying significant payload. Such payloads constitute a significant proportion of the combined payload-robot system, the effects of which cannot be ignored by delegating to feedback control. This paper showcases a general solution to this problem by integrating a whole body model predictive controller (WB-MPC) with an extended Kalman filter (EKF) for online estimation of fully physically consistent time-varying inertial parameters. These estimates are fed through to the WB-MPC's full rigid body dynamics model, resulting in more accurate feedforward torques for task demands under external load. Additionally, a virtual reality (VR) interface is provided that enables an operator to provide task-specific references without regard to payload while delegating dynamic balance to the WB-MPC. The framework is validated with simulation and hardware experiments on a humanoid system.

## 参考
- https://arxiv.org/abs/2610.22176
