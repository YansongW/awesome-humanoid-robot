---
$id: ent_paper_hu_workhorse_learning_robust_whol_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data'
  zh: 'Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data'
  ko: 'Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data'
summary:
  en: 'Humanoid robots still struggle to plan contact-rich whole-body manipulation from egocentric RGB and proprioception.
    Workhorse learns such manipulation from robot-free human demonstrations. A visual planner predicts five-link targets:
    the poses of the torso, both wrists, and both feet. A reinforcement-learning whole-body tracker follows them on the robot.
    Both policies train separately on the same ...'
  zh: Workhorse 是一种从无机器人参与的人类演示中学习人形机器人全身 loco-manipulation 的方法，由 Songbo Hu、Qiayuan Liao、Yufeng Chi、Kevin Zakka、Yakun Sophia
    Shao、Pieter Abbeel、Koushil Sreenath 提出。它由一个视觉规划器预测躯干、双腕和双脚这五个连杆的目标位姿，再由一个强化学习全身跟踪器在机器人上执行，两个策略分别在同一批录制的人类姿态上训练且无需 retargeting。在真实
    Unitree G1 上，系统完成了搬箱、踢箱、接住抛来的箱子以及推倒并攀爬行李箱等任务。
  ko: 'Humanoid robots still struggle to plan contact-rich whole-body manipulation from egocentric RGB and proprioception.
    Workhorse learns such manipulation from robot-free human demonstrations. A visual planner predicts five-link targets:
    the poses of the torso, both wrists, and both feet. A reinforcement-learning whole-body tracker follows them on the robot.
    Both policies train separately on the same ...'
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
- humanoid_loco_manipulation
- whole_body_control
- learning_from_human_demonstration
- reinforcement_learning
- visual_planner
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.09117);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.09117 Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data'
  url: https://arxiv.org/abs/2610.09117
  date: '2026-10-06'
  accessed_at: '2026-10-12'
- id: src_002
  type: website
  title: Project page
  url: https://hybridrobotics.github.io/workhorse/
  accessed_at: '2026-10-12'
---

## 概述

Workhorse 针对的是人形机器人难以从第一视角 RGB 与本体感知中规划富含接触的全身操作这一问题，其核心思路是直接从无机器人的人类演示中学习。系统由两部分组成：视觉规划器负责预测躯干、双腕与双脚五个连杆的目标位姿，强化学习全身跟踪器则让机器人在真实本体上跟随这些目标。两个策略在同一批录制的人类姿态上分别训练，过程中不需要 retargeting。为提升部署鲁棒性，作者对每个策略的训练数据做了增强，使其模仿另一个策略在部署时会犯的错误。在真实 Unitree G1 上，Workhorse 能用双手和踢击搬运箱子、接住抛来的箱子，并推倒和攀爬行李箱；搬箱过程中还展示了被人推搡或把箱子拿走后的恢复能力。

## 核心内容

### 问题背景
人形机器人从第一视角 RGB 与本体感知出发，规划富含接触的全身操作仍然困难。Workhorse 的目标是绕开这一难点，直接从无机器人参与的人类演示中学习此类操作。

### 方法
- 系统由两个策略组成：一个视觉规划器预测五个连杆的目标位姿，即躯干、双腕与双脚的位姿；一个强化学习全身跟踪器在机器人上跟随这些目标。
- 两个策略在同一批录制的人类姿态上分别训练，不需要 retargeting。
- 作者对每个策略的训练数据做增强，使其模仿另一个策略在部署时产生的错误。

### 实验设置与关键结果
- 在真实 Unitree G1 上，Workhorse 用双手和一次踢击搬运箱子、接住抛来的箱子，并推倒和攀爬行李箱。
- 在搬箱过程中，展示了被人推搡或把箱子拿走后的恢复能力。
- 在演示房间的仿真副本中，系统在 77% 的回合中完成搬箱；在 40 N.s 推力下完成率为 64%。
- 当两个策略都用同一批演示重新训练时，仿真中的第二台人形机器人在无推力条件下完成搬箱的回合比例为 83%。

### 结论
Workhorse 表明，无需机器人数据与 retargeting，仅凭人类演示即可训练出具备全身 loco-manipulation 能力的人形机器人系统，并在真实硬件与仿真中展现出对扰动的恢复能力。

## Overview

Humanoid robots still struggle to plan contact-rich whole-body manipulation from egocentric RGB and proprioception. Workhorse learns such manipulation from robot-free human demonstrations. A visual planner predicts five-link targets: the poses of the torso, both wrists, and both feet. A reinforcement-learning whole-body tracker follows them on the robot. Both policies train separately on the same recorded human poses, without retargeting. We augment the training data of each policy to imitate the errors that the other makes at deployment. On a real Unitree G1, Workhorse transport boxes with its hands and a kick, catches a thrown box, and topples and climbs a suitcase. During box transport, we show recoveries after a person pushes the robot or takes the box away. In a simulated copy of the demonstration room, the system completes box transport in 77% of episodes, and in 64% under 40 N.s pushes. With both policies retrained from the same demonstrations, a simulated second humanoid completes box transport in 83% of episodes without pushes.

## 参考
- https://arxiv.org/abs/2610.09117
- https://hybridrobotics.github.io/workhorse/
