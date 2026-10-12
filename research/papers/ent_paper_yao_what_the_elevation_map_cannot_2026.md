---
$id: ent_paper_yao_what_the_elevation_map_cannot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'What the Elevation Map Cannot See: Semantic-Aware Locomotion and Execution-Aware Navigation for Humanoid Robot'
  zh: 'What the Elevation Map Cannot See: Semantic-Aware Locomotion and Execution-Aware Navigation for Humanoid Robot'
  ko: 'What the Elevation Map Cannot See: Semantic-Aware Locomotion and Execution-Aware Navigation for Humanoid Robot'
summary:
  en: Navigation for humanoid robots is critical, yet large-scale evaluation on physical hardware is often impractical due
    to cost and safety concerns, making simulation benchmarks essential. Existing VLN benchmarks achieve physically executable
    navigation, but still assume (1) all hazards are observable from elevation maps; (2) realized motions closely match desired
    motions. In real environments, ...
  zh: 该工作指出现有 VLN 基准假设所有危险都能从 elevation map 中观测到、且实际运动与期望运动一致，因而无法暴露真实环境中的失败模式。作者提出一个同时建模 elevation-subtle 危险与执行偏差的基准，以及一个闭环
    VLN + locomotion 控制框架，用于持续将高层导航与机器人实际状态对齐。在仿真中评估导航，并在实体 Unitree G1 人形机器人上验证 locomotion 策略，结果显示语义输入可减少与 elevation map 中表征不佳的危险的接触，抗偏差机制可提升导航成功率。
  ko: Navigation for humanoid robots is critical, yet large-scale evaluation on physical hardware is often impractical due
    to cost and safety concerns, making simulation benchmarks essential. Existing VLN benchmarks achieve physically executable
    navigation, but still assume (1) all hazards are observable from elevation maps; (2) realized motions closely match desired
    motions. In real environments, ...
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
- humanoid_navigation
- vision_language_navigation
- locomotion_control
- sim_to_real
- hazard_avoidance
- execution_deviation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.07396);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.07396 What the Elevation Map Cannot See: Semantic-Aware Locomotion and Execution-Aware Navigation for
    Humanoid Robot'
  url: https://arxiv.org/abs/2610.07396
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

人形机器人导航的规模化硬件评测受成本与安全限制，仿真基准因此不可或缺。现有 VLN 基准虽已实现物理可执行的导航，但仍隐含两个假设：所有危险都能从 elevation map 中观测到，以及实际实现的运动与期望运动高度一致。真实环境中，倒地的瓶子在 elevation map 中可能语义模糊，手机与洒出的水也难以区分；而 locomotion 策略为规避危险所做的动作会使机器人实际轨迹偏离 VLN 策略规划的路径，这种指令—执行失配会不断累积，把机器人带向非预期位置。为暴露这些失败模式，作者构建了一个同时建模 elevation-subtle 危险与执行偏差的基准，并提出闭环 VLN + locomotion 控制框架，持续将高层导航与机器人实际状态重新对齐。实验在仿真中评估导航，并在实体 Unitree G1 上验证 locomotion 策略，结果表明语义输入减少了与 elevation map 表征不佳的危险的接触，抗偏差机制提升了导航成功率，说明人形机器人导航需从路径完成与危险规避两方面联合评估。

## 核心内容

### 问题背景

人形机器人导航在物理硬件上进行大规模评测往往不切实际，原因在于成本与安全风险，因此仿真基准成为必要手段。现有 VLN 基准已经能够实现物理可执行的导航，但仍建立在两个假设之上：

- 所有危险都可以从 elevation map 中观测到；
- 实际实现的运动与期望运动高度接近。

在真实环境中这两个假设都会失效。例如，倒地的瓶子在 elevation map 中可能表现为语义模糊的障碍，手机与洒出的水也难以仅凭高程信息区分。同时，locomotion 策略为规避危险而采取的动作，会使机器人实际轨迹偏离 VLN 策略原本规划的路径。这种指令与执行之间的失配会逐步累积，最终把机器人引导至非预期位置。

### 方法

为暴露上述失败模式，作者提出：

- 一个同时建模 elevation-subtle 危险（高程图中难以体现的危险）与执行偏差的基准；
- 一个闭环 VLN + locomotion 控制框架，持续将高层导航指令与机器人的实际状态重新对齐。

### 实验设置

导航部分在仿真中进行评估；locomotion 策略进一步在实体 Unitree G1 人形机器人上验证。

### 关键结果

- 语义输入减少了机器人与 elevation map 中表征不佳的危险之间的接触；
- 抗偏差（anti-deviation）机制提升了导航成功率。

### 结论

这些发现表明，人形机器人导航的评估需要同时考虑路径完成情况与危险规避能力，而不能仅依赖其中单一维度。

## Overview

Navigation for humanoid robots is critical, yet large-scale evaluation on physical hardware is often impractical due to cost and safety concerns, making simulation benchmarks essential. Existing VLN benchmarks achieve physically executable navigation, but still assume (1) all hazards are observable from elevation maps; (2) realized motions closely match desired motions. In real environments, however, fallen bottles may be ambiguous in elevation maps, while phones and water spills may be difficult to differentiate; hazard avoidance by the locomotion policy can cause the robot's actual trajectory to deviate from the path intended by the VLN policy. Such command-execution mismatch can accumulate and lead the robot toward unintended locations. To expose these failure modes, we introduce a benchmark that models both elevation-subtle hazards and execution deviations, together with a closed-loop VLN + locomotion control framework that continuously realigns high-level navigation with the robot's actual state. We evaluate navigation in simulation and further validate the locomotion policy on a physical Unitree G1 humanoid robot. Results show that semantic input reduces contact with hazards poorly represented in elevation maps, while anti-deviation improves navigation success. These findings highlight the need to evaluate humanoid navigation jointly in terms of route completion and hazard avoidance.

## 参考
- https://arxiv.org/abs/2610.07396
