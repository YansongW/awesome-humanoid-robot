---
$id: ent_paper_dai_navrsi_recursive_harness_self_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation'
  zh: 'NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation'
  ko: 'NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation'
summary:
  en: Frontier large language models (LLMs) have enabled vision-and-language navigation (VLN) through direct closed-loop perception
    and action. However, navigation performance depends strongly on the harness governing LLM-environment interactions, while
    existing harnesses largely rely on manually designed navigation tools, memory, and agent roles. We introduce NavRSI, a
    harness-centric recursive ...
  zh: NavRSI 是一个以 harness 为中心的递归自我改进框架，由 Guangzhao Dai 等人提出，用于提升冻结大语言模型在视觉语言导航（VLN）中的表现。它通过闭环经验迭代收集导航轨迹与失败诊断，由 designer agent
    重写 harness 并保留有效修订，使 harness 与设计经验协同演化。在 R2R-CE val-unseen 划分上，配合 GPT-6-Astra 达到 85.64% 成功率，较此前报告的最佳结果提升 4.13%。
  ko: Frontier large language models (LLMs) have enabled vision-and-language navigation (VLN) through direct closed-loop perception
    and action. However, navigation performance depends strongly on the harness governing LLM-environment interactions, while
    existing harnesses largely rely on manually designed navigation tools, memory, and agent roles. We introduce NavRSI, a
    harness-centric recursive ...
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
- vision_and_language_navigation
- recursive_self_improvement
- harness_optimization
- large_language_models
- humanoid_robot
- closed_loop_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.27499);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.27499 NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation'
  url: https://arxiv.org/abs/2611.27499
  date: '2026-11-20'
  accessed_at: '2026-11-23'
---

## 概述

NavRSI 针对视觉语言导航中导航性能高度依赖 LLM 与环境交互所依托的 harness、而现有 harness 多依赖人工设计的导航工具、记忆与智能体角色这一问题，提出以 harness 为中心的递归自我改进框架。该方法在每一轮中迭代采集导航轨迹与失败诊断，由 designer agent 改写 harness，并保留被证明有效的修订，同时 designer 从既往修订中积累经验，实现 harness 与经验的共同演化。特权仿真器诊断仅用于指导 designer，导航 LLM 无法访问，因此部署时仅需单个 RGB 相机与基础动作，无需任务特定的模型训练或额外导航工具。实验在来自四家厂商的多个 LLM 上均取得一致提升，其中 GPT-6-Astra 在完整 R2R-CE val-unseen 划分上成功率达 85.64%，超过此前报告的最佳结果 4.13%。在 RxR-CE、NavRAG-CE 以及一台真实人形机器人上的评测进一步验证了其泛化能力。

## 核心内容

### 问题背景

前沿大语言模型已能通过直接的闭环感知与动作实现视觉语言导航（VLN），但导航表现强烈依赖于约束 LLM 与环境交互的 harness。现有 harness 大多依赖人工设计的导航工具、记忆机制与智能体角色，限制了性能的进一步提升与迁移。

### 方法

NavRSI 是一个以 harness 为中心的递归自我改进框架，通过闭环经验优化冻结 LLM 的导航行为：

- 每一轮迭代采集导航轨迹与失败诊断；
- 由 designer agent 重写 harness；
- 保留被证明有效的修订；
- designer 从既往修订中积累经验，使 harness 与该经验协同演化。

特权仿真器诊断仅用于指导 designer，导航 LLM 无法访问这些信息。因此部署阶段仅需单个 RGB 相机与基础动作，无需任务特定的模型训练，也无需额外的导航工具。

### 实验设置与关键结果

- 在来自四家厂商的多个 LLM 上均观察到一致的性能提升。
- 使用 GPT-6-Astra 在完整 R2R-CE val-unseen 划分上取得 85.64% 的成功率，较此前报告的最佳结果高出 4.13%。
- 在 RxR-CE、NavRAG-CE 以及一台真实人形机器人上的评测进一步展示了方法的泛化性。

### 结论

NavRSI 表明，通过递归地自我改进 harness，可在不训练模型、不引入额外导航工具的条件下显著提升冻结 LLM 的视觉语言导航能力，并具备跨数据集与真实人形机器人平台的泛化潜力。

## Overview

Frontier large language models (LLMs) have enabled vision-and-language navigation (VLN) through direct closed-loop perception and action. However, navigation performance depends strongly on the harness governing LLM-environment interactions, while existing harnesses largely rely on manually designed navigation tools, memory, and agent roles. We introduce NavRSI, a harness-centric recursive self-improvement framework that optimizes the navigation behavior of frozen LLMs through closed-loop experience. In each round, NavRSI iteratively collects navigation trajectories and failure diagnostics, employs a designer agent to rewrite the harness, and retains the revisions that prove effective, while the designer accumulates experience from previous revisions so that the harness and this experience co-evolve. Privileged simulator diagnostics guide only the designer and remain inaccessible to the navigating LLM, enabling deployment with a single RGB camera and primitive actions, without task-specific model training or additional navigation tools. Experiments demonstrate consistent improvements across LLMs from four vendors, with 85.64% success rate on the full R2R-CE val-unseen split with GPT-6-Astra, surpassing the previously reported best by 4.13%. Evaluations on RxR-CE, NavRAG-CE, and a real humanoid robot further demonstrate its generalizability.

## 参考
- https://arxiv.org/abs/2611.27499
