---
$id: ent_paper_snegirev_orcestra_vlm_driven_visual_rob_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality'
  zh: 'ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality'
  ko: 'ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality'
summary:
  en: ORCESTRA is a mixed-reality system for programming robot digital twins through no-code waypoint teaching and language-guided
    control. In a passthrough mixed-reality workspace, users place robot twins on real surfaces, teach trajectories, save
    robot-relative episodes, or issue spoken/typed commands that a vision-language model converts into structured digital-twin
    plans. Both interaction modes ...
  zh: ORCESTRA 是一个混合现实系统，用于通过无代码路径点示教和语言引导控制来编程机器人数字孪生。该系统由俄罗斯团队（包括 Dzmitry Tsetserukou 等）开发，支持固定基座机械臂、移动基座和人形机器人等多种异构机器人形态，并将混合现实验证作为物理部署前的安全层。
  ko: ORCESTRA is a mixed-reality system for programming robot digital twins through no-code waypoint teaching and language-guided
    control. In a passthrough mixed-reality workspace, users place robot twins on real surfaces, teach trajectories, save
    robot-relative episodes, or issue spoken/typed commands that a vision-language model converts into structured digital-twin
    plans. Both interaction modes ...
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
- mixed_reality
- digital_twin
- language_guided_programming
- vision_language_model
- robot_programming
- safety_validation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-04'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-04). Bibliographic metadata from arXiv API (2608.00775);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.00775 ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality'
  url: https://arxiv.org/abs/2608.00775
  date: '2026-08-01'
  accessed_at: '2026-08-04'
---

## 概述

ORCESTRA 在透视式混合现实工作空间中运行，用户可将机器人数字孪生放置在真实表面上，通过示教轨迹、保存机器人相对片段或发出语音/文本命令来编程机器人。语音/文本命令由视觉语言模型转换为结构化数字孪生计划，两种交互模式共享同一后端，用于度量接地、具身感知验证、预览、确认和数字孪生执行。该系统支持多种机器人形态，并展示了混合现实验证作为语言引导机器人编程安全层的价值。

## 核心内容

### 问题背景
语言引导的机器人编程在物理部署前缺乏直观、安全的验证手段。传统方法要么依赖代码调试，要么缺乏对机器人具身约束的感知，容易导致执行错误或安全事故。ORCESTRA 旨在通过混合现实中的数字孪生编程，提供一种无代码、语言友好的编程范式，并在物理执行前进行安全验证。

### 方法
ORCESTRA 采用透视式混合现实工作空间，用户可将机器人数字孪生放置在真实表面上。系统提供两种交互模式：
- **无代码路径点示教**：用户直接示教轨迹，保存机器人相对片段，无需编写代码。
- **语言引导控制**：用户发出语音或文本命令，由视觉语言模型（VLM）将其转换为结构化的数字孪生计划。

两种模式共享同一后端，该后端负责度量接地（metric grounding）、具身感知验证（embodiment-aware validation）、预览、确认和数字孪生执行。度量接地确保语言命令与真实空间坐标对齐；具身感知验证检查计划是否符合机器人运动学与动力学约束。

### 实验设置与关键结果
系统支持多种异构机器人形态，包括固定基座机械臂、移动基座和全尺寸人形机器人。实验展示了 ORCESTRA 在混合现实环境中对上述机器人进行编程与验证的能力，并验证了混合现实验证作为语言引导机器人编程安全层的有效性——即在物理部署前，通过数字孪生执行计划，发现并修正潜在问题。

### 结论
ORCESTRA 提供了一种统一的混合现实编程框架，将无代码示教与语言引导控制结合，并通过具身感知验证提升安全性。该系统为异构机器人平台提供了一种可扩展的编程与验证方案，尤其适用于需要快速迭代与安全部署的场景。

## Overview

ORCESTRA is a mixed-reality system for programming robot digital twins through no-code waypoint teaching and language-guided control. In a passthrough mixed-reality workspace, users place robot twins on real surfaces, teach trajectories, save robot-relative episodes, or issue spoken/typed commands that a vision-language model converts into structured digital-twin plans. Both interaction modes share a backend for metric grounding, embodiment-aware validation, preview, confirmation, and digital-twin execution. The system supports heterogeneous robot embodiments, including fixed-base manipulators, a mobile base, and a humanoid robot, demonstrating MR validation as a safety layer for language-guided robot programming before physical deployment.

## 参考
- https://arxiv.org/abs/2608.00775
