---
$id: ent_paper_fu_reloco_unified_humanoid_locomo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReLoco: Unified Humanoid Locomotion and Fall Recovery via Behavior-Conditioned Motion Priors'
  zh: 'ReLoco: Unified Humanoid Locomotion and Fall Recovery via Behavior-Conditioned Motion Priors'
  ko: 'ReLoco: Unified Humanoid Locomotion and Fall Recovery via Behavior-Conditioned Motion Priors'
summary:
  en: Humanoid robots must recover from falls and resume commanded motion to sustain locomotion. Learning these behaviors
    in one policy requires supervision that accommodates both upright movement and ground-contact recovery. We present ReLoco,
    a framework that uses behavior-conditioned adversarial motion priors to learn locomotion, get-up from arbitrary fallen
    postures, and command resumption within ...
  zh: ReLoco 是一个由 Lequn Fu、Yufeng Hu、Yijun Zhong 等人提出的框架，利用行为条件化的对抗运动先验，在单一本体感知策略中统一学习人形机器人的行走、从任意跌倒姿态起身以及指令恢复。该方法通过机器人姿态选择专家池并对共享判别器的两个行为专用输出进行条件化，在共同训练迭代下实现
    96.80% 的独立起身成功率和 96.96% 的推倒恢复成功率，躯干平面速度 RMSE 为 0.1266 m/s。该策略在 64.5 kg 的 Tiangong 3.0 人形机器人上完成部署，无需控制器切换或机上策略微调。
  ko: Humanoid robots must recover from falls and resume commanded motion to sustain locomotion. Learning these behaviors
    in one policy requires supervision that accommodates both upright movement and ground-contact recovery. We present ReLoco,
    a framework that uses behavior-conditioned adversarial motion priors to learn locomotion, get-up from arbitrary fallen
    postures, and command resumption within ...
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
- humanoid_locomotion
- fall_recovery
- adversarial_motion_prior
- behavior_conditioning
- proprioceptive_policy
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.23916);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.23916 ReLoco: Unified Humanoid Locomotion and Fall Recovery via Behavior-Conditioned Motion Priors'
  url: https://arxiv.org/abs/2611.23916
  date: '2026-11-18'
  accessed_at: '2026-11-23'
---

## 概述

ReLoco 针对人形机器人既要保持直立行走又需从跌倒中恢复并继续执行指令的问题，提出以行为条件化对抗运动先验为核心的统一学习框架。训练时根据机器人当前姿态选择对应的专家池，并用两个行为专用输出对共享判别器进行条件化，从而在同一策略中同时监督直立运动与地面接触恢复。任务奖励与共享正则化共同支撑指令跟踪和恢复行为，临时辅助机制则用于促进探索；此外还引入基于仿真的精炼阶段，为监督提供机器人实际执行的运动参考。消融实验在匹配设置下考察了条件监督、输出分离与参考质量的影响。在共同训练迭代下，完整策略取得 96.80% 的独立起身成功率和 96.96% 的推倒恢复成功率（含指令恢复），躯干平面速度 RMSE 为 0.1266 m/s，比条件化单输出变体低 14.7%，动态时间规整测得的关节角差异相近。最终在 64.5 kg 的 Tiangong 3.0 人形机器人上部署，用单一本体感知 actor 实现行走、奔跑、起身以及跌倒后的运动恢复。

## 核心内容

### 问题背景
人形机器人需要从跌倒中恢复并重新执行指令运动，才能维持持续运动能力。在单一策略中同时学习直立行走与地面接触恢复，需要一种能兼顾两类行为的监督方式，而现有方法难以在同一策略内统一处理。

### 方法
- 提出 ReLoco 框架，采用行为条件化的对抗运动先验。
- 训练时由机器人姿态选择专家池，并对共享判别器的两个行为专用输出进行条件化。
- 任务奖励与共享正则化共同支持指令跟踪与恢复行为。
- 引入临时辅助机制以促进探索。
- 设置基于仿真的精炼阶段，为监督提供机器人实际执行的运动参考。

### 实验设置
- 消融实验在匹配设置下考察条件监督、输出分离与参考质量的影响。
- 在共同训练迭代下评估完整策略与条件化单输出变体。

### 关键结果
- 完整策略实现 96.80% 的独立起身成功率。
- 推倒恢复成功率达 96.96%，且包含指令恢复。
- 躯干平面速度 RMSE 为 0.1266 m/s，比条件化单输出变体低 14.7%。
- 动态时间规整测得的关节角差异与对比变体相近。

### 结论
在 64.5 kg 的 Tiangong 3.0 人形机器人上部署后，单一本体感知 actor 即可完成行走、奔跑、起身以及跌倒后的运动恢复，无需控制器切换，也无需在机器人上进行策略微调。

## Overview

Humanoid robots must recover from falls and resume commanded motion to sustain locomotion. Learning these behaviors in one policy requires supervision that accommodates both upright movement and ground-contact recovery. We present ReLoco, a framework that uses behavior-conditioned adversarial motion priors to learn locomotion, get-up from arbitrary fallen postures, and command resumption within one proprioceptive policy. During training, robot posture selects the expert pool and conditions a shared discriminator with two behavior-specific outputs. Task rewards and shared regularization support command tracking and recovery, while temporary assistance facilitates exploration. A simulation-based refinement stage supplies robot-executed motion references for this supervision. Ablations examine conditional supervision, output separation, and reference quality under matched settings. At a common training iteration, the full policy achieves $96.80\%$ independent get-up success and $96.96\%$ push-recovery success, including command resumption. Its torso planar velocity root-mean-square error is $0.1266$~m/s, $14.7\%$ lower than the conditional single-output variant, with similar joint-angle discrepancy measured by dynamic time warping. Deployment on the 64.5-kg Tiangong~3.0 humanoid demonstrates walking, running, get-up, and locomotion resumption after falls using one proprioceptive actor, without controller switching or on-robot policy fine-tuning.

## 参考
- https://arxiv.org/abs/2611.23916
