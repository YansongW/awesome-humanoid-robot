---
$id: ent_paper_sun_dexweave_learning_dexterous_hu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexWeave: Learning Dexterous Humanoid Loco-Manipulation from Human Demonstrations'
  zh: 'DexWeave: Learning Dexterous Humanoid Loco-Manipulation from Human Demonstrations'
  ko: 'DexWeave: Learning Dexterous Humanoid Loco-Manipulation from Human Demonstrations'
summary:
  en: Learning dexterous humanoid loco-manipulation from human demonstrations requires transferring not only human motion,
    but also the coordinated interaction structure underlying the demonstrated behavior. This is challenging because embodiment
    differences distort the coupling among body motion, wrist placement, finger articulation, and object interaction, while
    kinematically accurate references may ...
  zh: DexWeave 是一个统一框架，用于从人类演示中学习人形机器人的灵巧全身移动操作，由 Naichuan Sun、Haotian Shen、Yizhang Zhang、Luying Feng、Haoze Wang、Yuanbo Xiangli、Yaochu
    Jin、Peidong Liu 提出。该框架将交互一致的运动重定向与解剖结构感知的全身策略学习相连接，在重定向保真度、交互一致性和操作性能上优于 MLP 基线，并加快了策略收敛。作者进一步在配备 Inspire 灵巧手的 Unitree
    G1 实体人形机器人上部署了所学策略，实现了真实世界中的灵巧全身移动操作。
  ko: Learning dexterous humanoid loco-manipulation from human demonstrations requires transferring not only human motion,
    but also the coordinated interaction structure underlying the demonstrated behavior. This is challenging because embodiment
    differences distort the coupling among body motion, wrist placement, finger articulation, and object interaction, while
    kinematically accurate references may ...
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
- motion_retargeting
- dexterous_manipulation
- whole_body_control
- reinforcement_learning
- transformer_policy
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.34724);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.34724 DexWeave: Learning Dexterous Humanoid Loco-Manipulation from Human Demonstrations'
  url: https://arxiv.org/abs/2609.34724
  date: '2026-09-28'
  accessed_at: '2026-10-05'
---

## 概述

从人类演示中学习人形机器人的灵巧移动操作，不仅需要迁移人体运动，还需要迁移演示行为背后的协调交互结构。由于不同本体之间的差异会扭曲身体运动、手腕位置、手指关节运动与物体交互之间的耦合关系，这一任务颇具挑战；同时，运动学上准确的参考在机器人动力学下也可能难以实现。为此，作者提出 DexWeave，将交互一致的运动重定向与解剖结构感知的全身策略学习统一起来。该框架先通过两阶段重定向，用专用求解器初始化身体与手部运动，再在上肢交互链上进行耦合细化并保持下肢支撑。所得参考由解剖结构感知的 Transformer 策略跟踪，该策略将解剖区域表示为结构化 token，并用有向掩码注意力建模其依赖关系，同时让物体信息选择性地调节上肢通路。策略直接通过强化学习训练，联合输出身体与灵巧手动作，无需预训练跟踪策略、师生蒸馏或后续残差细化。

## 核心内容

### 问题背景
从人类演示中学习人形机器人的灵巧移动操作，难点在于不仅要迁移人体运动本身，还要迁移演示行为中隐含的协调交互结构。不同本体之间的差异会扭曲身体运动、手腕位置、手指关节运动与物体交互之间的耦合关系；此外，即使参考动作在运动学上是准确的，在机器人动力学约束下也可能难以真正实现。

### 方法
DexWeave 是一个统一框架，将交互一致的运动重定向与解剖结构感知的全身策略学习连接起来，包含两个主要部分：

- **两阶段重定向**：先用专用求解器分别初始化身体与手部运动，随后在上肢交互链上进行耦合细化，同时保持下肢支撑，从而得到交互一致的参考动作。
- **解剖结构感知策略**：采用 Transformer 策略跟踪上述参考，将解剖区域表示为结构化 token，并通过有向掩码注意力建模各区域之间的依赖关系；物体信息被选择性地用于调节上肢通路，以支持灵巧交互。
- **训练方式**：策略联合输出身体动作与灵巧手动作，直接使用强化学习训练，不依赖预训练跟踪策略、师生蒸馏，也不需要后续的残差细化。

### 关键结果
- 与 MLP 基线相比，DexWeave 提升了重定向保真度与交互一致性。
- 在操作性能上优于 MLP 基线，并实现了更快的策略收敛。
- 作者将学习到的策略部署在配备 Inspire 灵巧手的 Unitree G1 实体人形机器人上，在真实世界中展示了灵巧的全身移动操作。

### 结论
DexWeave 通过将交互一致的重定向与解剖结构感知的全身策略学习相结合，为从人类演示中学习人形机器人灵巧移动操作提供了一条统一路径，并在真实硬件上验证了其可行性。项目页面为 https://dexweave.github.io ，可查看视频。

## Overview

Learning dexterous humanoid loco-manipulation from human demonstrations requires transferring not only human motion, but also the coordinated interaction structure underlying the demonstrated behavior. This is challenging because embodiment differences distort the coupling among body motion, wrist placement, finger articulation, and object interaction, while kinematically accurate references may still be difficult to realize under robot dynamics. We present DexWeave, a unified framework that connects interaction-consistent motion retargeting with anatomy-aware whole-body policy learning. DexWeave first employs a two-stage retargeting procedure that initializes body and hand motions with specialized solvers and subsequently performs coupled refinement over the upper-body interaction chain while preserving lower-body support. The resulting references are tracked by an anatomy-aware Transformer policy that represents anatomical regions as structured tokens and uses directed masked attention to model their dependencies, with object information selectively conditioning the upper-body pathway for dexterous interaction. The policy jointly outputs body and dexterous-hand actions and is trained directly with reinforcement learning, without pretrained tracking policies, teacher-student distillation, or subsequent residual refinement. DexWeave improves retargeting fidelity and interaction consistency while achieving higher manipulation performance and faster policy convergence than MLP baselines. We further deploy the learned policies on a physical Unitree G1 humanoid equipped with Inspire dexterous hands, demonstrating dexterous whole-body loco-manipulation in the real world. See our project page (https://dexweave.github.io) for videos.

## 参考
- https://arxiv.org/abs/2609.34724
