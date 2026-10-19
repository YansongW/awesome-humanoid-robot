---
$id: ent_paper_kang_trace_typed_reference_aware_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion'
  zh: 'TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion'
  ko: 'TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion'
summary:
  en: Language-conditioned humanoid motion generation enables users to create and refine robot movements through natural language.
    The central challenge is to connect an underspecified request to concrete motion structure that can subsequently be revised
    relative to an accepted reference. We present TRACE, a generation and editing framework for the Unitree G1 humanoid robot
    built around typed, ...
  zh: TRACE 是面向 Unitree G1 人形机器人的运动生成与编辑框架，由 Zejian Kang、Yifu Luo、Boyang Shen 等人提出。其核心思路是以类型化、可度量的运动学量作为生成条件与编辑目标的共同基础：语言模型从运动数据中学习预测支撑、根节点与手部事件，并将其时间对齐编码与原始文本共同输入扩散生成器；编辑阶段则由类型化请求定义身体—时间范围与相对参考的目标，交由独立的参考条件扩散编辑器实现。定量评估与人工评测显示，该方法在语义对齐与运动质量上优于对比方法。
  ko: Language-conditioned humanoid motion generation enables users to create and refine robot movements through natural language.
    The central challenge is to connect an underspecified request to concrete motion structure that can subsequently be revised
    relative to an accepted reference. We present TRACE, a generation and editing framework for the Unitree G1 humanoid robot
    built around typed, ...
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
- humanoid_motion_generation
- motion_diffusion
- language_conditioned_control
- motion_editing
- unitree_g1
- kinematic_consistency
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.21515);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.21515 TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion'
  url: https://arxiv.org/abs/2610.21515
  date: '2026-10-15'
  accessed_at: '2026-10-19'
---

## 概述

TRACE 针对语言条件下人形机器人运动生成与迭代修改这一任务，关注如何把欠指定的自然语言请求落到具体、可修改的运动结构上。作者将生成条件锚定在成对的训练运动上，将编辑目标锚定在当前运动上，并以类型化、可度量的运动学量作为二者的共同表示。具体而言，一个语言模型从运动衍生的监督信号中学习预测支撑、根节点与手部事件，这些事件的时间对齐编码在扩散生成器中补充原始文本；重力参考状态与轨迹—接触目标进一步提升运动学一致性。编辑方面，类型化请求界定身体—时间范围与相对参考的目标，独立的参考条件扩散编辑器结合这些目标与修订后的事件完成修改，采样时投影则保护受保护的状态坐标。实验包含定量评估、人工评估、受控消融与多轮编辑评测，结果表明语义对齐与运动质量优于对比方法，且多轮相对请求在共享保持约束下执行更可靠。

## 核心内容

### 问题背景

语言条件下的人形运动生成让用户可以用自然语言创建并逐步修改机器人动作。核心难点在于：欠指定的请求需要被连接到具体的运动结构，且该结构要能相对于一个已被接受的参考运动继续修改。作者以 Unitree G1 人形机器人为目标平台，提出生成与编辑框架 TRACE，围绕类型化、可度量的运动学量构建。

### 方法

- **生成条件的锚定**：将生成条件建立在成对的训练运动之上，而非仅依赖文本。
- **事件预测**：一个语言模型从运动衍生的监督中学习预测支撑（support）、根节点（root）与手部（hand）事件；这些事件的时间对齐编码在扩散生成器中与原始文本互补。
- **运动学一致性**：引入重力参考状态与轨迹—接触目标，改善运动学一致性。
- **编辑机制**：类型化请求定义身体—时间范围（body–time scopes）与相对参考的目标（source-relative goals）。一个独立的参考条件扩散编辑器利用这些目标与修订后的事件实现修改；采样时投影（sampling-time projection）用于保护受保护的状态坐标。

### 实验设置与评估

评估包括定量评价与人工评估，并与对比方法进行比较；另设受控消融实验与多轮编辑评测。摘要未披露具体数据集规模、基线名称或数值指标。

### 关键结果

- 定量评估与人工评估显示，相比对比方法，语义对齐与运动质量均有提升。
- 受控消融支持运动锚定条件与运动学一致性的价值。
- 多轮编辑评测表明，在共享保持约束下，连续的相对请求能够得到更可靠的执行。

### 结论

结果支持将类型化运动学结构作为运动生成与参考感知修订的共同基础。

## Overview

Language-conditioned humanoid motion generation enables users to create and refine robot movements through natural language. The central challenge is to connect an underspecified request to concrete motion structure that can subsequently be revised relative to an accepted reference. We present TRACE, a generation and editing framework for the Unitree G1 humanoid robot built around typed, measurable kinematic quantities. Our insight is to ground generation conditions in paired training motions and editing goals in the current motion. A language model learns to predict support, root, and hand events from motion-derived supervision; their time-aligned encodings complement the original text in a diffusion generator. Gravity-referenced states and trajectory--contact objectives improve kinematic consistency. For editing, typed requests define body--time scopes and source-relative goals. A separate reference-conditioned diffusion editor uses these goals and revised events to realize changes, while sampling-time projection preserves protected state coordinates. Quantitative evaluation and human assessment show improved semantic alignment and motion quality over the compared methods. Controlled ablations support the value of motion-grounded conditioning and kinematic consistency, while multi-turn editing evaluations demonstrate more reliable execution of successive relative requests under shared preservation constraints. Together, these results support typed kinematic structure as a common basis for motion generation and reference-aware revision.

## 参考
- https://arxiv.org/abs/2610.21515
