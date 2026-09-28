---
$id: ent_paper_huang_online_sim_to_real_adaptation_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Online Sim-to-Real Adaptation via Closed-Loop System Modeling
  zh: Online Sim-to-Real Adaptation via Closed-Loop System Modeling
  ko: Online Sim-to-Real Adaptation via Closed-Loop System Modeling
summary:
  en: Sim-to-real transfer has made substantial progress, but can still produce controllers that remain stable and functional
    on hardware while suffering from degraded tracking accuracy due to residual dynamics mismatch. Correcting these errors
    typically requires identifying the underlying system dynamics, adapting the control policy, or returning to simulation
    for additional training and finetuning, ...
  zh: OSRAM（Online Sim-to-Real Adaptation via Closed-Loop System Modeling）是由 Yuhao Huang、Samuel A. Moore 和 Boyuan Chen 提出的框架，通过在线调整已有控制器的参考指令来缓解仿真到现实迁移中的残余动力学失配。该方法将部署后的机器人与策略视为统一的闭环动力学系统，在仿真中跨随机动力学元训练闭环模型，并在部署后用有限的真实交互快速微调，从而优化未来的参考指令而不改动底层控制策略。在双足速度跟踪与移动操作任务上，仿真与硬件实验均显示该方法提升了预测与跟踪精度。
  ko: Sim-to-real transfer has made substantial progress, but can still produce controllers that remain stable and functional
    on hardware while suffering from degraded tracking accuracy due to residual dynamics mismatch. Correcting these errors
    typically requires identifying the underlying system dynamics, adapting the control policy, or returning to simulation
    for additional training and finetuning, ...
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
- sim_to_real
- closed_loop_modeling
- online_adaptation
- reference_command_optimization
- bipedal_locomotion
- loco_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.28878);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.28878 Online Sim-to-Real Adaptation via Closed-Loop System Modeling
  url: https://arxiv.org/abs/2609.28878
  date: '2026-09-24'
  accessed_at: '2026-09-28'
---

## 概述

仿真到现实的迁移虽已取得显著进展，但残余的动力学失配仍会导致控制器在硬件上保持稳定却跟踪精度下降。传统做法通常需要辨识系统动力学、调整控制策略或回到仿真中继续训练微调，这些途径往往消耗大量数据与算力。OSRAM 提出改换思路：不去改动控制器本身，而是调整输入给已有控制器的参考指令。该框架把部署后的机器人与策略整体看作一个闭环动力学系统，直接从跟踪观测中学习其任务层面的指令—响应行为。闭环动力学模型先在仿真中跨随机动力学进行元训练，部署后再利用有限的真实交互快速微调，并用适配后的模型优化后续参考指令。作者在双足速度跟踪与移动操作任务上开展了仿真与硬件评估，结果表明闭环建模提升了在未见动力学下的预测与跟踪精度，在线参考适配则在不同控制目标与硬件配置下降低了残余的仿真到现实跟踪误差。

## 核心内容

### 问题背景
仿真到现实的迁移研究已取得长足进步，但迁移后的控制器仍可能面临一种困境：在硬件上保持稳定且可运行，却因残余的动力学失配而出现跟踪精度下降。要修正这类误差，通常需要辨识底层系统动力学、对控制策略进行适配，或者返回仿真环境做额外的训练与微调，而这些途径往往需要大量数据与计算资源。

### 方法
作者提出 OSRAM（Online Sim-to-Real Adaptation via Closed-Loop System Modeling），其核心思路是不改动控制器，而是调整提供给已有控制器的参考指令。

- 将部署后的机器人及其策略视为一个统一的闭环动力学系统。
- 直接从跟踪观测中学习该系统在任务层面的指令—响应行为。
- 闭环动力学模型在仿真中跨随机动力学进行元训练，部署后借助有限的真实世界交互快速微调。
- 使用适配后的模型优化未来的参考指令，同时保持底层控制策略不变。

### 实验设置
评估覆盖双足速度跟踪与移动操作两类任务，既在仿真中进行，也在硬件上开展。

### 关键结果
- 闭环建模提升了在未见动力学条件下的预测精度与跟踪精度。
- 在线参考适配在不同控制目标与硬件配置下均降低了残余的仿真到现实跟踪误差。

### 结论
结果表明，对机器人—策略闭环的行为进行适配，为仿真到现实迁移提供了一种切实可行的替代方案，可取代微调策略或辨识完整物理动力学这两类做法。更多信息见 http://generalroboticslab.com/OSRAM。

## Overview

Sim-to-real transfer has made substantial progress, but can still produce controllers that remain stable and functional on hardware while suffering from degraded tracking accuracy due to residual dynamics mismatch. Correcting these errors typically requires identifying the underlying system dynamics, adapting the control policy, or returning to simulation for additional training and finetuning, all of which can require substantial data and computation. We propose OSRAM (Online Sim-to-Real Adaptation via Closed-Loop System Modeling), a framework that instead adapts the reference commands provided to an existing controller. OSRAM treats the deployed robot and its policy as a unified closed-loop dynamical system and learns its task-level command-response behavior directly from tracking observations. A closed-loop dynamics model is meta-trained across randomized dynamics in simulation and rapidly finetuned after deployment using limited real-world interaction. The adapted model is then used to optimize future reference commands while leaving the underlying control policy unchanged. We evaluate OSRAM on bipedal velocity tracking and loco-manipulation in simulation and on hardware. Results show that closed-loop modeling improves prediction and tracking accuracy under unseen dynamics, while online reference adaptation reduces residual sim-to-real tracking errors across different control objectives and hardware configurations. These results demonstrate that adapting the behavior of the robot-policy closed loop provides a practical alternative to finetuning the policy or identifying the full physical dynamics for sim-to-real transfer. More information can be found at http://generalroboticslab.com/OSRAM.

## 参考
- https://arxiv.org/abs/2609.28878
