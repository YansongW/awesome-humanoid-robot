---
$id: ent_paper_wu_kinogen_customizable_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation'
  zh: 'KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation'
  ko: 'KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation'
summary:
  en: We present KinoGen, a framework that synthesizes customizable humanoid loco-manipulation references through kinematically
    grounded video generation. KinoGen conditions a pretrained video generator on calibrated renders of the target robot and
    object in a simulated task instance and recovers the reference by fitting the same models to the generated two-view video,
    so that the reference lies in the ...
  zh: KinoGen 是一个通过运动学约束的视频生成来合成可定制人形机器人移动操作参考轨迹的框架。该方法以目标机器人与物体在仿真任务实例中的标定渲染图为条件驱动预训练视频生成器，再通过对生成的双视角视频拟合相同模型来恢复参考轨迹，使参考轨迹天然位于机器人构型空间中，无需人体代理或重定向。在八项移动操作任务上，KinoGen
    相比基于视频的基线方法具有更低的穿透与脚部滑移，并保留超过 90% 的标注接触；其定制参考轨迹能满足全部指定目标且穿透显著低于直接插值，所训练的策略已部署在配备灵巧手的 Unitree G1 人形机器人上。
  ko: We present KinoGen, a framework that synthesizes customizable humanoid loco-manipulation references through kinematically
    grounded video generation. KinoGen conditions a pretrained video generator on calibrated renders of the target robot and
    object in a simulated task instance and recovers the reference by fitting the same models to the generated two-view video,
    so that the reference lies in the ...
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
- video_generation
- motion_retargeting_free
- contact_preservation
- unitree_g1
- reference_trajectory_synthesis
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.20552);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.20552 KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation'
  url: https://arxiv.org/abs/2610.20552
  date: '2026-10-14'
  accessed_at: '2026-10-19'
---

## 概述

KinoGen 面向人形机器人移动操作参考轨迹的生成问题，提出以运动学约束为核心的视频生成框架。它并不依赖人体动作数据或重定向流程，而是将预训练视频生成器以目标机器人和物体在仿真任务实例中的标定渲染图为条件，再通过对生成的双视角视频拟合同一套模型来反解参考轨迹，因此所得轨迹在构造上即处于机器人构型空间内。重建过程由身体、手部与物体先验初始化，并通过对跨视角证据的直接优化进行精修。由于编辑后的关键帧本身只是另一种渲染状态，用户可以指定目标物体位姿、围绕该关键帧重新生成视频，从而获得精确满足该位姿的参考轨迹。在八项移动操作任务上的实验显示，该方法在穿透与脚部滑移指标上优于基于视频的基线，并保留超过 90% 的标注接触；定制参考轨迹满足所有预设目标，且穿透明显低于直接插值。基于合成参考轨迹训练的策略已部署于配备灵巧手的 Unitree G1 人形机器人。

## 核心内容

### 问题背景

人形机器人移动操作（loco-manipulation）需要高质量的参考轨迹用于策略学习，但获取此类参考通常依赖人体动作捕捉与重定向，流程复杂且难以精确控制目标物体位姿。KinoGen 旨在绕开人体代理与重定向环节，直接生成位于机器人构型空间内的可定制参考轨迹。

### 方法

- **条件化视频生成**：以目标机器人与物体在仿真任务实例中的标定渲染图为条件，驱动预训练视频生成器生成双视角视频。
- **运动学约束恢复**：对生成的双视角视频拟合与条件化阶段相同的模型，从而反解出参考轨迹；由于轨迹由该拟合过程产生，其天然处于机器人构型空间中。
- **先验初始化与优化精修**：利用身体、手部与物体先验初始化重建，并针对跨视角证据进行直接优化以精修结果。
- **关键帧编辑实现定制**：编辑后的关键帧被视为另一种渲染状态，用户可指定目标物体位姿，围绕该关键帧重新生成视频，进而获得精确满足该位姿的参考轨迹。

### 实验设置

在八项移动操作任务上评估，与基于视频的基线方法进行比较，考察穿透、脚部滑移与标注接触保留情况；并评估定制参考轨迹对预设目标的满足程度及穿透水平（与直接插值对比）。所合成的参考轨迹用于训练跟踪策略，并部署在配备灵巧手的 Unitree G1 人形机器人上。

### 关键结果

- 在八项移动操作任务中，KinoGen 的穿透与脚部滑移均低于基于视频的基线方法。
- 保留超过 90% 的标注接触。
- 定制参考轨迹满足全部预设目标，且穿透显著低于直接插值。
- 基于合成参考轨迹训练的跟踪策略已在 Unitree G1 人形机器人上部署。

### 结论

KinoGen 通过运动学约束的视频生成，实现了无需人体代理与重定向的可定制人形机器人移动操作参考轨迹合成，并在接触保留、穿透与脚部滑移等指标上优于视频基线，同时支持精确的目标物体位姿定制。

## Overview

We present KinoGen, a framework that synthesizes customizable humanoid loco-manipulation references through kinematically grounded video generation. KinoGen conditions a pretrained video generator on calibrated renders of the target robot and object in a simulated task instance and recovers the reference by fitting the same models to the generated two-view video, so that the reference lies in the robot configuration space by construction without a human body proxy or retargeting. Body, hand, and object priors initialize the reconstruction, and direct optimization against cross-view evidence refines it. Since an edited keyframe is simply another rendered state, a user can prescribe a goal object pose, regenerate the video around the edited keyframe, and obtain a reference that satisfies the pose exactly. Across eight loco-manipulation tasks, KinoGen yields lower penetration and foot skating than video-based baselines and preserves over 90% of annotated contacts, and its customized references satisfy every prescribed target with substantially less penetration than direct interpolation. Tracking policies trained on the synthesized references are deployed on a Unitree G1 humanoid with dexterous hands. Project webpage: https://kinogen-humanoid.github.io/.

## 参考
- https://arxiv.org/abs/2610.20552
