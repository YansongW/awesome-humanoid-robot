---
$id: ent_paper_jia_roboassist_interactive_human_h_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboAssist: Interactive Human-Humanoid Planning for Long-Horizon Surgical Assistance'
  zh: 'RoboAssist: Interactive Human-Humanoid Planning for Long-Horizon Surgical Assistance'
  ko: 'RoboAssist: Interactive Human-Humanoid Planning for Long-Horizon Surgical Assistance'
summary:
  en: Long-horizon surgical assistance requires humanoid robots to coordinate with evolving human activities while maintaining
    safety across planning and execution. We present RoboAssist, an agent-based framework for interactive human-humanoid planning
    that integrates workflow reasoning, task coordination, and cross-layer safety. At its core is an asymmetric dual-track
    representation that separates ...
  zh: RoboAssist 是一个面向长时程手术辅助的基于智能体的交互式人-人形机器人规划框架，由 Jingwei Jia、Keyu Zhou、Jiewei Wang、Peisen Xu、Xingyuan Zhou、Liang Wang、Jiming
    Chen、Gaofeng Li 等人提出。其核心是非对称双轨表示，将部分可观测的人类流程状态与可执行的机器人任务序列分离，并在工作流请求变化时仅重规划受影响的后续片段。框架在 Unitree G1 人形机器人上于多阶段仿真手术辅助场景中验证，涵盖多模态交互、器械处理、医疗物资运输、导航与安全人机交接。
  ko: Long-horizon surgical assistance requires humanoid robots to coordinate with evolving human activities while maintaining
    safety across planning and execution. We present RoboAssist, an agent-based framework for interactive human-humanoid planning
    that integrates workflow reasoning, task coordination, and cross-layer safety. At its core is an asymmetric dual-track
    representation that separates ...
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
- surgical_assistance
- task_and_motion_planning
- human_robot_handover
- runtime_safety
- long_horizon_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.39384);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.39384 RoboAssist: Interactive Human-Humanoid Planning for Long-Horizon Surgical Assistance'
  url: https://arxiv.org/abs/2609.39384
  date: '2026-09-30'
  accessed_at: '2026-10-05'
- id: src_002
  type: website
  title: Project page
  url: https://roboassist.github.io
  accessed_at: '2026-10-05'
---

## 概述

RoboAssist 针对长时程手术辅助场景，提出一个基于智能体的交互式人-人形机器人规划框架，把工作流推理、任务协调与跨层安全整合在一起。框架的核心是非对称双轨表示，将部分可观测的人类流程状态与机器人可执行任务序列分开建模，并通过在线更新人类流程估计、场景上下文与任务依赖，对剩余任务序列重新校验，在工作流请求变化时只重规划受影响的后续片段。安全方面采用跨层架构，结合预防性导航调节、近距离交接时的反应式调节，以及独立的全身运行时监督。作者在 Unitree G1 人形机器人上，于长时程多阶段仿真手术辅助场景中进行了演示，覆盖多模态交互、器械处理、医疗物资运输、导航与安全人机交接。实验显示多阶段任务能够完成并适应工作流请求变化；针对性的全量重规划消融表明，残差重规划降低了计划更新延迟与更新后的 token 用量，独立的安全实验则显示导航、交接与运行时监督三方面具有互补的保护作用。

## 核心内容

### 问题背景
长时程手术辅助要求人形机器人在规划与执行全过程中与不断变化的人类活动相协调，并持续保持安全。这一场景同时涉及工作流推理、任务协调与跨层安全，难度在于人类流程状态只能被部分观测，而机器人任务序列必须可执行且能随工作流请求变化而调整。

### 方法
- **非对称双轨表示**：将部分可观测的人类流程状态与可执行的机器人任务序列分离表示，作为框架的核心。
- **在线更新与残差重规划**：在线更新人类流程估计、场景上下文与任务依赖，据此重新校验剩余任务序列；当工作流请求发生变化时，只重规划受影响的后续片段（suffix），而非整体重规划。
- **跨层安全架构**：结合预防性导航调节、近距离交接过程中的反应式调节，以及独立的全身运行时监督，使在线任务协调与安全约束在执行全程相互耦合。

### 实验设置
- 平台：Unitree G1 人形机器人。
- 场景：长时程、多阶段仿真手术辅助场景，涵盖多模态交互、器械处理、医疗物资运输、导航以及安全的人机交接。
- 消融：针对性的全量重规划消融实验。
- 安全实验：分别针对导航、交接与运行时监督的独立安全实验。
- 更多结果与演示见 https://roboassist.github.io。

### 关键结果
- 实验展示了多阶段任务的完成能力，以及对工作流请求变化的适应能力。
- 全量重规划消融显示，残差重规划降低了计划更新延迟，并减少了更新后的 token 用量。
- 独立的安全实验表明，导航、交接与运行时监督三方面提供了互补的保护。

### 结论
RoboAssist 通过非对称双轨表示与残差重规划，将在线任务协调与跨层安全约束贯穿执行过程，在 Unitree G1 上验证了长时程多阶段手术辅助任务的完成与对工作流变化的适应能力。

## Overview

Long-horizon surgical assistance requires humanoid robots to coordinate with evolving human activities while maintaining safety across planning and execution. We present RoboAssist, an agent-based framework for interactive human-humanoid planning that integrates workflow reasoning, task coordination, and cross-layer safety. At its core is an asymmetric dual-track representation that separates partially observed human process states from executable robot task sequences. By updating human-process estimates, scene context, and task dependencies online, RoboAssist revalidates the remaining task sequence and replans only the affected suffix when workflow requests change. A cross-layer safety architecture combines preventive navigation regulation, reactive regulation during close-range handover, and independent whole-body runtime supervision. This design couples online task coordination with safety constraints throughout execution. We demonstrate the framework on a Unitree G1 humanoid robot in long-horizon, multi-stage simulated surgical assistance scenarios encompassing multimodal interaction, instrument handling, medical material transport, navigation, and safe human-robot handover. Experiments show multi-stage task completion and adaptation to workflow-request changes. A targeted full-replanning ablation shows that residual replanning reduces plan-update latency and post-update token usage. Separate safety experiments demonstrate complementary protection across navigation, handover, and runtime supervision. Additional results and demonstrations are available online at https://roboassist.github.io.

## 参考
- https://arxiv.org/abs/2609.39384
- https://roboassist.github.io
