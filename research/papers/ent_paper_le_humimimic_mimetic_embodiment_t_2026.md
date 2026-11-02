---
$id: ent_paper_le_humimimic_mimetic_embodiment_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumiMimic: Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos'
  zh: 'HumiMimic: Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos'
  ko: 'HumiMimic: Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos'
summary:
  en: Enabling a humanoid to interact naturally with human partners requires preserving not only individual motions but also
    the spatial, semantic, and contact relationships underlying the interaction (i.e., hugging, dancing, hand-shaking, etc.).
    Furthermore, a practical solution should generalize across various humanoid embodiments with distinct morphologies and
    kinematic constraints. To tackle this ...
  zh: HumiMimic 工作提出 HumiTransfer 框架，将野外拍摄的人-人交互视频转换为物理合理的人-人形机器人交互动作，在保留空间、语义与接触关系的同时适配不同形态的人形本体。作者将其应用于 1,200 段野外视频，为 26
    自由度的 Unitree R1 Edu 与 23 自由度的 HighTorque Mini-hi 生成约 50 万帧数据，构建 HumiMimic 数据集，并在真实机器人上验证了动作的可执行性。
  ko: Enabling a humanoid to interact naturally with human partners requires preserving not only individual motions but also
    the spatial, semantic, and contact relationships underlying the interaction (i.e., hugging, dancing, hand-shaking, etc.).
    Furthermore, a practical solution should generalize across various humanoid embodiments with distinct morphologies and
    kinematic constraints. To tackle this ...
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
- human_humanoid_interaction
- motion_retargeting
- embodiment_transfer
- motion_generation
- in_the_wild_videos
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.36615);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.36615 HumiMimic: Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos'
  url: https://arxiv.org/abs/2610.36615
  date: '2026-10-27'
  accessed_at: '2026-11-02'
---

## 概述

人形机器人与人类自然交互，不仅需要复现单个动作，还要保留拥抱、跳舞、握手等交互背后的空间、语义与接触关系，并且要能迁移到形态与运动学约束各异的本体上。为此作者提出 HumiTransfer，一个模仿式本体迁移框架：先重建具有一致足-地接触的三维人体运动，再通过交互建模将其中一方参与者迁移到目标人形本体，迁移中使用加权关节相对方向与解剖学偏移来优先保持对交互关键的躯体间关系，随后用重定向后优化保证平衡、接触与避碰。作者将该框架应用于 1,200 段野外视频，为 26 自由度的 Unitree R1 Edu 和 23 自由度的 HighTorque Mini-hi 生成约 50 万帧多样化交互数据，形成 HumiMimic 数据集。实验显示其在两款机器人上的运动保真度、躯体间关系保持与接触精度均优于现有基线，且该数据集可支撑以人类伙伴为条件的交互动作生成方法，真实机器人部署也验证了迁移动作的物理可执行性。

## 核心内容

### 问题背景
人形机器人与人类伙伴自然交互，难点不止在于复现单个人的动作，还在于保留交互本身所依赖的空间、语义与接触关系（如拥抱、跳舞、握手）。同时，实际方案需要能泛化到形态与运动学约束各不相同的多种人形本体。现有动作重定向方法通常针对单人运动，难以兼顾交互中的躯体间关系。

### 方法
作者提出 HumiTransfer，一个模仿式本体迁移框架，将野外拍摄的人-人交互视频转换为物理合理的人-人形机器人交互：

- **三维人体运动重建**：从视频重建人体运动，并保持一致的足-地接触。
- **交互建模与本体迁移**：将交互中的一方参与者迁移到目标人形本体，采用加权关节相对方向与解剖学偏移，优先保持对交互关键的躯体间关系。
- **重定向后优化**：在迁移之后施加优化，保证平衡、接触与避碰。

### 实验设置与数据
- 将 HumiTransfer 应用于 1,200 段野外视频。
- 目标本体为 26 自由度的 Unitree R1 Edu 与 23 自由度的 HighTorque Mini-hi 人形机器人。
- 生成约 500,000 帧多样化交互数据，构成 HumiMimic 数据集。

### 关键结果
- 在两款机器人上，与现有基线相比，HumiTransfer 取得更高的运动保真度，更好地保持躯体间关系，并维持接触精度。
- HumiMimic 可支撑动作生成方法，用于合成跟随人类伙伴的交互式人形动作。
- 真实机器人部署验证了迁移动作在真实环境中的物理可执行性。

### 结论
HumiTransfer 能够从野外人-人交互视频中迁移出物理合理、保留交互关系且适配不同人形本体的动作，HumiMimic 数据集为交互式人形动作生成提供了数据基础，并在真实机器人上得到验证。

## Overview

Enabling a humanoid to interact naturally with human partners requires preserving not only individual motions but also the spatial, semantic, and contact relationships underlying the interaction (i.e., hugging, dancing, hand-shaking, etc.). Furthermore, a practical solution should generalize across various humanoid embodiments with distinct morphologies and kinematic constraints. To tackle this challenge, we propose HumiTransfer, a mimetic embodiment transfer framework that converts in-the-wild human-human interaction videos into physically plausible human-humanoid interactions. HumiTransfer first reconstructs 3D human motion with consistent foot-ground contact, then transfers one participant to a target humanoid embodiment via interaction modeling, using weighted joint-relative directions and anatomical offsets to prioritize interaction-critical inter-body relationships, while post-retargeting optimization enforces balance, contact, and collision avoidance. Subsequently, we apply HumiTransfer to 1,200 in-the-wild videos, producing approximately 500,000 frames of diverse interactions for the 26-DoF Unitree R1 Edu and the 23-DoF HighTorque Mini-hi humanoid robot, resulting in our HumiMimic dataset. Across both robots, HumiTransfer achieves superior motion fidelity, preserves inter-body relationships, and maintains contact accuracy compared with existing baselines. Moreover, we demonstrate that HumiMimic supports motion generation methods for synthesizing interactive humanoid motions following a human partner. Finally, our real robot deployments confirm the physical executability of the transferred motions in real-world settings. Our project is available at https://aioznetwork.github.io/HumiMimic/

## 参考
- https://arxiv.org/abs/2610.36615
