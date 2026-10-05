---
$id: ent_paper_syarubany_equivdp3_a_sim3_invariant_poin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EquivDP3: A SIM(3)-Invariant Point-Cloud Encoder for Data-Efficient Humanoid Loco-Manipulation'
  zh: 'EquivDP3: A SIM(3)-Invariant Point-Cloud Encoder for Data-Efficient Humanoid Loco-Manipulation'
  ko: 'EquivDP3: A SIM(3)-Invariant Point-Cloud Encoder for Data-Efficient Humanoid Loco-Manipulation'
summary:
  en: Visuomotor policies for humanoid loco-manipulation must generalize across object poses and lighting from only a handful
    of demonstrations. 3D Diffusion Policy (DP3) conditions a diffusion-based action generator on point-cloud features, but
    its PointNet-style encoder has no built-in equivariance to the rotations, translations, and scalings (SIM(3)) that manipulation
    tasks respect. EquiBot closed ...
  zh: EquivDP3 是一种面向人形机器人移动操作（loco-manipulation）的两阶段视觉运动策略，由 Abu Hanif Muhammad Syarubany 与 Chang D. Yoo 提出。它把 EquiBot 中用于轮式机械臂的
    SIM(3)-等变 Vector Neuron Network（VNN）编码器扩展到 43 自由度的 Unitree G1 人形机器人，替换 3D Diffusion Policy（DP3）原有的 PointNet 式编码器。核心贡献是在低数据量下显著提升成功率：5-10
    条演示时达到 67.1%，而四个非等变基线仅为 38.2-52.4%。
  ko: Visuomotor policies for humanoid loco-manipulation must generalize across object poses and lighting from only a handful
    of demonstrations. 3D Diffusion Policy (DP3) conditions a diffusion-based action generator on point-cloud features, but
    its PointNet-style encoder has no built-in equivariance to the rotations, translations, and scalings (SIM(3)) that manipulation
    tasks respect. EquiBot closed ...
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
- sim3_equivariance
- diffusion_policy
- point_cloud_encoder
- data_efficiency
- behavior_cloning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.36575);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.36575 EquivDP3: A SIM(3)-Invariant Point-Cloud Encoder for Data-Efficient Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2609.36575
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

人形机器人的视觉运动策略需要在仅有少量演示的条件下泛化到不同的物体位姿与光照，而 3D Diffusion Policy（DP3）所用的 PointNet 式点云编码器并不内建对旋转、平移与缩放（SIM(3)）的等变性。EquiBot 曾用 SIM(3)-等变 Vector Neuron Network（VNN）编码器为轮式机械臂解决这一问题，本文则将其推广到结构复杂得多的 43 关节 Unitree G1 人形机器人。EquivDP3 采用两阶段结构：高层扩散规划器配备 SIM(3)-等变 VNN 编码器，以 6 Hz 输出全身指令块，再由冻结的预训练 RL 运动策略与手臂微分逆运动学模块以 50 Hz 执行，整体通过行为克隆端到端训练。在 IsaacLab 的两个仿真基准与四个非等变基线上，其优势集中在低数据区间，且额外延迟仅 0.8 ms。

## 核心内容

### 问题背景
人形移动操作（loco-manipulation）的视觉运动策略需要从极少量演示中泛化到新的物体位姿与光照条件。3D Diffusion Policy（DP3）以点云特征为条件驱动扩散式动作生成器，但其 PointNet 式编码器不具备对操作任务所遵循的旋转、平移与缩放（SIM(3)）的等变性。EquiBot 已用 SIM(3)-等变 Vector Neuron Network（VNN）编码器为轮式机械臂弥补这一缺口，本文将其扩展到更复杂的本体。

### 方法
- 本体：43 关节的 Unitree G1 人形机器人。
- 提出 EquivDP3，一个两阶段策略：
  - 高层扩散规划器搭载 SIM(3)-等变 VNN 编码器，输出 6 Hz 的全身指令块（whole-body command chunks）。
  - 底层由冻结的预训练 RL 运动策略与手臂的微分逆运动学（differential inverse-kinematics）模块以 50 Hz 执行。
- 整体通过行为克隆（behavior cloning）端到端训练。

### 实验设置
- 在两个仿真 IsaacLab 基准上进行评估。
- 对比四个非等变基线。
- 演示数量覆盖 5-100 条，并区分分布内与分布外情形。
- 另设仅本体感觉（proprioception-only）的对照实验，用于检验性能差距是否确实来自感知。

### 关键结果
- 优势集中在低数据区间：5-10 条演示时 EquivDP3 成功率为 67.1%，基线为 38.2-52.4%。
- 到 50-100 条演示时，各编码器收敛至 74.3-85.2%，排序不再具有意义。
- 仅本体感觉对照：移除点云后，5 条演示时成功率降至 31%（EquivDP3 为 60%），10 条演示时为 78%（EquivDP3 为 99%），但到 50-100 条时差距消失，说明高数据平台期反映的是基准上限，而非五种编码器学到了相同的等变性。
- 相比被替换的 PointNet 编码器，该编码器每个动作块仅增加 0.8 ms 延迟。

### 结论
将几何对称性嵌入分层扩散策略的感知主干，是在演示稀缺时提升人形移动操作数据效率的一种实用且几乎零成本的方式。

## Overview

Visuomotor policies for humanoid loco-manipulation must generalize across object poses and lighting from only a handful of demonstrations. 3D Diffusion Policy (DP3) conditions a diffusion-based action generator on point-cloud features, but its PointNet-style encoder has no built-in equivariance to the rotations, translations, and scalings (SIM(3)) that manipulation tasks respect. EquiBot closed this gap for wheeled manipulators with a SIM(3)-equivariant Vector Neuron Network (VNN) encoder. We extend this to a substantially more complex embodiment, the 43-joint Unitree G1 humanoid, and propose EquivDP3: a two-stage policy where a high-level diffusion planner with a SIM(3)-equivariant VNN encoder emits 6 Hz whole-body command chunks, executed at 50 Hz by a frozen, pre-trained RL locomotion policy and a differential inverse-kinematics module for the arms, trained end-to-end by behavior cloning. Across two simulated IsaacLab benchmarks and four non-equivariant baselines (5-100 demonstrations, in- and out-of-distribution), EquivDP3's advantage concentrates in the low-data regime: at 5-10 demonstrations it reaches 67.1% success versus 38.2-52.4% for the baselines, while by 50-100 all encoders converge (74.3-85.2%) and the ordering is no longer meaningful. A proprioception-only control confirms this gap is genuinely perceptual: with the point cloud removed, success drops to 31% vs. 60% (EquivDP3) at 5 demonstrations and 78% vs. 99% at 10, but vanishes by 50-100, showing the high-data plateau reflects a benchmark ceiling, not five encoders learning the same invariance. The encoder costs only 0.8 ms of extra latency per action chunk over the PointNet encoder it replaces. Baking geometric symmetry into a hierarchical diffusion policy's perception backbone is a practical, nearly free way to improve data efficiency for humanoid loco-manipulation when demonstrations are scarce.

## 参考
- https://arxiv.org/abs/2609.36575
