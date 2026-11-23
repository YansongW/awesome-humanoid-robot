---
$id: ent_paper_dawood_driving_the_style_velocity_con_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Driving the Style: Velocity-Conditioned Whole-Body Control from Motion Demonstrations'
  zh: 'Driving the Style: Velocity-Conditioned Whole-Body Control from Motion Demonstrations'
  ko: 'Driving the Style: Velocity-Conditioned Whole-Body Control from Motion Demonstrations'
summary:
  en: Achieving human-like behavior on humanoid robots has advanced rapidly by leveraging motion-capture demonstrations rather
    than hand-crafted cost functions. Adversarial imitation supplies a style signal that lets a policy fulfill a task while
    adhering to a desired style, but is difficult to transfer to hardware. Whole-body tracking through reinforcement learning
    instead deploys reliably and ...
  zh: 该论文提出一种速度条件化的全身控制方法，让人形机器人仅凭紧凑的运动指令与机器人观测即可复现示范动作的全身风格。作者为 Murad Dawood、Oezge Drama Berkenkamp、Antonio Gonzales Marin
    与 Nutan Chen。核心做法是用全身跟踪奖励训练策略，参考动作只用于监督奖励与特权评论家，不向演员提供参考关节轨迹，也无需教师蒸馏；在 Unitree G1 上全部试验均完成。
  ko: Achieving human-like behavior on humanoid robots has advanced rapidly by leveraging motion-capture demonstrations rather
    than hand-crafted cost functions. Adversarial imitation supplies a style signal that lets a policy fulfill a task while
    adhering to a desired style, but is difficult to transfer to hardware. Whole-body tracking through reinforcement learning
    instead deploys reliably and ...
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
- humanoid_control
- whole_body_tracking
- motion_imitation
- velocity_conditioned_policy
- reinforcement_learning
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.20888);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.20888 Driving the Style: Velocity-Conditioned Whole-Body Control from Motion Demonstrations'
  url: https://arxiv.org/abs/2611.20888
  date: '2026-11-16'
  accessed_at: '2026-11-23'
---

## 概述

现有方法中，对抗式模仿能提供风格信号但难以迁移到真实硬件，而基于强化学习的全身跟踪虽部署可靠却依赖运行时参考轨迹，遇到训练分布外的动作容易失败。本文改为直接用全身跟踪奖励训练人形机器人策略，同时把演员的输入限制为紧凑的运动指令和机器人观测，参考动作仅用于监督奖励函数与特权评论家，既不给演员提供参考关节轨迹，也不需要教师蒸馏。这样示范风格通过跟踪奖励被编码进策略，机器人便能在给定速度指令下复现全身风格。作者仅用一段随机行走动作训练，并用来自留出动作的速度曲线下达指令，仿真中成功率至少 98%，在 Unitree G1 上每次试验均完成；而在留出的慢速行走上，全身跟踪成功率降至 2%，指令条件化蒸馏为 56%，两者在真实机器人上均失败。

## 核心内容

### 问题背景

让人形机器人表现出类人行为，主流路线之一是借助动作捕捉示范而非手工设计代价函数。对抗式模仿能提供风格信号，使策略在完成任务的同时贴合期望风格，但难以迁移到真实硬件。基于强化学习的全身跟踪部署可靠、模仿示范忠实，然而其策略以未来参考为条件，运行时必须提供参考轨迹，且当动作偏离训练数据时可能失败。

### 方法

- 直接用全身跟踪奖励训练人形机器人策略。
- 将演员的输入限制为紧凑的运动指令与机器人观测，不向其提供参考关节轨迹。
- 参考动作仅用于监督奖励函数与特权评论家，不进行教师蒸馏。
- 示范风格由此通过跟踪奖励编码进策略，机器人在给定速度指令下复现全身风格。

### 实验设置

- 训练仅使用一段随机行走动作。
- 指令使用来自留出动作的速度曲线。
- 对比对象包括全身跟踪与指令条件化蒸馏，以及对抗运动先验（AMP）。
- 评测平台为仿真环境与 Unitree G1 真实机器人。

### 关键结果

- 仿真中成功率至少 98%，在 Unitree G1 上完成每一次试验。
- 在留出的慢速行走上，全身跟踪成功率降至 2%，指令条件化蒸馏为 56%，两者在真实机器人上均失败。
- 在训练过的动作上，本策略的关节位置误差保持在全身跟踪的 8% 以内。
- 本策略的风格覆盖率高于 AMP，而 AMP 在真实机器人上未使用安全吊架时摔倒。

### 结论

将参考动作的作用限制在奖励与特权评论家、让演员只依赖紧凑指令与观测，可以在无需运行时参考轨迹与教师蒸馏的前提下，把人形机器人的全身示范风格编码进可部署的策略，并在仿真与真实硬件上取得稳定表现。

## Overview

Achieving human-like behavior on humanoid robots has advanced rapidly by leveraging motion-capture demonstrations rather than hand-crafted cost functions. Adversarial imitation supplies a style signal that lets a policy fulfill a task while adhering to a desired style, but is difficult to transfer to hardware. Whole-body tracking through reinforcement learning instead deploys reliably and imitates demonstrations faithfully, but the resulting policies are conditioned on the future reference, so they require a reference trajectory at runtime and can fail when the motion differs from the training data. We train a humanoid policy directly with whole-body tracking rewards while restricting its actor to compact locomotion commands and robot observations. Reference motion supervises the reward and privileged critic, without supplying reference joint trajectories to the actor or requiring teacher distillation. The demonstrated style is thereby encoded in the policy through the tracking reward, so the robot reproduces the whole-body style under commanded velocities. Trained on a single random-walk motion and commanded with velocity profiles from held-out motions, our policy reaches at least 98\% success in simulation and completes every trial on the Unitree G1. On held-out slow walking, whole-body tracking drops to 2\% success and command-conditioned distillation to 56\%, and both fail on the real robot. On the trained motions, the joint position error of our policy stays within 8\% of whole-body tracking, and it has a higher style coverage than adversarial motion priors (AMP), which fell on the real robot without a safety crane.

## 参考
- https://arxiv.org/abs/2611.20888
