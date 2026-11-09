---
$id: ent_paper_gu_recontact_reconstruct_and_reta_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation'
  zh: 'ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation'
  ko: 'ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation'
summary:
  en: Contact transitions allow humanoid robots to redistribute object support across the whole body, enabling manipulation
    beyond hand-only grasps. Human videos provide a scalable source of such transitions for robots to learn from. However,
    body occlusion disrupts object pose tracking and corrupts retargeted motion. Moreover, accurately reproducing the object
    trajectory does not ensure that the robot ...
  zh: ReContact 是一种从人类视频中重建并重定向人-物接触的方法，由 Zhongkai Gu、Yang Liu、Wei Zhu 与 Mitsuhiro Hayashibe 提出，用于实现接触丰富的人形机器人操作。该方法以物体为中心的接触计划（包含接触阶段、接触对、锚点、按压方向与粘附/滑动模式）来稳定遮挡下的物体位姿重建，并在冻结的全身跟踪器之上训练残差策略，使机器人在计划锚点处以指定方向施力。仿真中大腿支撑重抓取任务的双掌底部托持成功率达
    83.5，远超最佳基线；单一策略在 247 条参考上训练后，新放置的管内传递成功率由 20.4% 提升至 97.8%，并在真实 Unitree G1 上执行了七项接触丰富操作与两项移动操作任务。
  ko: Contact transitions allow humanoid robots to redistribute object support across the whole body, enabling manipulation
    beyond hand-only grasps. Human videos provide a scalable source of such transitions for robots to learn from. However,
    body occlusion disrupts object pose tracking and corrupts retargeted motion. Moreover, accurately reproducing the object
    trajectory does not ensure that the robot ...
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
- humanoid_manipulation
- contact_retargeting
- learning_from_video
- residual_policy
- whole_body_control
- contact_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.02968);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.02968 ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation'
  url: https://arxiv.org/abs/2611.02968
  date: '2026-11-02'
  accessed_at: '2026-11-09'
---

## 概述

ReContact 关注的是如何让人形机器人从人类视频中学习全身参与的多接触操作，而非仅靠手部抓取。人类视频虽可提供大量接触转换样本，但身体遮挡会破坏物体位姿跟踪并污染重定向后的动作，而且仅复现物体轨迹并不能保证机器人在预期接触点施加稳定力，容易在后续阶段发生滑移或掉落。为此，作者提出以物体为中心的接触计划，显式规定接触阶段、接触对、锚点、按压方向以及粘附或滑动模式，并利用接触先验在遮挡条件下稳定物体位姿重建。在方法上，一个残差策略叠加在冻结的全身跟踪器之上，并以“在计划锚点处按指定方向完成接触”为奖励进行训练。仿真与真机实验表明该方法在接触精度与任务成功率上均显著优于基线，并已在 Unitree G1 上部署验证。

## 核心内容

### 问题背景
人形机器人可通过接触转换在全身范围内重新分配对物体的支撑，从而完成超越单手抓取的操作。人类视频是这类接触转换的可扩展数据来源，但存在两个关键障碍：一是身体遮挡会中断物体位姿跟踪，使重定向后的运动被污染；二是即使精确复现物体轨迹，也不能保证机器人在预期接触点施加稳定力，后续阶段仍可能出现滑移或掉落。

### 方法
ReContact 通过以物体为中心的接触计划来重建并重定向人-物交互。该计划规定：
- 接触阶段
- 接触对
- 锚点
- 按压方向
- 粘附或滑动模式

接触先验被用于在遮挡情况下稳定物体位姿重建。在控制层面，方法在一个冻结的全身跟踪器之上训练残差策略，奖励信号鼓励机器人在计划锚点处完成接触，并使施力方向与规定方向对齐。

### 实验设置与关键结果
- 仿真中的大腿支撑重抓取任务：ReContact 在三个训练种子下平均有 83.5 的回合实现计划的双掌底部托持，最佳适配基线仅为 0.16%。
- 单一策略在 247 条参考上训练，并针对新放置重新求解：工作空间内管内传递成功率从仅用源参考的 20.4% 提升至 97.8%。
- 真机部署于 Unitree G1：策略执行了七项接触丰富操作任务与两项移动操作任务。

### 结论
以物体为中心的接触计划结合接触先验与残差策略，可有效缓解遮挡导致的位姿重建退化，并保证机器人在计划接触点施加方向一致的稳定力，从而在仿真与真实人形平台上实现接触丰富的操作。

## Overview

Contact transitions allow humanoid robots to redistribute object support across the whole body, enabling manipulation beyond hand-only grasps. Human videos provide a scalable source of such transitions for robots to learn from. However, body occlusion disrupts object pose tracking and corrupts retargeted motion. Moreover, accurately reproducing the object trajectory does not ensure that the robot applies stabilizing forces at the intended contacts, risking slips or drops in later phases. To address these challenges, we propose ReContact, which reconstructs and retargets human-object interactions through an object-centric contact plan. The plan specifies contact phases, contact pairs, anchors, pressing directions, and sticking or sliding modes. Contact priors stabilize object pose reconstruction through occlusion. A residual policy over a frozen whole-body tracker is rewarded for making contact at planned anchors with forces aligned to the specified directions. In simulation, on a thigh-supported regrasp task, ReContact achieves the planned two-palm bottom hold in 83.5 of episodes over three training seeds, versus 0.16% for the best adapted baseline. One policy trained on 247 references re-solved for new placements raises in-workspace tube-transfer success from 20.4% (source reference only) to 97.8%. On a real Unitree G1, policies execute seven contact-rich manipulation and two loco-manipulation tasks.

## 参考
- https://arxiv.org/abs/2611.02968
