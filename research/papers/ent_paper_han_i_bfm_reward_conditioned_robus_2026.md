---
$id: ent_paper_han_i_bfm_reward_conditioned_robus_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'I-BFM: Reward-Conditioned Robust Humanoid Interaction via Unsupervised Reinforcement Learning'
  zh: 'I-BFM: Reward-Conditioned Robust Humanoid Interaction via Unsupervised Reinforcement Learning'
  ko: 'I-BFM: Reward-Conditioned Robust Humanoid Interaction via Unsupervised Reinforcement Learning'
summary:
  en: Behavioral foundation models (BFMs) have recently shown that a single humanoid policy can support diverse whole-body
    control, but extending such generality to physical interaction remains challenging. We introduce I-BFM, to our knowledge
    the first BFM for humanoid-object interaction. Rather than relying on task-specific policies or reference tracking, I-BFM
    learns a shared representation of the ...
  zh: I-BFM 是首个面向人形机器人—物体交互的行为基础模型（BFM），由 Ziqi Han、Yitang Li 等人提出。它借助前向—后向表示与无监督强化学习，学习人形机器人、物体及其接触之间耦合动力学的共享表示，使同一策略在给定下游任务奖励后可直接以潜在指令为条件执行闭环交互，无需针对任务单独优化策略。单个策略可完成搬运、推动、踢击等交互任务，并兼顾目标到达、动作跟踪、风格控制与长时程任务串联。
  ko: Behavioral foundation models (BFMs) have recently shown that a single humanoid policy can support diverse whole-body
    control, but extending such generality to physical interaction remains challenging. We introduce I-BFM, to our knowledge
    the first BFM for humanoid-object interaction. Rather than relying on task-specific policies or reference tracking, I-BFM
    learns a shared representation of the ...
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
- humanoid_interaction
- behavior_foundation_model
- unsupervised_reinforcement_learning
- forward_backward_representations
- whole_body_control
- loco_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.06129);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.06129 I-BFM: Reward-Conditioned Robust Humanoid Interaction via Unsupervised Reinforcement Learning'
  url: https://arxiv.org/abs/2610.06129
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

I-BFM 针对的是行为基础模型在物理交互场景中泛化能力不足的问题：以往单个策略虽能覆盖多样的全身控制，却难以扩展到人形机器人与物体的接触交互。该方法不依赖任务专用策略或参考轨迹跟踪，而是用前向—后向表示结合无监督强化学习，习得人形机器人、物体与接触之间耦合动力学的共享表示。下游任务只需给出奖励，同一策略即可被潜在指令条件化，直接完成闭环交互，省去任务专用策略优化。为兼顾不同时间尺度的控制，训练中同时引入短时程交互目标与较长时程目标目标。实验显示，单一策略可执行搬运、推动、踢击，并支持目标到达、动作跟踪、风格控制与长时程任务串联；在偏离标称执行后仍保持有效，Carry 任务标称成功率为 94.3%，机器人跌倒后仍保留 89.3% 成功率，而基于规划的基线仅为 1.3%。在 Unitree G1 上的真实世界实验进一步展示了多样的移动操作行为、交互失败与外部扰动后的快速恢复，以及无需任务专用重训练的任务串联。

## 核心内容

### 问题背景
行为基础模型（BFMs）已表明单个类人策略可以支撑多样的全身控制，但把这种通用性延伸到物理交互仍然困难。现有做法多依赖任务专用策略或参考轨迹跟踪，难以在接触丰富的交互场景中复用同一策略。

### 方法
- 提出 I-BFM，作者称其为首个面向人形机器人—物体交互的 BFM。
- 不依赖任务专用策略或参考跟踪，而是通过前向—后向表示（forward-backward representations）与无监督强化学习，学习人形机器人、物体及其接触之间耦合动力学的共享表示。
- 给定下游任务奖励后，同一策略可直接以潜在指令（latent command）为条件执行闭环交互，无需任务专用策略优化。
- 为改善不同时间尺度上的交互控制，策略同时使用短时程交互目标与较长时程目标目标进行训练。

### 能力与实验设置
- 单一 I-BFM 策略可执行搬运（carrying）、推动（pushing）、踢击（kicking），并支持目标到达（goal reaching）、动作跟踪（motion tracking）、风格控制（stylistic control）与长时程任务串联（long-horizon task chaining）。
- 真实世界实验在 Unitree G1 上进行。

### 关键结果
- 在 Carry 任务上，I-BFM 达到 94.3% 的标称成功率；在机器人跌倒后仍保留 89.3% 的成功率，而基于规划的基线仅为 1.3%。
- 策略在显著偏离标称执行后依然有效。
- Unitree G1 上的真实实验展示了多样的移动操作行为、交互失败与外部扰动后的快速恢复，以及无需任务专用重训练的任务串联。

### 结论
I-BFM 表明，借助无监督强化学习习得的共享交互表示，单个策略即可在无需任务专用优化的情况下覆盖多种人形机器人—物体交互任务，并在跌倒等大幅偏离后保持鲁棒性，同时可迁移到真实机器人平台。

## Overview

Behavioral foundation models (BFMs) have recently shown that a single humanoid policy can support diverse whole-body control, but extending such generality to physical interaction remains challenging. We introduce I-BFM, to our knowledge the first BFM for humanoid-object interaction. Rather than relying on task-specific policies or reference tracking, I-BFM learns a shared representation of the coupled dynamics among the humanoid, objects, and their contacts using forward-backward representations and unsupervised reinforcement learning. Given a downstream task reward, the same policy can be directly conditioned on a latent command to execute closed-loop interaction without task-specific policy optimization. To improve interaction control over different time scales, we further train the policy with both short-horizon interaction targets and longer-horizon goal targets. A single I-BFM policy performs carrying, pushing, and kicking, while also supporting goal reaching, motion tracking, stylistic control, and long-horizon task chaining. More importantly, it remains effective after large deviations from nominal execution: on Carry, I-BFM achieves 94.3% nominal success and retains 89.3% success after robot falls, compared with 1.3% for a planning-based baseline. Real-world experiments on a Unitree G1 further demonstrate diverse loco-manipulation behaviors, rapid recovery from interaction failures and external disturbances, and task chaining without task-specific retraining.

## 参考
- https://arxiv.org/abs/2610.06129
