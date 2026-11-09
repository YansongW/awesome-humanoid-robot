---
$id: ent_paper_zhu_regate_recurrent_gated_visual_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReGATE: Recurrent Gated Visual Fusion for Reactive Humanoid-Object Interaction'
  zh: 'ReGATE: Recurrent Gated Visual Fusion for Reactive Humanoid-Object Interaction'
  ko: 'ReGATE: Recurrent Gated Visual Fusion for Reactive Humanoid-Object Interaction'
summary:
  en: Humanoid loco-manipulation requires coordinating object acquisition, transport, and release from onboard sensing while
    responding to user commands and incomplete visual observations. We present ReGATE, a whole-body controller that combines
    egocentric depth, proprioception, and online locomotion and contact commands. Built on a teacher-student framework, ReGATE
    integrates interaction-state ...
  zh: ReGATE 是一种面向人形机器人全身 loco-manipulation 的控制器，由 Hao Zhu 与 Jorge Peña-Queralta 提出，融合第一视角深度、本体感知以及在线运动与接触指令。其核心是在教师-学生框架下引入循环适配器进行交互状态估计，并通过头级与全局门控调节视觉更新，在仿真中静态物体抓取成功率达
    85.2%，并在 Unitree G1 上完成抓取-搬运-释放与视觉遮挡下的物体获取。
  ko: Humanoid loco-manipulation requires coordinating object acquisition, transport, and release from onboard sensing while
    responding to user commands and incomplete visual observations. We present ReGATE, a whole-body controller that combines
    egocentric depth, proprioception, and online locomotion and contact commands. Built on a teacher-student framework, ReGATE
    integrates interaction-state ...
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
- recurrent_gated_fusion
- teacher_student_framework
- visuoproprioceptive_fusion
- unitree_g1
- object_acquisition
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.02871);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.02871 ReGATE: Recurrent Gated Visual Fusion for Reactive Humanoid-Object Interaction'
  url: https://arxiv.org/abs/2611.02871
  date: '2026-11-02'
  accessed_at: '2026-11-09'
---

## 概述

ReGATE 针对人形机器人在机载感知条件下完成物体获取、搬运与释放的任务，需同时应对用户指令响应与视觉观测不完整的问题。方法上以教师-学生框架为基础，通过循环适配器预测物体几何与物理接触，从而无需外部物体位姿估计器即可完成交互状态估计；同时用头级与全局门控控制视觉信息对本体感知通路的更新。训练中采用视觉 grounding 与损坏课程，并配合相位感知初始化以提升对短暂接触过渡的覆盖。仿真中，ReGATE 在 330 次静态物体获取试验中成功率为 85.2%，相同协议下 VisualMimic 为 48.5%；在 440 次移动物体获取试验中成功率为 85.9%。在 Unitree G1 上的部署展示了指令化的抓取-搬运-释放序列以及对侧向偏移箱体的获取，定性硬件实验还展示了在初始观测后、接触指令前相机被遮挡时仍能成功获取箱体。

## 核心内容

### 问题背景
人形机器人的 loco-manipulation 需要从机载传感出发协调物体的获取、运输与释放，同时响应用户指令并处理不完整的视觉观测。这一设定对交互状态估计与视觉-本体感知融合提出了较高要求。

### 方法
- **整体架构**：ReGATE 是一个全身控制器，输入包括第一视角深度、本体感知以及在线运动与接触指令。
- **教师-学生框架**：在此框架下训练控制器，并集成交互状态估计。
- **循环适配器**：通过循环适配器预测物体几何与物理接触，不依赖外部物体位姿估计器。
- **门控机制**：采用头级与全局门控调节视觉更新对本体感知通路的注入。
- **训练课程**：使用视觉 grounding 与损坏课程训练适配器，并采用相位感知初始化以增加对短暂接触过渡的覆盖。

### 实验设置与关键结果
- 仿真中，在 330 次静态物体获取试验上达到 85.2% 成功率；相同协议下 VisualMimic 为 48.5%。
- 在 440 次移动物体获取试验上成功率为 85.9%。
- 在 Unitree G1 上部署，展示了指令化的抓取-搬运-释放序列，以及获取侧向偏移箱体的能力。
- 定性硬件实验显示，在初始观测之后、接触指令之前相机被遮挡的情况下，仍能成功获取箱体。

### 结论
作者称，据其所知，这是首个将机载深度与本体感知的循环门控融合从感知式 locomotion 扩展到视觉感知中断条件下人形 loco-manipulation 的工作。

## Overview

Humanoid loco-manipulation requires coordinating object acquisition, transport, and release from onboard sensing while responding to user commands and incomplete visual observations. We present ReGATE, a whole-body controller that combines egocentric depth, proprioception, and online locomotion and contact commands. Built on a teacher-student framework, ReGATE integrates interaction-state estimation through a recurrent adapter that predicts object geometry and physical contact without an external object-pose estimator. Head-wise and global gates regulate visual updates to a proprioceptive pathway. A visual-grounding and corruption curriculum trains the adapter, while phase-aware initialization increases coverage of brief contact transitions. In simulation, ReGATE achieves 85.2% success across 330 static-object acquisition trials, compared with 48.5% for VisualMimic under the same protocol, and 85.9% across 440 moving-object acquisition trials. Deployment on a Unitree G1 demonstrates commanded grasp-transport-release sequences and acquisition of laterally displaced boxes. A qualitative hardware experiment further demonstrates successful box acquisition when the camera is occluded after an initial observation and before the contact command. To the best of our knowledge, this is the first work to extend recurrent gated fusion of onboard depth and proprioception from perceptive locomotion to humanoid loco-manipulation under interrupted visual sensing.

## 参考
- https://arxiv.org/abs/2611.02871
