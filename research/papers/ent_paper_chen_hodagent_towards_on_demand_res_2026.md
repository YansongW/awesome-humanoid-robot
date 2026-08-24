---
$id: ent_paper_chen_hodagent_towards_on_demand_res_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction'
  zh: 'HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction'
  ko: 'HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction'
summary:
  en: We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent,
    responsive execution, task revision, and outcome verification. Its semi-duplex architecture integrates an Env-Interactor,
    Planner, Executor, and hierarchical Memory to maintain coherent interaction, planning, and task state during service episodes.
    This allows handling new requests ...
  zh: HODAgent 是一种面向服务场景人形机器人的 System-2 具身智能体，由 Wang Warren Chen 等研究者提出，旨在解决情境化意图理解、响应式执行、任务修订与结果验证问题。其半双工架构整合环境交互器、规划器、执行器与分层记忆，在仿真和
    Unitree G1 实体机器人上均取得显著性能提升。
  ko: We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent,
    responsive execution, task revision, and outcome verification. Its semi-duplex architecture integrates an Env-Interactor,
    Planner, Executor, and hierarchical Memory to maintain coherent interaction, planning, and task state during service episodes.
    This allows handling new requests ...
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
- humanoid_robot
- embodied_agent
- system2_reasoning
- service_robot
- task_planning
- human_robot_interaction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.17584);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.17584 HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction'
  url: https://arxiv.org/abs/2608.17584
  date: '2026-08-18'
  accessed_at: '2026-08-24'
---

## 概述

HODAgent 采用半双工架构，通过环境交互器、规划器、执行器和分层记忆模块协同工作，在服务交互过程中维持连贯的交互、规划与任务状态。该系统能够在运动过程中处理新请求、保留进度、修订动作，并以执行结果作为闭环依据。通过共享接口连接仿真与实体机器人（Unitree G1），隔离平台特定控制逻辑。在包含 164 个案例的交互式仿真中，HODAgent 在两种 VLM 骨干下分别达到 84.8% 和 91.5% 的联合成功率，超越基线 9.8 和 18.9 个百分点；实体机器人上原子任务、复合任务和完整任务的通过率分别为 92%、72% 和 63.3%。

## 核心内容

### 问题背景
服务场景中的人形机器人需要应对动态、不可预测的人类交互，传统方法难以同时满足情境化意图理解、响应式执行、任务修订和结果验证等需求。现有系统通常缺乏统一的 System-2 推理层，难以在长时间服务交互中维持任务状态与适应性。

### 方法
HODAgent 采用半双工架构，包含四个核心模块：
- **环境交互器（Env-Interactor）**：感知环境状态并处理交互信号。
- **规划器（Planner）**：基于当前任务状态生成行动方案。
- **执行器（Executor）**：执行规划的动作并反馈结果。
- **分层记忆（Hierarchical Memory）**：维护短期与长期任务状态，支持进度保留与动作修订。

该架构允许系统在运动过程中接收新请求，保留已有进度，并根据执行结果调整后续动作。共享接口设计将仿真与实体机器人（Unitree G1）的平台特定控制逻辑隔离，便于跨平台迁移。

### 实验设置与结果
- **仿真实验**：在包含 164 个案例的交互式仿真环境中，HODAgent 在两种 VLM 骨干下分别取得 84.8% 和 91.5% 的联合成功率，较基线提升 9.8 和 18.9 个百分点。
- **实体机器人实验**：在 Unitree G1 上，原子任务通过率为 92%，复合任务为 72%，完整任务为 63.3%。
- **多具身基准测试**：在多个具身智能基准上，HODAgent 较基线提升 0.7 至 9.0 个百分点。

### 结论
结果表明，统一的 System-2 智能体架构能够使服务型人形机器人在仿真与现实环境中均实现自适应服务，验证了该方法的有效性与泛化能力。

## Overview

We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent, responsive execution, task revision, and outcome verification. Its semi-duplex architecture integrates an Env-Interactor, Planner, Executor, and hierarchical Memory to maintain coherent interaction, planning, and task state during service episodes. This allows handling new requests during motion, retaining progress, revising actions, and grounding closure in execution outcomes. A shared interface connects simulation and physical robots (Unitree G1), isolating platform-specific control. In an interactive simulation with 164 cases, HODAgent achieves 84.8% and 91.5% Joint Success under two VLM backbones, outperforming baselines by 9.8 and 18.9 points. On physical robots, pass rates are 92% (atomic), 72% (composite), and 63.3% (complete tasks). On multiple embodied benchmarks, it improves over baselines by 0.7-9.0 points. Results show a unified System-2 agent enables adaptive humanoid service across simulation and reality.

## 参考
- https://arxiv.org/abs/2608.17584
