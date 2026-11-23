---
$id: ent_paper_liu_humanoid_robots_for_safety_cri_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter'
  zh: 'Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter'
  ko: 'Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter'
summary:
  en: Humanoid robots can reduce personnel exposure in electrical switching, but safe control is challenging because the tool
    must reach a target switch next to similar devices, where an imprecise operator command can contact a non-target switch.
    This study proposes a runtime safety filter that checks each operator command during virtual-reality teleoperation of
    a humanoid robot. The filter integrates ...
  zh: 本文提出一种运行时安全过滤器，用于人形机器人在安全关键的电气开关操作中进行虚拟现实遥操作时的指令校验。该过滤器结合由机器人头部相机估计的场景模型与以目标为条件的控制屏障函数二次规划（CBF-QP），在放行安全指令的同时使工具远离非目标开关。在
    Unitree G1 人形机器人上的真实实验中，两个站立位置各进行六轮，共十轮目标操作全部成功，且未发生非目标开关被触发；仿真研究中该方法实现 9/9 安全完成，而原始遥操作为 5/9。
  ko: Humanoid robots can reduce personnel exposure in electrical switching, but safe control is challenging because the tool
    must reach a target switch next to similar devices, where an imprecise operator command can contact a non-target switch.
    This study proposes a runtime safety filter that checks each operator command during virtual-reality teleoperation of
    a humanoid robot. The filter integrates ...
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
- safety_filter
- control_barrier_function
- teleoperation
- electrical_switching
- runtime_assurance
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.27845);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.27845 Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint
    filter'
  url: https://arxiv.org/abs/2611.27845
  date: '2026-11-20'
  accessed_at: '2026-11-23'
---

## 概述

人形机器人可降低电气开关操作中的人员暴露风险，但由于目标开关紧邻相似设备，操作者指令不精确时工具可能误触非目标开关，因此安全控制颇具挑战。为此，作者提出一种运行时安全过滤器，在人形机器人虚拟现实遥操作过程中逐条检查操作者指令。该过滤器融合从机器人头部相机估计的场景模型，并采用以目标为条件的控制屏障函数二次规划，在保持工具远离非目标开关的同时，将安全指令原样放行。研究在 Unitree G1 人形机器人上开展真实世界实验，两个站立位置各进行六轮，十轮目标操作全部成功，目标开关保持不变且未触发任何非目标开关。仿真研究进一步显示该方法实现 9/9 的安全完成，而原始遥操作仅为 5/9，表明该方法用于人形机器人开关操作具有可行性。

## 核心内容

### 问题背景

人形机器人能够减少人员在电气开关操作中的暴露，但安全控制存在难点：工具需要抵达目标开关，而目标开关紧邻相似设备，操作者指令不够精确时可能接触到非目标开关，造成误操作风险。

### 方法

- 提出一种运行时安全过滤器，在人形机器人虚拟现实遥操作过程中对每一条操作者指令进行检查。
- 过滤器融合两部分：一是由机器人头部相机估计得到的场景模型；二是以目标为条件的控制屏障函数二次规划（CBF-QP）。
- 该二次规划的作用是使工具与目标开关保持距离约束、远离非目标开关，同时对安全的操作指令不作修改、原样放行。

### 实验设置

- 真实世界实验：在 Unitree G1 人形机器人上进行，设置两个站立位置，每个位置进行六轮。
- 仿真研究：与原始遥操作进行对比。

### 关键结果

- 真实世界实验中，十轮目标操作全部成功，目标开关保持不变，且未发生任何非目标开关被触发。
- 仿真研究中，该方法实现 9/9 的安全完成，而原始遥操作仅为 5/9。

### 结论

实验结果证明了该方法用于人形机器人电气开关操作的可行性，能够在放行安全指令的同时有效避免对非目标开关的误触。

## Overview

Humanoid robots can reduce personnel exposure in electrical switching, but safe control is challenging because the tool must reach a target switch next to similar devices, where an imprecise operator command can contact a non-target switch. This study proposes a runtime safety filter that checks each operator command during virtual-reality teleoperation of a humanoid robot. The filter integrates a scene model estimated from the robot head camera and a target-conditioned control barrier function quadratic program that keeps the tool away from the non-target switch while passing safe commands unchanged. In real-world experiments on a Unitree G1 humanoid robot, with six rounds at each of two standing positions, target operations succeed in all ten rounds with an unchanged target and no non-target actuation. A simulation study achieves 9/9 safe completions, compared with 5/9 for raw teleoperation, demonstrating the feasibility of the method for humanoid switching operations.

## 参考
- https://arxiv.org/abs/2611.27845
