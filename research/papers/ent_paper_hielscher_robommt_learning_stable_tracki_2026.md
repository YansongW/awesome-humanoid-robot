---
$id: ent_paper_hielscher_robommt_learning_stable_tracki_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMMT: Learning Stable Tracking of Modulated Expressive and Interactive Robot Motion'
  zh: 'RoboMMT: Learning Stable Tracking of Modulated Expressive and Interactive Robot Motion'
  ko: 'RoboMMT: Learning Stable Tracking of Modulated Expressive and Interactive Robot Motion'
summary:
  en: Expressive robot motion can improve naturalness, effectiveness, and perceived likability in human-robot interaction.
    When deployed on dynamically unstable platforms, however, reactive execution of expressive body motion may bring the robot
    to its stability limits, especially when expressivity is decoupled from physical control. In this paper, we present RoboMMT
    (Robot Modulated Motion Tracking), ...
  zh: RoboMMT（Robot Modulated Motion Tracking）是由 Till Hielscher 与 Kai O. Arras 提出的模块化控制架构，将参数化表现性动作合成、基于物理的角色控制与面向空间交互目标的反应式适应相耦合。该方法训练一个以参考动作为条件的跟踪策略，使其在广泛的表现性域内既能忠实执行指令动作又能保持动态稳定，并通过轻量级任务专用交互策略调节参考生成器的空间目标吸引点。在四足与两款人形机器人上的评估表明，该跟踪器在整个调制域内保持稳定与准确，而缺乏该覆盖范围训练的跟踪器会失去平衡或跟踪精度。
  ko: Expressive robot motion can improve naturalness, effectiveness, and perceived likability in human-robot interaction.
    When deployed on dynamically unstable platforms, however, reactive execution of expressive body motion may bring the robot
    to its stability limits, especially when expressivity is decoupled from physical control. In this paper, we present RoboMMT
    (Robot Modulated Motion Tracking), ...
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
- humanoid_robotics
- motion_tracking
- expressive_motion
- sim_to_real
- whole_body_control
- human_robot_interaction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.26414);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.26414 RoboMMT: Learning Stable Tracking of Modulated Expressive and Interactive Robot Motion'
  url: https://arxiv.org/abs/2610.26414
  date: '2026-10-19'
  accessed_at: '2026-10-26'
---

## 概述

表现性机器人动作能提升人机交互的自然度、有效性与被感知的亲和力，但在动态不稳定平台上，若表现性与物理控制解耦，反应式执行表现性身体动作可能使机器人逼近稳定性极限。RoboMMT 采用模块化控制架构，把参数化表现性动作合成、基于物理的角色控制以及对空间交互目标的反应式适应三者耦合起来。其核心是训练一个以参考动作为条件的跟踪策略，覆盖宽广的表现性域，从而在忠实复现指令动作的同时维持动态稳定；目标反应性则由轻量级、任务专用的交互策略实现，这些策略调节参考生成器的空间目标吸引点，而稳定化跟踪策略始终保留在闭环中。在四足机器人与两款人形机器人上的评估显示，学习到的跟踪器在整个调制域内保持稳定与准确，而未覆盖该域训练的跟踪器会失去平衡、损失跟踪精度或两者兼有。在此基础之上叠加闭环目标适应，可实现交互式的面向与指向行为，同时保持稳定执行与相近的参考跟踪保真度；机器人还能学会主动重分配体重并采取纠正步。四足机器人在强扰动下的真机实验展示了零样本 sim-to-real 迁移。

## 核心内容

### 问题背景

表现性机器人动作有助于提升人机交互中的自然度、有效性与被感知的亲和力。然而当这类动作部署在动态不稳定的平台上时，若表现性与物理控制相互解耦，反应式地执行表现性身体动作可能把机器人推向稳定性极限。如何在保持动态稳定的前提下执行可调的表现性动作，并同时响应空间交互目标，是本文关注的问题。

### 方法

RoboMMT（Robot Modulated Motion Tracking）是一个模块化控制架构，耦合三个部分：

- 参数化表现性动作合成；
- 基于物理的角色控制；
- 对空间交互目标的反应式适应。

具体做法包括：

- 训练一个以参考动作为条件的跟踪策略，训练覆盖宽广的表现性域，使其既能忠实实现指令动作，又能维持动态稳定；
- 目标反应性通过训练轻量级、任务专用的交互策略实现，这些策略调节参考生成器的空间目标吸引点，同时将稳定化跟踪策略保留在闭环中。

### 实验设置

评估在四足机器人与两款人形机器人上进行。对比对象为未覆盖该调制域训练的跟踪器。真机实验在四足机器人上开展，并施加了强扰动以考察零样本 sim-to-real 迁移。

### 关键结果

- 学习到的跟踪器在整个调制域内保持稳定且准确；
- 未覆盖该域训练的跟踪器会失去平衡、损失跟踪精度，或两者兼有；
- 在该基础之上叠加闭环目标适应，可实现交互式的面向与指向行为，同时保持稳定执行与相近的参考跟踪保真度；
- 机器人学会主动重分配体重并采取纠正步；
- 四足机器人在强扰动下的真机实验展示了零样本 sim-to-real 迁移。

### 结论

将覆盖广泛表现性域的参考条件跟踪策略与轻量级闭环目标适应分层组合，可以在动态不稳定平台上稳定地执行可调的表现性动作并实现交互式空间行为，且具备向真实四足机器人零样本迁移的能力。

## Overview

Expressive robot motion can improve naturalness, effectiveness, and perceived likability in human-robot interaction. When deployed on dynamically unstable platforms, however, reactive execution of expressive body motion may bring the robot to its stability limits, especially when expressivity is decoupled from physical control. In this paper, we present RoboMMT (Robot Modulated Motion Tracking), a modular control architecture that couples parameterized expressive motion synthesis, physics-based character control, and reactive adaptation to spatial interaction goals. Our approach trains a reference-conditioned tracking policy across a broad domain of expressivity, enabling it to faithfully realize the commanded motions while maintaining dynamic stability. Goal reactivity is achieved by training lightweight, task-specific interaction policies that modulate the reference generator's spatial goal-attraction point, with the stabilizing tracking policy kept in the loop. Evaluations on a quadruped and two humanoid robots show that the learned tracker remains stable and accurate across the entire modulation domain, whereas trackers trained without this coverage lose balance, tracking accuracy, or both. We show that layering closed-loop goal adaptation over this foundation enables interactive facing and pointing behaviors, while maintaining stable execution and comparable reference-tracking fidelity. The robot learns to proactively redistribute its weight and take corrective steps. Zero-shot sim-to-real transfer is demonstrated through real-robot experiments on a quadruped under heavy disturbances.

## 参考
- https://arxiv.org/abs/2610.26414
