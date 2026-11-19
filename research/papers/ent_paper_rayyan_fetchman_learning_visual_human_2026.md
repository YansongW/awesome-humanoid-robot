---
$id: ent_paper_rayyan_fetchman_learning_visual_human_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences'
  zh: 'FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences'
  ko: 'FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences'
summary:
  en: Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics
    research. However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation,
    and even more so for humanoids that must also walk and balance. Learning from simulated data and transferring that behavior
    to the real world, as is ...
  zh: FetchMan 是由 Omar Rayyan 等人提出的视觉人形机器人移动操作策略，通过从模拟经验中学习实现零样本部署。其核心贡献是提出一种结合行为克隆与 Flow-GRPO 强化学习的端到端 sim-to-real 流水线，在超过
    150,000 个场景上训练，并在真实 Unitree G1 机器人上达到 73.3% 的单物体到达-抓取成功率。
  ko: Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics
    research. However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation,
    and even more so for humanoids that must also walk and balance. Learning from simulated data and transferring that behavior
    to the real world, as is ...
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
- humanoid_locomotion
- manipulation_policy
- reinforcement_learning
- behavior_cloning
- zero_shot_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.17027);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.17027 FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences'
  url: https://arxiv.org/abs/2608.17027
  date: '2026-08-17'
  accessed_at: '2026-08-24'
- id: src_002
  type: website
  title: Project page
  url: https://orayyan.com/fetchman
  accessed_at: '2026-08-24'
---

## 概述

该研究针对人形机器人视觉移动操作策略难以泛化到新场景和物体的问题，借鉴运动控制领域从模拟数据学习并迁移到真实世界的成功经验。作者发现单纯克隆合成演示数据存在性能上限，而通过 Flow-GRPO 强化学习对克隆策略进行精炼，在单一稀疏奖励下即可突破该上限。他们构建了覆盖超过 150,000 个场景的端到端 sim-to-real 流水线，训练出 FetchMan 策略，并在模拟基准 FetchMan-Bench 上评估，同时在真实 Unitree G1 机器人上实现零样本部署。此外，该工作还探索了多物体训练，为移动操作通用策略迈出第一步。

## 核心内容

### 问题背景
视觉移动操作策略需要同时处理感知、导航、平衡和操作，其泛化能力是机器人研究长期追求的目标。然而，现有算法对数据需求极大，桌面操作已难以收集足够演示，人形机器人还需兼顾行走与平衡，数据收集更为困难。运动控制领域已证明从模拟数据学习并迁移到真实世界的有效性，本研究将该范式复制到移动操作任务中。

### 方法
- **行为克隆阶段**：从合成演示中克隆策略，但实验发现无论训练数据量如何增加，克隆策略的性能始终存在较低的天花板。
- **强化学习精炼阶段**：使用 Flow-GRPO 算法，在单一稀疏奖励下对克隆策略进行精炼，成功突破性能上限，达到合成行为克隆无法企及的水平。
- **端到端流水线**：上述两个阶段共同构成完整的 sim-to-real 流水线，覆盖超过 150,000 个场景，用于训练 FetchMan 策略。

### 实验设置与结果
- **模拟评估**：在作者发布的仿真基准 FetchMan-Bench 上评估 FetchMan 策略。
- **真实部署**：将策略零样本部署到真实 Unitree G1 人形机器人上，单物体到达-抓取策略在未见场景中行走并抓取目标，成功率达到 73.3%。
- **多物体扩展**：将流水线扩展到多物体训练，这是在该数据规模下迈向移动操作通用策略的第一步。

### 结论
该工作验证了从模拟经验学习视觉人形移动操作策略的可行性，通过行为克隆与强化学习结合的方式克服了合成数据克隆的性能瓶颈，并展示了在真实机器人上的零样本泛化能力。多物体训练的探索为未来构建通用移动操作策略奠定了基础。

## Overview

Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research. However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation, and even more so for humanoids that must also walk and balance. Learning from simulated data and transferring that behavior to the real world, as is commonly done in locomotion, sidesteps this struggle, so we replicate that recipe for loco-manipulation. In doing so, we find that cloning synthetic demonstrations results in a low performance ceiling no matter the amount of training data. Reinforcement learning breaks through it, and refining the cloned policy with Flow-GRPO on a single sparse reward yields performance that synthetic behavior cloning cannot match. Together, these stages form our end-to-end sim-to-real pipeline spanning more than 150,000 scenes, which we use to train FetchMan. We evaluate it on FetchMan-Bench, a simulation benchmark we release, and deploy it zero-shot on a real Unitree G1, where our single-object reach-and-pick policy walks to and grasps a target across unseen scenes at 73.3% success. Finally, we extend this recipe to multi-object training, a first step toward loco-manipulation generalist policies at this data scale.

## 参考
- https://arxiv.org/abs/2608.17027
- https://orayyan.com/fetchman
