---
$id: ent_paper_chen_wevo_world_model_enabled_vla_o_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation'
  zh: 'WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation'
  ko: 'WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation'
summary:
  en: Reinforcement learning (RL) can improve vision-language-action (VLA) policies beyond imitation, but humanoid exploration
    is unsafe and simulator RL can exploit residual sim-to-real gaps. We present WEVO, a teleoperation-free framework for
    post-training a whole-body humanoid VLA in an action-conditioned video world model (WM). Simulated manipulation and locomotion
    play data improve ...
  zh: WEVO 是一个无需遥操作的框架，用于在动作条件视频世界模型（WM）中对全身人形机器人 VLA 策略进行后训练。作者利用仿真操作与运动"play data"提升接触动力学与视角变化预测，并用真实机器人自主 rollout 对齐世界模型。在三项真实机器人任务上，视频世界模型强化学习将平均成功率从
    23.3% 提升至 75.0%，高于真实机器人 RL 的 48.3%。
  ko: Reinforcement learning (RL) can improve vision-language-action (VLA) policies beyond imitation, but humanoid exploration
    is unsafe and simulator RL can exploit residual sim-to-real gaps. We present WEVO, a teleoperation-free framework for
    post-training a whole-body humanoid VLA in an action-conditioned video world model (WM). Simulated manipulation and locomotion
    play data improve ...
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
- vision_language_action
- world_model
- humanoid_loco_manipulation
- reinforcement_learning
- sim_to_real
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.25251);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.25251 WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation'
  url: https://arxiv.org/abs/2611.25251
  date: '2026-11-18'
  accessed_at: '2026-11-23'
---

## 概述

WEVO 针对的是强化学习提升 VLA 策略时面临的两难：真实人形机器人上探索不安全，而仿真器 RL 又可能利用残留的 sim-to-real 差距。该框架在动作条件视频世界模型中完成全身人形 VLA 的后训练，全程无需遥操作。方法上，先用仿真操作与运动 play data 改善世界模型对接触动力学和视角变化的预测能力，再让在合成示范上训练的 VLA 在每项任务上采集 20 次真实机器人自主 rollout，使世界模型与部署观测对齐。随后 VLA、全身控制器（WBC）与视频世界模型构成带稠密进度奖励的闭环 RL 环境。三项真实机器人任务的结果显示，play data 提升了所有被评估的世界模型指标及下游策略成功率，而视频世界模型 RL 的平均成功率达 75.0%，明显优于真实机器人 RL 的 48.3%。作者据此主张结合两类环境的互补优势：仿真提供策略初始化与广泛覆盖，视频世界模型提供与部署对齐的策略改进环境。

## 核心内容

### 问题背景

强化学习能够让 VLA 策略超越单纯的模仿学习，但在人形机器人上直接探索存在安全风险，而在仿真器中做 RL 又可能利用残留的 sim-to-real 差距，导致策略在真实部署中失效。WEVO 试图在不依赖遥操作的前提下，为全身人形 VLA 提供一个既安全又与部署对齐的策略改进环境。

### 方法

- **动作条件视频世界模型**：以动作条件视频世界模型作为 RL 环境的核心，替代真实机器人上的在线探索。
- **play data 预训练**：利用仿真中的操作与运动 play data，提升世界模型对接触动力学与视角变化的预测能力。
- **部署对齐**：在合成示范上训练的 VLA 在每项任务上采集 20 次真实机器人自主 rollout，用于将世界模型与真实部署观测对齐。
- **闭环 RL 环境**：VLA、全身控制器（WBC）与视频世界模型共同构成闭环 RL 环境，并使用稠密进度奖励进行策略优化。

### 实验设置

在三项真实机器人任务上进行评估，比较世界模型各项指标与下游策略成功率，并与真实机器人 RL 基线对照。

### 关键结果

- play data 提升了所有被评估的世界模型指标，并提升了下游策略成功率。
- 视频世界模型 RL 将平均成功率从 23.3% 提升至 75.0%。
- 真实机器人 RL 的平均成功率为 48.3%。

### 结论

仿真与视频世界模型具有互补优势：仿真提供策略初始化与广泛覆盖，视频世界模型则提供与部署对齐的环境用于策略改进。WEVO 以无需遥操作的方式实现了全身人形 VLA 的后训练。

## Overview

Reinforcement learning (RL) can improve vision-language-action (VLA) policies beyond imitation, but humanoid exploration is unsafe and simulator RL can exploit residual sim-to-real gaps. We present WEVO, a teleoperation-free framework for post-training a whole-body humanoid VLA in an action-conditioned video world model (WM). Simulated manipulation and locomotion play data improve contact-dynamics and viewpoint-change prediction. A VLA trained on synthetic demonstrations collects 20 autonomous real robot rollouts per task to align the WM with deployment observations. The VLA, whole-body controller (WBC), and video WM then form a closed-loop RL environment with dense progress rewards. Across three real robot tasks, play data improves every evaluated WM metric and downstream policy success; video WM RL raises mean success from 23.3% to 75.0%, compared with 48.3% for real robot RL. We therefore leverage the complementary strengths of both environments: simulation provides policy initialization and broad coverage, while the video WM offers a deployment-aligned environment for policy improvement. Project website: https://qianzhong-chen.github.io/wevo.github.io/.

## 参考
- https://arxiv.org/abs/2611.25251
