---
$id: ent_paper_wang_reflexarc_bottom_up_integratio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control'
  zh: 'ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control'
  ko: 'ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control'
summary:
  en: Humanoid robots operating in cluttered environments must react to unexpected contacts before the first impact peak,
    which arrives within tens of milliseconds. Learned whole-body policies running at 50 Hz introduce a policy-cycle delay
    and may suppress a protective withdrawal as a tracking error. To address these challenges, we propose ARC (Ascending Reflex
    Control), a bottom-up framework that ...
  zh: ARC（Ascending Reflex Control）是一个自下而上的框架，将瞬时触觉反射与学习式全身控制相结合，用于人形机器人在杂乱环境中的快速接触响应。该工作由 Mingyu Wang、Si Li、Ziqing Chen、He
    Wang、Li Yi 完成。其反射通路可在 10 ms 内将全身退缩姿态直接送达电机，并在 Unitree G1 上验证：相比延迟 20 ms 的同等反射，首次力峰值降低 34.1%，接触冲量从 0.2632 N s 降至 0.1225
    N s（2.15 倍比值）。
  ko: Humanoid robots operating in cluttered environments must react to unexpected contacts before the first impact peak,
    which arrives within tens of milliseconds. Learned whole-body policies running at 50 Hz introduce a policy-cycle delay
    and may suppress a protective withdrawal as a tracking error. To address these challenges, we propose ARC (Ascending Reflex
    Control), a bottom-up framework that ...
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
- tactile_reflex
- whole_body_control
- contact_response
- reflex_integration
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.04424);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.04424 ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control'
  url: https://arxiv.org/abs/2611.04424
  date: '2026-11-03'
  accessed_at: '2026-11-09'
---

## 概述

人形机器人在杂乱环境中需要在首次冲击峰值到来前做出反应，而该峰值往往在数十毫秒内出现；以 50 Hz 运行的学习式全身策略会引入策略周期延迟，并可能把保护性退缩当作跟踪误差而抑制。为此，作者提出 ARC（Ascending Reflex Control），由瞬时反射通路与自下而上反射集成两部分组成：前者从全身触觉感知中检测危险接触、求解全身退缩姿态并在 10 ms 内直接下发至电机；后者通过反射在环策略学习、反射透明策略对齐与反射知情策略适配，维持退缩、保持平衡并完成更长时程的恢复。团队在 Unitree G1 上部署 ARC，并针对三类危险接触进行评估，同时展示了受保护的动捕跟踪、遥操作以及由足部触觉引导的无视觉越障。

## 核心内容

### 问题背景
人形机器人在杂乱环境中运动时，意外接触的首次冲击峰值通常在数十毫秒内到达，机器人必须在峰值前做出反应。以 50 Hz 运行的学习式全身策略存在策略周期延迟，且可能将保护性退缩动作误判为跟踪误差而加以抑制，难以满足这种毫秒级响应需求。

### 方法
作者提出 ARC（Ascending Reflex Control），一个自下而上集成的框架，包含两个组件：

- **瞬时反射通路**：从全身触觉感知中检测危险接触，求解全身退缩姿态，并在 10 ms 内将指令直接送达电机。
- **自下而上反射集成**：由三部分构成——反射在环策略学习（reflex-in-the-loop policy learning）、反射透明策略对齐（reflex-transparent policy alignment）与反射知情策略适配（reflex-informed policy adaptation），用于维持退缩动作、保持平衡并完成更长时程的恢复。

### 实验设置
ARC 部署于 Unitree G1 人形机器人，评估覆盖三类危险接触。对比基线为其他条件相同、但反射延迟 20 ms 的版本。

### 关键结果
- 相比延迟 20 ms 的同等反射，ARC 将首次力峰值降低 34.1%。
- 接触冲量从 0.2632 N s 降至 0.1225 N s，比值为 2.15 倍。
- 进一步展示了受保护的动捕跟踪、遥操作，以及由足部触觉引导的无视觉越障。

### 结论
将瞬时触觉反射以自下而上的方式与学习式全身控制集成，可在策略周期延迟之外提供毫秒级的保护性响应，并在维持平衡与完成长时程恢复的同时显著降低接触冲击。

## Overview

Humanoid robots operating in cluttered environments must react to unexpected contacts before the first impact peak, which arrives within tens of milliseconds. Learned whole-body policies running at 50 Hz introduce a policy-cycle delay and may suppress a protective withdrawal as a tracking error. To address these challenges, we propose ARC (Ascending Reflex Control), a bottom-up framework that integrates instantaneous tactile reflexes with learned whole-body control. ARC consists of two components: an instantaneous reflex pathway and bottom-up reflex integration. The reflex pathway detects hazardous contacts from full-body tactile sensing, solves a whole-body withdrawal pose, and delivers it directly to the motors within 10 ms. Bottom-up reflex integration combines reflex-in-the-loop policy learning, reflex-transparent policy alignment, and reflex-informed policy adaptation to sustain the withdrawal, maintain balance, and complete longer-horizon recovery. We deploy ARC on a Unitree G1 and evaluate three categories of hazardous contact. Compared with an otherwise identical reflex delayed by 20 ms, ARC reduces the first force peak by 34.1% and reduces the contact impulse from 0.2632 N s to 0.1225 N s (a 2.15x ratio). We further demonstrate protected motion tracking, teleoperation, and vision-free obstacle traversal guided by foot tactile sensing. Project page: https://minusmodulo.github.io/reflexarc-website/

## 参考
- https://arxiv.org/abs/2611.04424
