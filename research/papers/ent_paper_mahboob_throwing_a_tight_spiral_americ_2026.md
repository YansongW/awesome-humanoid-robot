---
$id: ent_paper_mahboob_throwing_a_tight_spiral_americ_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Throwing a Tight Spiral American Football by a Humanoid Robot
  zh: Throwing a Tight Spiral American Football by a Humanoid Robot
  ko: Throwing a Tight Spiral American Football by a Humanoid Robot
summary:
  en: Accurate throwing of the American football requires precise regulation of release conditions, where coupled linear and
    angular momentum determine flight stability and targeting accuracy. While prior work on robotic object throwing has largely
    focused on generating dynamically feasible release velocities using open-gripper paradigms, explicit control of spin injection
    at detachment remains ...
  zh: 本文提出了一种由人形机器人实现美式橄榄球“紧螺旋”投掷的控制框架，通过全身协调控制精确调节释放时的线动量与角动量。该方法在配备7自由度Dex3-1三指夹爪的29自由度Unitree G1人形机器人上验证，实现了最高93.6%的自旋效率和0.286弧度的鼻尖对准误差。
  ko: Accurate throwing of the American football requires precise regulation of release conditions, where coupled linear and
    angular momentum determine flight stability and targeting accuracy. While prior work on robotic object throwing has largely
    focused on generating dynamically feasible release velocities using open-gripper paradigms, explicit control of spin injection
    at detachment remains ...
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
- humanoid_robot
- whole_body_control
- object_throwing
- spin_stabilization
- model_predictive_control
- trajectory_optimization
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.16642);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2608.16642 Throwing a Tight Spiral American Football by a Humanoid Robot
  url: https://arxiv.org/abs/2608.16642
  date: '2026-08-17'
  accessed_at: '2026-08-24'
---

## 概述

本研究针对美式橄榄球这类气动各向异性物体的投掷问题，重点解决了释放阶段自旋注入的显式控制难题。作者将全身控制策略分为下肢稳定支撑与上肢两阶段控制（投掷阶段与跟随阶段），通过轨迹优化和模型预测控制管理亚100毫秒释放期间的欠驱动接触动力学。实验表明，该框架在5.35米/秒线速度和14.5弧度/秒角速度下，实现了接近理想的紧螺旋投掷效果。

## 核心内容

### 问题背景
精确投掷美式橄榄球需要严格调控释放条件，其中耦合的线动量与角动量决定飞行稳定性与瞄准精度。以往机器人投掷研究多采用开爪范式生成动态可行的释放速度，但对脱离瞬间自旋注入的显式控制研究不足，尤其针对美式橄榄球这类气动各向异性物体。

### 方法
作者提出耦合全身控制策略，将任务分解为：
- **下肢**：执行信息化的稳定控制，为上半身运动提供支撑。
- **上肢两阶段控制**：
  - **投掷阶段**：通过轨迹优化与跟踪，将橄榄球加速至目标状态。
  - **跟随阶段**：利用模型预测控制主动控制手腕及仍与球接触的手指，管理释放期间的瞬态接触动力学。

该策略需应对两大挑战：(i) 在约半秒内完成高自由度（DoF）运动以精确达到目标耦合动量；(ii) 管理亚100毫秒释放阶段中橄榄球部分跨越手指移动时的欠驱动接触动力学。

### 实验设置
- **平台**：29自由度Unitree G1人形机器人，配备7自由度Dex3-1三指夹爪。
- **评估指标**：自旋效率（理想紧螺旋为100%）与线速度-鼻尖对准（鼻尖角）误差（理想为0弧度）。

### 关键结果
- 投掷橄榄球达到最高**93.6%自旋效率**。
- 鼻尖角误差为**0.286弧度**。
- 最大线速度**5.35米/秒**，角速度**14.5弧度/秒**。

### 结论
该框架通过显式控制释放阶段的自旋注入，显著提升了人形机器人对气动各向异性物体的投掷精度，为动态操控任务提供了新的控制范式。

## Overview

Accurate throwing of the American football requires precise regulation of release conditions, where coupled linear and angular momentum determine flight stability and targeting accuracy. While prior work on robotic object throwing has largely focused on generating dynamically feasible release velocities using open-gripper paradigms, explicit control of spin injection at detachment remains underexplored, particularly for aerodynamically anisotropic objects like the American football. In this paper, we present the spin-stabilized controlled tight spiral throw of an American football by a humanoid robot. Achieving this requires (i) accurately reaching the desired coupled momentum, which often involves high degrees-of-freedom (DoF) movements completed within approximately half a second, and (ii) managing the complex transient contact dynamics that arise during the sub-100-millisecond release phase, when the football is effectively underactuated as it moves partially across the fingers. To this end, we develop a coupled whole-body control strategy where the lower body is performing informed stabilization while the upper body is further divided into two phases with (i) a throw phase accelerating the football to a target state through trajectory optimization and tracking, and (ii) a follow-through phase utilizing model predictive control to actively control the wrist and remaining in-contact fingers. The proposed framework is empirically validated on a 29-DoF Unitree G1 humanoid equipped with a 7-DoF Dex3-1 three-fingered gripper. The thrown American football reaches up to 93.6% spin efficiency and a 0.286 radians linear-velocity-to-nose-alignment (nose-angle) error (where an ``ideal'' tight spiral corresponds to 100 % spin efficiency and 0 radians nose-angle error) at up to a 5.35 m/s linear velocity and an angular velocity of 14.5 rad/s.

## 参考
- https://arxiv.org/abs/2608.16642
