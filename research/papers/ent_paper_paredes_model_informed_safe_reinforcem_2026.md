---
$id: ent_paper_paredes_model_informed_safe_reinforcem_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Model-Informed Safe Reinforcement Learning for Bipedal Locomotion via Step-to-Step Prediction
  zh: Model-Informed Safe Reinforcement Learning for Bipedal Locomotion via Step-to-Step Prediction
  ko: Model-Informed Safe Reinforcement Learning for Bipedal Locomotion via Step-to-Step Prediction
summary:
  en: Humanoid robots promise versatile mobility in cluttered, human-centric environments, but real deployment demands principled
    safety. Classical model-based gait generators yield interpretable motions but often lack the robustness and adaptability
    of modern reinforcement learning (RL) based approaches. We propose a model-informed reinforcement learning framework anchored
    to the analytical Angular ...
  zh: 本文提出一种模型引导的安全强化学习框架，用于双足机器人行走，其核心是将解析的 Angular Momentum Linear Inverted Pendulum (ALIP) 模板与离散指数控制屏障函数（DECBF）结合，为 ALIP
    迈步提供逐步安全证书。该证书既作为训练期的塑形信号，也作为运行时的动作过滤器，以最小幅度调整摆动足落点。作者为 Victor Paredes 与 Ayonga Hereid，在 MuJoCo 中的 Digit 人形机器人上配合全身控制器进行了验证。
  ko: Humanoid robots promise versatile mobility in cluttered, human-centric environments, but real deployment demands principled
    safety. Classical model-based gait generators yield interpretable motions but often lack the robustness and adaptability
    of modern reinforcement learning (RL) based approaches. We propose a model-informed reinforcement learning framework anchored
    to the analytical Angular ...
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
- safe_reinforcement_learning
- bipedal_locomotion
- control_barrier_function
- alip_template
- humanoid_robotics
- step_to_step_prediction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.34486);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.34486 Model-Informed Safe Reinforcement Learning for Bipedal Locomotion via Step-to-Step Prediction
  url: https://arxiv.org/abs/2609.34486
  date: '2026-09-28'
  accessed_at: '2026-10-05'
---

## 概述

人形机器人有望在杂乱且以人为中心的环境中实现灵活移动，但实际部署需要具备原理性保障的安全性。传统基于模型的步态生成器能产生可解释的运动，却往往缺乏现代强化学习方法的鲁棒性与适应性。为此，作者提出一种锚定于解析 ALIP 模板的模型引导强化学习框架，通过离散指数控制屏障函数为 ALIP 迈步提供逐步安全证书。该证书被同时用作训练期的塑形信号与运行时的动作过滤器，后者以最小方式调整摆动足落点以满足模板层面的约束。整体安全性在 MuJoCo 中的 Digit 人形机器人上配合全身控制器栈进行经验评估，结果显示相比无约束基线，该方法在报告的外部扰动试验中减少了安全违规事件，但较大的横向速度瞬变也暴露出安全与跟踪之间的权衡。

## 核心内容

### 问题背景
人形机器人具备在杂乱、以人为中心的环境中实现多样移动的潜力，但真实部署要求有原理支撑的安全性。经典基于模型的步态生成器能给出可解释的运动，却常常不如现代强化学习方法鲁棒和适应性强。因此作者希望在保留解析模型可解释性的同时，借助强化学习提升鲁棒性与适应性，并引入明确的安全机制。

### 方法
- 以解析的 Angular Momentum Linear Inverted Pendulum (ALIP) 模板作为框架锚点。
- 通过离散指数控制屏障函数（DECBF）为 ALIP 迈步提供逐步安全证书。
- 该安全证书有两种用途：
  - 作为训练期的塑形信号；
  - 作为运行时的动作过滤器，以最小幅度调整摆动足落点，从而满足模板层面的约束。

### 实验设置
- 在 MuJoCo 中对 Digit 人形机器人进行全阶安全性经验评估。
- 使用全身控制器栈（whole-body controller stack）。
- 与无约束基线进行对比，并在报告的外部扰动试验中统计安全违规事件。

### 关键结果
- 相比无约束基线，所提方法在报告的外部扰动试验中减少了安全违规事件。
- 在较大的横向速度瞬变下，观察到安全与跟踪之间存在权衡。

### 结论
将解析 ALIP 模板的逐步安全证书同时用于训练塑形与运行时动作过滤，可在保持模板层面约束的同时降低安全违规；但安全性与跟踪性能之间存在需要权衡的关系。

## Overview

Humanoid robots promise versatile mobility in cluttered, human-centric environments, but real deployment demands principled safety. Classical model-based gait generators yield interpretable motions but often lack the robustness and adaptability of modern reinforcement learning (RL) based approaches. We propose a model-informed reinforcement learning framework anchored to the analytical Angular Momentum Linear Inverted Pendulum (ALIP) template. We provide a step-to-step safety certificate for ALIP stepping via a discrete exponential control barrier function (DECBF) and use it as (i) a training-time shaping signal and (ii) a runtime action filter that minimally adjusts swing-foot placement to satisfy template-level constraints. Full-order safety is evaluated empirically on the Digit humanoid in MuJoCo with a whole-body controller stack. Compared to an unconstrained baseline, our approach reduces safety-violation events in the reported external-disturbance trial, while larger lateral-velocity transients reveal a safety-tracking tradeoff.

## 参考
- https://arxiv.org/abs/2609.34486
