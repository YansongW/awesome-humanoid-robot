---
$id: ent_paper_schuck_learning_loco_manipulation_fro_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL
  zh: Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL
  ko: Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL
summary:
  en: Integrating locomotion and manipulation is essential for robot autonomy, but scaling standard Reinforcement Learning
    (RL) to complex tasks is severely bottlenecked by the slow, manual process of dense reward shaping. To bypass this limitation,
    we leverage Sample-based Model Predictive Control (SMPC) entirely in simulation as an automated, rapidly tunable expert
    to generate massive offline ...
  zh: 本文提出一种从SMPC演示中学习移动操作技能的新框架，利用模拟中的样本模型预测控制（SMPC）作为自动专家生成大规模离线数据，结合稀疏奖励的离策略强化学习（RL）训练高层策略，并与低层动态稳定控制器集成，使学习策略超越原始最优控制教师。该方法在配备机械臂的Spot四足机器人和G1人形机器人上验证了跨形态的鲁棒性。
  ko: Integrating locomotion and manipulation is essential for robot autonomy, but scaling standard Reinforcement Learning
    (RL) to complex tasks is severely bottlenecked by the slow, manual process of dense reward shaping. To bypass this limitation,
    we leverage Sample-based Model Predictive Control (SMPC) entirely in simulation as an automated, rapidly tunable expert
    to generate massive offline ...
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
- loco_manipulation
- sparse_reward_rl
- model_predictive_control
- sim_to_real
- quadruped
- humanoid
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-17'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-17). Bibliographic metadata from arXiv API (2608.12063);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2608.12063 Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL
  url: https://arxiv.org/abs/2608.12063
  date: '2026-08-12'
  accessed_at: '2026-08-17'
---

## 概述

该研究旨在解决强化学习在复杂移动操作任务中因密集奖励设计缓慢而受限的问题。作者完全在模拟中使用基于样本的模型预测控制（SMPC）作为可快速调整的专家，自动生成大规模离线数据集，从而解决探索难题。通过仅使用稀疏任务奖励训练离策略RL智能体，显著减少学习新技能的时间并消除手动调参需求。将高层智能体与低层动态稳定控制器集成，可产生更优行为并严格对齐真实任务目标，最终使学习策略超越原始最优控制教师。该模拟到现实框架在配备机械臂的Spot四足机器人和G1人形机器人上成功部署，验证了其跨形态的鲁棒性。

## 核心内容

### 问题背景
将移动与操作集成对机器人自主性至关重要，但标准强化学习（RL）在复杂任务中的扩展受限于密集奖励塑形的缓慢手动过程。传统方法需要精心设计奖励函数以引导探索，这成为技能学习的瓶颈。

### 方法
- **SMPC专家生成数据**：完全在模拟环境中使用基于样本的模型预测控制（SMPC）作为自动化、可快速调整的专家，生成大规模离线数据集。该数据解决了基本探索问题，使离策略RL智能体能够仅使用稀疏任务奖励进行训练。
- **分层架构**：高层RL智能体负责任务决策，低层动态稳定控制器确保运动稳定性。这种集成产生更优行为，严格对齐真实任务目标。
- **训练效率**：稀疏奖励设计大幅减少学习新技能所需时间，并消除手动调参需求。

### 实验设置与结果
- **跨形态验证**：在两种不同形态上部署复杂移动操作技能：配备机械臂的Spot四足机器人和G1人形机器人。
- **性能超越**：学习策略在任务目标上超越原始最优控制教师（SMPC），表明RL智能体能够优化超出专家演示的行为。
- **模拟到现实迁移**：框架的鲁棒性通过成功部署得到验证，未提及具体实验数字或额外设置。

### 结论
该工作展示了利用SMPC演示结合稀疏奖励RL的有效性，为复杂移动操作任务提供了一种无需密集奖励设计的自动化学习途径，并在多形态机器人上验证了其通用性和迁移能力。

## Overview

Integrating locomotion and manipulation is essential for robot autonomy, but scaling standard Reinforcement Learning (RL) to complex tasks is severely bottlenecked by the slow, manual process of dense reward shaping. To bypass this limitation, we leverage Sample-based Model Predictive Control (SMPC) entirely in simulation as an automated, rapidly tunable expert to generate massive offline datasets. Because this data solves the fundamental exploration problem, we can train an off-policy RL agent using purely sparse task rewards, drastically reducing the time required to learn new skills and eliminating the need for manual tuning. Integrating this high-level agent with a low-level dynamic stability controller yields more optimal behaviors that strictly align with true task objectives, ultimately allowing the learned policies to surpass the original optimal control teacher. We validate the robustness of this sim-to-real framework by successfully deploying complex loco-manipulation skills across different morphologies, including an arm-equipped Spot quadruped and a G1 humanoid.

## 参考
- https://arxiv.org/abs/2608.12063
