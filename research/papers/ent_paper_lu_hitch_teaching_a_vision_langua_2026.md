---
$id: ent_paper_lu_hitch_teaching_a_vision_langua_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness'
  zh: 'HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness'
  ko: 'HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness'
summary:
  en: Enabling vision-language models (VLMs) to control humanoid robots requires both reliable whole-body interfaces and knowledge
    of how to use the body that carries over across tasks. We present HITCH (Harness Interfaces To Command Humanoids), a harness
    in which perception returns the 3D position of any point the VLM selects in its image, and execution turns commands for
    the pelvis, torso, hands, ...
  zh: HITCH（Harness Interfaces To Command Humanoids）是一个面向人形机器人的全身操控框架，由 Qingzhou Lu、Chenxin Liu、Xinming Wang、Liu Cao、Yanjiang
    Guo、Mengdi Xu、Jianyu Chen 提出。该框架让视觉语言模型通过图像选点获得三维位置感知，并借助学习到的跟踪器把骨盆、躯干、手、行走与注视指令转化为全身运动。作者在此基础上微调 VLM，使其学会操作人形机器人，在无任务专属轨迹时完成
    51% 的 SIMPLE 回合与 42.5% 的 HumanoidArena 回合，每任务补充五条轨迹后 SIMPLE 成功率升至 95%。
  ko: Enabling vision-language models (VLMs) to control humanoid robots requires both reliable whole-body interfaces and knowledge
    of how to use the body that carries over across tasks. We present HITCH (Harness Interfaces To Command Humanoids), a harness
    in which perception returns the 3D position of any point the VLM selects in its image, and execution turns commands for
    the pelvis, torso, hands, ...
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
- vision_language_model
- humanoid_robot
- whole_body_control
- robot_learning
- imitation_learning
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.08039);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.08039 HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness'
  url: https://arxiv.org/abs/2611.08039
  date: '2026-11-05'
  accessed_at: '2026-11-09'
- id: src_002
  type: website
  title: Project page
  url: https://hitch.axell.top/
  accessed_at: '2026-11-09'
---

## 概述

该工作关注如何让视觉语言模型可靠地控制人形机器人，认为关键在于两件事：一是可用的全身接口，二是能够跨任务迁移的身体使用知识。为此作者构建了 HITCH 框架，感知端返回 VLM 在图像中所选任意点的三维位置，执行端则通过一个学习到的跟踪器把骨盆、躯干、手、行走和注视指令合成为全身动作。作者发现，准确测量场景与准确执行命令都能提升任务成功率。随后他们用教师策略通过 HITCH 完成五个基础任务的轨迹对 VLM 进行微调，使其习得操作人形机器人的能力。在没有任务专属轨迹的情况下，微调后的模型在 SIMPLE 上完成 51% 的回合、在 HumanoidArena 上完成 42.5% 的回合；为每个 SIMPLE 任务增加五条轨迹后，SIMPLE 成功率提升到 95%。在真实的 G1 上，该模型无需真实训练数据即可搬箱并走向目标。

## 核心内容

### 问题背景

让视觉语言模型（VLM）控制人形机器人面临两方面需求：既需要可靠的全身接口，也需要关于如何使用身体、且能跨任务迁移的知识。作者围绕这两点构建了统一的框架与训练流程。

### 方法

- **HITCH 框架**：全称为 Harness Interfaces To Command Humanoids。感知侧返回 VLM 在其图像中选定的任意点的三维位置；执行侧将针对骨盆、躯干、手、行走与注视的命令，通过一个学习到的跟踪器转换为全身运动。
- **关键观察**：作者发现，准确测量场景与准确执行命令这两者都能提高任务成功率。
- **VLM 微调**：在教师策略通过 HITCH 求解五个基础任务所产生的轨迹上对 VLM 进行微调，使其学会如何操作人形机器人。

### 实验设置与关键结果

- 在无任务专属轨迹的条件下，微调后的模型完成 51% 的 SIMPLE 回合与 42.5% 的 HumanoidArena 回合。
- 为每个 SIMPLE 任务增加五条轨迹后，SIMPLE 成功率提升至 95%。
- 在真实 G1 机器人上，模型在没有真实训练数据的情况下完成搬箱并走向目标的动作。

### 结论

HITCH 通过统一的感知—执行接口把 VLM 与全身运动连接起来，并证明借助教师策略生成的轨迹进行微调，可以让 VLM 获得可迁移的人形机器人操作能力，且能迁移到真实硬件。

## Overview

Enabling vision-language models (VLMs) to control humanoid robots requires both reliable whole-body interfaces and knowledge of how to use the body that carries over across tasks. We present HITCH (Harness Interfaces To Command Humanoids), a harness in which perception returns the 3D position of any point the VLM selects in its image, and execution turns commands for the pelvis, torso, hands, walking, and gaze into whole-body motion with a learned tracker. We find that both measuring the scene and executing commands accurately raise task success. We then fine-tune a VLM on trajectories in which teacher policies solve five base tasks through HITCH, so that it learns how to operate the humanoid. Without task-specific trajectories, the fine-tuned model completes 51% of SIMPLE episodes and 42.5% of HumanoidArena episodes, and adding five trajectories per SIMPLE task raises its SIMPLE success to 95%. On a real G1, it carries a box and walks to a goal without real training data.

## 参考
- https://arxiv.org/abs/2611.08039
- https://hitch.axell.top/
