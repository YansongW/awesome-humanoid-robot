---
$id: ent_paper_team_systematically_exploring_the_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies
  zh: Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies
  ko: Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies
summary:
  en: GPT-6 Astra exhibits a remarkable ability to generate numerical robot actions, extending its role beyond high-level
    planning. To assess Astra's capabilities as general-purpose embodied policies, we conduct comprehensive evaluations across
    six domains, examining direct control, cooperation with learned policies, and feedback-driven adaptation. In gripper manipulation,
    Astra can correct task ...
  zh: Galbot Team 等对 GPT-6 Astra 作为通用具身策略的能力进行了系统评测，覆盖夹爪操作、灵巧操作、移动操作、导航、运动控制与人形全身操作六大领域，考察直接控制、与学习型策略协作以及反馈驱动适应三种模式。结果显示 Astra
    在任务决策层面表现突出，例如导航任务中 RxR 指令跟随成功率达 92%，但与 π0.5 等策略混合控制时成功率多在 38.7%–50% 之间，运动控制中五次尝试均未到达目标。研究揭示出有用任务决策与可靠物理控制之间的差距，并指出推理延迟与
    token 消耗对实际控制的制约。
  ko: GPT-6 Astra exhibits a remarkable ability to generate numerical robot actions, extending its role beyond high-level
    planning. To assess Astra's capabilities as general-purpose embodied policies, we conduct comprehensive evaluations across
    six domains, examining direct control, cooperation with learned policies, and feedback-driven adaptation. In gripper manipulation,
    Astra can correct task ...
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
- embodied_policy
- gpt_6_astra
- hybrid_control
- humanoid_loco_manipulation
- navigation
- inference_latency
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.38537);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.38537 Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies
  url: https://arxiv.org/abs/2609.38537
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

该工作由 Galbot Team 联合多位作者完成，旨在评估 GPT-6 Astra 能否从高层规划扩展到直接生成数值机器人动作，从而充当通用具身策略。评测横跨六个领域，并区分直接控制、与已学习策略协作以及基于反馈的适应三种使用方式。在夹爪与灵巧操作中，Astra 可修正任务目标并为后续策略执行准备接触条件，混合控制分别取得 48% 与 50% 的成功率；移动操作混合控制成功率为 38.7%。导航是 Astra 表现最好的方向，RxR 指令跟随达 92%、HM3D 物体搜索达 82%，但搜索过程绕行明显。运动控制仍是短板，单条障碍赛道五次连续尝试均未到达目标；人形 loco-manipulation 则在 30 项 HumanoidBench 任务中的 13 项超过基线。作者据此指出任务决策与物理控制之间存在落差，并强调推理延迟与 token 开销对实际部署的限制。

## 核心内容

### 问题背景
GPT-6 Astra 展现出生成数值机器人动作的能力，其角色已不限于高层规划。为判断它能否作为通用具身策略使用，作者在六个领域展开系统评测，并区分三种使用范式：直接控制、与学习型策略协作、以及反馈驱动的适应。

### 方法
评测覆盖夹爪操作、灵巧操作、移动操作、导航、运动控制与人形 loco-manipulation 六个领域。在协作范式中，Astra 与已学习策略（如 π0.5）组合形成混合控制；在直接控制范式中由 Astra 直接输出动作；同时考察基于反馈的适应能力。

### 关键结果
- **夹爪操作**：Astra 能够修正任务目标并为后续策略执行准备接触条件；与 π0.5 的混合控制在所评测的 RoboDojo 子集上达到 48% 成功率。
- **灵巧操作**：在十次经验引导的 DexJoCo 试验中，混合控制达到 50% 成功率；而直接的手内控制难以协调手指接触。
- **移动操作**：混合控制在所评测的 RoboCasa365 上达到 38.7% 成功率。
- **导航**：Astra 在本地对比中领先，RxR 指令跟随成功率为 92%，HM3D 物体搜索为 82%，但搜索过程产生大量绕行。
- **运动控制**：密集运动参考生成仍不可靠，在单条障碍赛道上的五次连续尝试均未到达目标，尽管稳定性与前进进度有所改善。
- **人形 loco-manipulation**：配合预训练全身控制器，Astra 在 30 项 HumanoidBench 任务中的 13 项上超过基线方法。

### 推理开销
推理延迟进一步制约实际控制。在每种条件下各 50 个 RoboDojo 实例中，策略辅助控制与直接控制分别消耗 6.248 亿与 11.32 亿 token。一次 30 秒的运动控制运行需要 250 次模型调用，平均每次耗时 39.86 秒，且推理期间物理仿真处于暂停状态。

### 结论
评测结果揭示出有用的任务决策与可靠的物理控制之间存在明显差距：Astra 在导航与部分操作任务中能提供有效的任务级判断，但在需要精细接触协调或密集运动参考的场景中仍不可靠，同时推理延迟与 token 消耗构成实际部署的重要约束。

## Overview

GPT-6 Astra exhibits a remarkable ability to generate numerical robot actions, extending its role beyond high-level planning. To assess Astra's capabilities as general-purpose embodied policies, we conduct comprehensive evaluations across six domains, examining direct control, cooperation with learned policies, and feedback-driven adaptation. In gripper manipulation, Astra can correct task targets and prepare contact conditions for subsequent policy execution; hybrid control with π0.5 achieves 48% success on the evaluated RoboDojo subset. In dexterous manipulation, hybrid control achieves 50% success in ten experience-guided DexJoCo trials, while direct in-hand control struggles to coordinate finger contacts. In mobile manipulation, hybrid control reaches 38.7% success on the evaluated RoboCasa365. In navigation, Astra leads our local comparisons, reaching 92% success on RxR instruction following and 82% on HM3D object search, although search incurs substantial detours. In locomotion, dense motion-reference generation remains unreliable: none of five sequential attempts on a single obstacle course reaches the goal, despite improvements in stability and forward progress. In humanoid loco-manipulation, Astra exceeds baseline methods on 13 of 30 HumanoidBench tasks with pretrained whole-body controllers. These findings reveal a gap between useful task decisions and reliable physical control. Inference latency further constrains practical control: across 50 RoboDojo instances per condition, policy-assisted and direct control consume 624.8 million and 1.132 billion tokens. A 30-second locomotion run requires 250 model calls averaging 39.86 seconds each, with physics paused during inference.

## 参考
- https://arxiv.org/abs/2609.38537
