---
$id: ent_paper_zhang_actor_ambient_ai_based_agentic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms'
  zh: 'ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms'
  ko: 'ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms'
summary:
  en: 'Operating rooms (ORs) increasingly contain ambient sensing infrastructure to enable AI-based optimization of workflows
    and utilization. We pursue an alternative path: using ambient AI to guide robot action and optimize utilization. Deploying
    humanoids in the OR without ambient AI is severely limited by cumbersome de novo orientation and planning due to partial
    onboard observations. We posit that ...'
  zh: ActOR 是一种面向手术室（OR）人形机器人自主性的环境 AI 智能体编排框架，由 Han Zhang、Sicheng Lu、Aleks Santari、Jeffrey K. Jopling、Masaru Ishii、Mathias
    Unberath 提出。该方法将壁挂式环境相机与机器人头部相机融合为共享的物体级数字孪生（DT），并由大语言模型智能体在 DT 上调度预编程的移动与操作技能，无需任务特定训练。在仿真与实体环境中，环境感知将目标不在视野内时的探索调用从每试次
    1.05 次降至 0.12 次，闭环反馈将标称执行成功率从 46.7% 提升至 83.3%，在注入扰动下从 8.3% 提升至 51.7%。
  ko: 'Operating rooms (ORs) increasingly contain ambient sensing infrastructure to enable AI-based optimization of workflows
    and utilization. We pursue an alternative path: using ambient AI to guide robot action and optimize utilization. Deploying
    humanoids in the OR without ambient AI is severely limited by cumbersome de novo orientation and planning due to partial
    onboard observations. We posit that ...'
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
- ambient_ai
- humanoid_robotics
- agentic_orchestration
- digital_twin
- surgical_operating_room
- llm_agent
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.04255);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.04255 ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms'
  url: https://arxiv.org/abs/2611.04255
  date: '2026-11-03'
  accessed_at: '2026-11-09'
---

## 概述

手术室正越来越多地部署环境感知基础设施，以支持基于 AI 的工作流与利用率优化；ActOR 则探索另一条路径，即用环境 AI 直接引导机器人动作。研究团队指出，若缺乏环境 AI，人形机器人在手术室中会因机载观测不完整而面临繁琐的从零定向与规划难题。为此，他们将基于环境 AI 的智能体编排器与人形机器人执行者耦合，为手术室中的人形自主性提供共享感知与执行反馈。ActOR 把壁挂环境相机与机器人头部相机融合为共享的物体级数字孪生，由大语言模型智能体在其上规划预编程的移动与操作技能，并在执行过程中依据 DT 更新与执行结果决定重试、换方案或重新规划。仿真与实体实验表明，环境观测提供的场景状态能显著提升规划成功率并减少探索，而将技能结果与 DT 更新回传给规划器可改善多步任务的成功率。

## 核心内容

### 问题背景
手术室中环境感知基础设施日益普及，现有工作多将其用于工作流与利用率的 AI 优化。本文关注另一方向：利用环境 AI 引导机器人动作。作者指出，在没有环境 AI 支持的情况下，人形机器人因机载观测只能覆盖局部视野，在手术室部署时需要进行繁琐的从零定向与规划，自主性受到严重限制。

### 方法
- **共享数字孪生（DT）**：ActOR 将壁挂式环境相机与机器人头部相机融合，构建物体级的共享数字孪生，作为规划与执行的共同场景表示。
- **智能体编排**：由大语言模型智能体在 DT 之上进行规划，调用预编程的移动与操作技能，无需针对具体任务进行训练。
- **闭环反馈**：执行过程中，DT 更新与执行结果回传给规划器，用于触发重试、采用替代方案或重新规划。

### 实验设置
评估在仿真与实体环境中进行：
- 仿真方面，基于两个由真实房间重建的手术室，设置三项任务。
- 实体方面，在配备人形机器人的模拟手术室（mock OR）中开展单物体处置试验。
- 扰动测试注入导航、物体移位与抓取三类扰动。

### 关键结果
- 当目标初始不在机器人视野内时，环境感知将探索调用从每试次 1.05 次降至 0.12 次。
- 闭环反馈使标称执行下的成功率从 46.7% 提升至 83.3%；在注入导航、物体移位与抓取扰动时，成功率从 8.3% 提升至 51.7%。
- 在实体模拟手术室中，ActOR 在 20 次单物体处置试验中完成 14 次，并展示了场景变化后的重新规划能力。

### 结论
基于环境 AI 的观测所提供的场景状态可改善机器人动作规划，相比仅依赖机器人自身观测，能提高成功率并减少探索；将技能执行结果与 DT 更新反馈给规划器可提升多步任务成功率。结果验证了人形机器人在模拟手术室中执行多步处置任务的任务级自主性可行性。

## Overview

Operating rooms (ORs) increasingly contain ambient sensing infrastructure to enable AI-based optimization of workflows and utilization. We pursue an alternative path: using ambient AI to guide robot action and optimize utilization. Deploying humanoids in the OR without ambient AI is severely limited by cumbersome de novo orientation and planning due to partial onboard observations. We posit that this can be achieved by coupling an ambient AI-based agentic orchestrator with the humanoid robotic actor, providing shared perception and execution feedback for humanoid autonomy in the OR. ActOR fuses a wall-mounted ambient camera and the robot's head-mounted camera into a shared object-level digital twin (DT). A large language model agent plans over the DT using pre-programmed locomotion and manipulation skills without task-specific training. During execution, DT updates and execution outcomes inform retries, alternative approaches, or replanning. We evaluated ActOR in simulated and physical environments. Across three tasks in two simulated ORs reconstructed from real rooms, ambient perception reduced exploration from 1.05 to 0.12 Explore calls per trial when targets were initially outside the robot's view. Closed-loop feedback increased success from 46.7% to 83.3% under nominal execution and from 8.3% to 51.7% under injected navigation, object-relocation, and grasp perturbations. In a physical mock OR with a humanoid, ActOR completed 14 of 20 single-object disposal trials and demonstrated replanning after scene changes. Ambient AI-based observations provide scene state that improves robot action planning, increasing success and reducing exploration compared with robot-only observations. Feeding skill outcomes and DT updates back to the planner improves multi-step task success. Our results show the feasibility of humanoid task autonomy for multi-step disposal tasks in a mock OR.

## 参考
- https://arxiv.org/abs/2611.04255
