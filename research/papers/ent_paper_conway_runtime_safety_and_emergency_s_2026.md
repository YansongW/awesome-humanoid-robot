---
$id: ent_paper_conway_runtime_safety_and_emergency_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority'
  zh: 'Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority'
  ko: 'Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority'
summary:
  en: Full-size humanoid robots are being considered for hazardous industrial work such as disassembling electric-vehicle
    batteries. We describe the safety mechanisms of an open-source autonomy stack for the Unitree H1-2 humanoid and what deploying
    them taught us. All joint commands pass through a safety layer that runs separately from the control software. It enforces
    joint position, velocity, and ...
  zh: 本文介绍了为 Unitree H1-2 全尺寸人形机器人开发的开源自主栈中的安全机制，并总结了实际部署经验。所有关节指令都经过一个独立于控制软件运行的安全层，该层执行关节位置、速度和力矩限制，并在状态估计过期或硬接线急停（e-stop）被按下或断开时停止机器人。作者通过推倒站立机器人进行测试，发现模型预测下体控制器从未成功恢复平衡，操作员每次都必须按下急停，而急停会移除平衡控制并导致机器人跌倒；作者据此主张应分阶段授予机器人施力权限，并由明确的人员或组织对其使用负责。
  ko: Full-size humanoid robots are being considered for hazardous industrial work such as disassembling electric-vehicle
    batteries. We describe the safety mechanisms of an open-source autonomy stack for the Unitree H1-2 humanoid and what deploying
    them taught us. All joint commands pass through a safety layer that runs separately from the control software. It enforces
    joint position, velocity, and ...
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
- humanoid_safety
- emergency_stop
- runtime_safety
- force_authority
- unitree_h1_2
- deployment_lessons
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.15928);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.15928 Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated
    Force Authority'
  url: https://arxiv.org/abs/2611.15928
  date: '2026-11-11'
  accessed_at: '2026-11-16'
---

## 概述

本文面向全尺寸人形机器人在危险工业作业（如拆解电动汽车电池）中的部署安全需求，描述了 Unitree H1-2 开源自主栈的安全机制及其部署教训。安全层独立于控制软件运行，对所有关节指令施加位置、速度和力矩限制，并在状态估计过期或硬接线急停被按下或断开时触发停止。作者对站立机器人进行推倒测试，使用模型预测下体控制器时机器人从未恢复平衡，操作员在每次试验中都必须按下急停，而按下急停会移除平衡控制并导致跌倒。安全层自身的限制也会触发同样的停止，且为操作任务选定的限制在正常行走中即被超出。作者指出，在操作员或电池包附近，跌倒可能比触发停止的原因更危险，关节限制只能约束机器人能施加多大的力，却无法判断何时施力是合适的，因此借鉴责任研究以及儿童与青少年发展研究，主张分阶段授予机器人施力权限，并由明确的人员或组织对其使用负责。

## 核心内容

### 问题背景
全尺寸人形机器人正被考虑用于危险工业作业，例如拆解电动汽车电池。此类场景对安全性提出很高要求，本文以 Unitree H1-2 人形机器人为平台，介绍其开源自主栈中的安全机制，并总结部署过程中获得的经验教训。

### 方法
- 所有关节指令都经过一个安全层，该层与控制软件分开运行。
- 安全层执行关节位置、速度与力矩限制。
- 当状态估计变得过期，或硬接线急停（e-stop）被按下或断开时，安全层会停止机器人。

### 实验设置与关键结果
- 作者推动站立的机器人直至其失去平衡。
- 在使用模型预测下体控制器的情况下，机器人从未恢复平衡，操作员在每次试验中都必须按下急停。
- 按下急停会移除平衡控制，机器人随之跌倒。
- 安全层自身的限制会触发同样的停止；为操作任务选定的限制在正常行走过程中即被超出。
- 在操作员或电池包附近，跌倒可能比导致停止的原因更危险。

### 结论
关节限制只能约束机器人能施加多大的力，却无法界定何时施力是合适的。作者借鉴关于责任的研究以及儿童与青少年发展的研究，主张分阶段授予机器人施力权限，并由一名人员或一个组织明确对其使用负责。

## Overview

Full-size humanoid robots are being considered for hazardous industrial work such as disassembling electric-vehicle batteries. We describe the safety mechanisms of an open-source autonomy stack for the Unitree H1-2 humanoid and what deploying them taught us. All joint commands pass through a safety layer that runs separately from the control software. It enforces joint position, velocity, and torque limits, and it stops the robot when a state estimate becomes stale or when the hard-wired emergency stop (e-stop) is pressed or disconnected. We pushed the standing robot until it lost balance. With a model-predictive lower-body controller it never recovered, and the operator had to press the e-stop in every trial. Pressing it removes balance control, and the robot falls. The safety layer's own limits trigger the same stop, and limits chosen for manipulation were exceeded during normal walking. Near an operator or a battery pack, the fall can be more dangerous than the cause of the stop. Joint limits bound how much force a robot can apply, but not when applying it is appropriate. Drawing on research on responsibility and on child and adolescent development, we therefore make a case for granting robots force authority in stages, with a person or organization explicitly responsible for its use.

## 参考
- https://arxiv.org/abs/2611.15928
