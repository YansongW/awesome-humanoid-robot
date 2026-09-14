---
$id: ent_paper_he_roboreact_agentic_skill_distil_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation'
  zh: 'RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation'
  ko: 'RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation'
summary:
  en: Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and
    generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances
    in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual observations,
    but transferring such ...
  zh: RoboReact 是一个从单目 RGB-D 观测自动合成全身人形操作技能的框架，由 Shuliang He 等人提出。它通过生成人类操作视频、深度感知 3D 重建提取关键帧，并重定向到高自由度人形平台，结合在线对象中心重定位和视觉语言模型引导的优化循环，实现无需遥操作或人类演示的泛化操作。实验在真实人形机器人上验证了其跨对象配置的泛化性和对执行扰动的鲁棒恢复能力。
  ko: Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and
    generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances
    in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual observations,
    but transferring such ...
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
- whole_body_manipulation
- video_generation
- skill_distillation
- humanoid_robots
- vision_language_model
- closed_loop_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-10'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-10). Bibliographic metadata from arXiv API (2608.03387);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.03387 RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body
    Manipulation'
  url: https://arxiv.org/abs/2608.03387
  date: '2026-08-04'
  accessed_at: '2026-08-10'
---

## 概述

RoboReact 旨在解决人形机器人技能获取成本高昂的问题，利用视频生成模型合成丰富的操作经验，并将其转化为可执行的全身技能。该框架从单个 RGB-D 观测出发，生成人类操作视频，通过深度感知 3D 重建提取保持几何结构的关键帧，并重定向到高自由度人形平台，同时保留手-物交互几何。为弥合想象计划与物理执行之间的差距，RoboReact 采用在线对象中心重定位和视觉语言模型引导的优化循环，适应几何失配和执行偏差。最终通过全身控制器执行技能，实现协调的全身操作和灵巧交互，实验表明其无需遥操作或人类演示即可泛化并鲁棒恢复。

## 核心内容

### 问题背景
人形机器人在人类环境中执行灵巧操作潜力巨大，但获取多样且可泛化的技能成本高昂，主要源于硬件数据采集昂贵和标注劳动密集。视频生成模型的最新进展为从视觉观测合成丰富操作经验提供了机会，但将这种想象行为转化为可执行的全身人形技能仍未被充分探索。

### 方法
RoboReact 框架从单个 egocentric RGB-D 观测自动合成全身操作技能，流程包括：
- **视频生成与关键帧提取**：生成人类操作视频，通过深度感知 3D 重建提取保持几何结构（geometry-preserving）的交互关键帧。
- **重定向**：将关键帧重定向到高自由度（high-DoF）人形平台，同时保留手-物交互几何。
- **在线重定位**：执行过程中进行对象中心重定位（object-centric re-grounding），适应几何失配。
- **优化循环**：利用视觉语言模型（VLM）引导的优化循环，根据执行偏差调整技能。
- **全身控制**：通过全身控制器执行精炼后的技能，实现协调的全身操作和灵巧交互。

### 实验设置与结果
实验在真实人形机器人上进行，评估了跨多种对象配置的泛化能力，以及面对执行扰动时的鲁棒恢复能力。结果显示，RoboReact 无需遥操作或人类演示即可实现泛化，并能从执行干扰中稳健恢复。

### 结论
RoboReact 展示了生成模型、视觉语言推理和闭环控制相结合用于可扩展人形技能获取的潜力，为降低数据采集成本提供了新途径。

## Overview

Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual observations, but transferring such imagined behaviors into executable whole-body humanoid skills remains largely unexplored. In this work, we present RoboReact, a framework that automatically synthesizes whole-body humanoid manipulation skills from a single egocentric RGB-D observation. RoboReact generates human manipulation videos, extracts geometry-preserving interaction keyframes through depth-aware 3D reconstruction, and retargets them to high-DoF humanoid platforms while preserving hand-object interaction geometry. To bridge the gap between imagined plans and physical execution, RoboReact performs online object-centric re-grounding and leverages a vision-language model-guided refinement loop to adapt skills under geometric mismatch and execution deviations. The refined skills are executed through a whole-body controller, enabling coordinated whole-body manipulation and dexterous interaction. Experiments on real humanoid robots demonstrate that RoboReact generalizes across diverse object configurations and robustly recovers from execution disturbances without requiring teleoperation or human demonstrations. These results highlight the potential of combining generative models, vision-language reasoning, and closed-loop control for scalable humanoid skill acquisition.

## 参考
- https://arxiv.org/abs/2608.03387
