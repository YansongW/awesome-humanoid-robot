---
$id: ent_paper_hwang_learning_distance_conditioned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion Clip
  zh: Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion Clip
  ko: Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion Clip
summary:
  en: 'Motion tracking can reproduce humanoid loco-manipulation from a single retargeted motion clip, but a policy trained
    on a fixed reference primarily reproduces its demonstrated transport outcome. Although the source trajectory visits intermediate
    object displacements, transport termination is demonstrated only at its endpoint. We identify this mismatch as the termination-versus-passage
    gap: ...'
  zh: 该论文研究人形机器人 loco-manipulation 中的物体搬运问题，作者来自韩国研究团队（Yuhyeon Hwang 等）。作者指出单一动作片段训练的策略只能复现演示终点的搬运结果，并提出 Distance-Conditioned
    Reference Recomposition (DCRR)，将演示的终止片段重定位到中间搬运状态，从而构建距离条件监督。DCRR-BC 在 Carry、Kick-Push、Crouch-Push、Drag 四种交互模式下实现命令相关的搬运，整体归一化距离
    MAE 为 0.15，优于仅用源动作行为克隆的 0.28。
  ko: 'Motion tracking can reproduce humanoid loco-manipulation from a single retargeted motion clip, but a policy trained
    on a fixed reference primarily reproduces its demonstrated transport outcome. Although the source trajectory visits intermediate
    object displacements, transport termination is demonstrated only at its endpoint. We identify this mismatch as the termination-versus-passage
    gap: ...'
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
- motion_tracking
- distance_conditioned_policy
- behavior_cloning
- sim_to_sim_transfer
- reference_recomposition
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.21467);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.21467 Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion
    Clip
  url: https://arxiv.org/abs/2609.21467
  date: '2026-09-18'
  accessed_at: '2026-09-21'
---

## 概述

人形机器人可通过单个重定向动作片段进行运动跟踪来复现 loco-manipulation，但基于固定参考训练的策略主要只能复现演示中的搬运结果。作者将这一问题归因于“终止与经过之间的差距”：源轨迹虽然经过中间物体位移，但只在终点演示了搬运终止。为此提出 Distance-Conditioned Reference Recomposition (DCRR)，把演示的终止片段重新放置到中间搬运状态上。冻结的跟踪教师模型在闭环动力学下重放重组后的参考，保留的轨迹按实际达成的物体放置位置重新标注，并蒸馏为无参考策略。该方法从源动作所编码的交互行为中构建出距离条件监督。在 Carry、Kick-Push、Crouch-Push、Drag 上，DCRR-BC 产生依赖命令的搬运，整体归一化距离 MAE 为 0.15，而仅用源动作的行为克隆为 0.28；RL 微调进一步提升了训练仿真器中的命令响应与执行鲁棒性，并在 sim-to-sim 迁移下保持有效，硬件实验也展示了四种交互模式下的搬运距离调制。

## 核心内容

### 问题背景
- 通过单个重定向动作片段进行运动跟踪，可以让人形机器人复现 loco-manipulation 行为。
- 但基于固定参考训练的策略主要只能复现其演示的搬运结果，无法按命令调节搬运距离。
- 作者将这一不匹配称为 termination-versus-passage gap：源轨迹会经过中间物体位移，但这些中间位移只是“经过状态”，只有终点才被演示为“终止完成”的结果。

### 方法：Distance-Conditioned Reference Recomposition (DCRR)
- DCRR 将演示中的终止片段重新定位到中间搬运状态，从而把终点演示转化为中间状态下的终止监督。
- 一个冻结的跟踪教师模型在闭环动力学下重放这些重组后的参考。
- 保留下来的轨迹按其实际达成的物体放置位置重新标注。
- 这些标注数据被蒸馏为一个无参考策略。
- 该流程从源动作所编码的交互行为中构造出距离条件监督。

### 实验设置与关键结果
- 评估覆盖四种交互模式：Carry、Kick-Push、Crouch-Push、Drag。
- DCRR-BC 产生依赖命令的搬运行为，整体归一化距离 MAE 为 0.15。
- 仅用源动作的行为克隆（source-only behavior cloning）整体归一化距离 MAE 为 0.28。
- RL 微调进一步改善了命令响应与执行鲁棒性，在训练仿真器中有效，并在 sim-to-sim 迁移下同样有效。
- 硬件实验展示了全部四种交互模式下的搬运距离调制。

### 结论
- 通过将演示终止片段重定位到中间状态并重新标注、蒸馏，可以从单个动作片段中构建距离条件监督，使无参考策略具备按命令调节搬运距离的能力。

## Overview

Motion tracking can reproduce humanoid loco-manipulation from a single retargeted motion clip, but a policy trained on a fixed reference primarily reproduces its demonstrated transport outcome. Although the source trajectory visits intermediate object displacements, transport termination is demonstrated only at its endpoint. We identify this mismatch as the termination-versus-passage gap: intermediate displacements are observed as passage states rather than termination-complete outcomes. We introduce Distance-Conditioned Reference Recomposition (DCRR), which relocates the demonstrated termination segment to intermediate transport states. A frozen tracking teacher replays the recomposed references under closed-loop dynamics, and the retained trajectories are relabeled by their achieved object placements and distilled into a reference-free policy. This procedure constructs distance-conditioned supervision from the interaction behavior encoded in the source motion. Across Carry, Kick-Push, Crouch-Push, and Drag, DCRR-BC produces command-dependent transport with an overall normalized distance mean absolute error (MAE) of 0.15, compared with 0.28 for source-only behavior cloning. RL fine-tuning further improves the command response and execution robustness in the training simulator and under sim-to-sim transfer. Finally, hardware experiments demonstrate transport-distance modulation across all four interaction modes.

## 参考
- https://arxiv.org/abs/2609.21467
