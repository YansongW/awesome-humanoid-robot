---
$id: ent_paper_lee_echo_in_the_steps_learning_per_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory'
  zh: 'Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory'
  ko: 'Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory'
summary:
  en: While recent advances in perceptive locomotion have enabled humanoid robots to traverse structured terrains, agile parkour
    in highly discontinuous environments remains an open challenge. In particular, crossing sparse footholds and narrow support
    regions requires precise foothold selection, effective use of visual observations, and consistent alternating foot placement
    during fast transitions. In ...
  zh: 本文提出了一套感知式人形机器人跑酷框架，由 Ming-Ju Lee、Zizhuo Wang、Shaoting Zhu、Haozhe Lou、Hang Zhao、Yiming Li 等人完成，旨在解决高不连续地形中落脚点稀疏、支撑区域狭窄的敏捷穿越难题。该框架仅依赖机载深度观测，核心是结合显著性先验与门控记忆的显著性引导时序感知模块，并通过交替损失实现对称性正则化以鼓励交替步态。实验表明该方法在仿真与真实世界中均显著提升了挑战性地形上的成功率与落脚精度。
  ko: While recent advances in perceptive locomotion have enabled humanoid robots to traverse structured terrains, agile parkour
    in highly discontinuous environments remains an open challenge. In particular, crossing sparse footholds and narrow support
    regions requires precise foothold selection, effective use of visual observations, and consistent alternating foot placement
    during fast transitions. In ...
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
- humanoid_parkour
- perceptive_locomotion
- gated_memory
- saliency_prior
- foothold_selection
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.28960);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.28960 Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory'
  url: https://arxiv.org/abs/2609.28960
  date: '2026-09-24'
  accessed_at: '2026-09-28'
---

## 概述

针对人形机器人在高度不连续环境中进行敏捷跑酷这一尚未解决的难题，本文提出了一个感知式人形跑酷框架，使机器人仅凭机载深度观测即可在落脚点有限的地形上稳定穿越。框架的关键设计是显著性引导的时序感知模块，它将显著性先验与门控记忆相结合，从而跨帧保留有信息量的深度特征，使机器人能够从部分观测中可靠地完成落脚。此外，作者引入交替损失作为对称性正则化手段，鼓励形成交替步态模式，提升穿越的鲁棒性。大量实验显示，该方法在仿真和真实世界的挑战性地形上均显著提高了成功率与落脚点精度。

## 核心内容

### 问题背景
感知式运动控制虽已使人形机器人能够穿越结构化地形，但在高度不连续的环境中实现敏捷跑酷仍是开放挑战。跨越稀疏落脚点与狭窄支撑区域，要求机器人具备精确的落脚点选择能力、对视觉观测的有效利用，以及在快速转换过程中保持一致的左右脚交替落足。

### 方法
- **整体框架**：一个感知式人形跑酷框架，仅使用机载深度观测，即可在落脚点可用性受限的地形上实现稳定穿越。
- **显著性引导的时序感知模块**：将显著性先验与门控记忆结合，跨帧保留有信息量的深度特征，从而在仅有部分观测的情况下实现可靠的落脚。
- **交替损失**：作为对称性正则化引入，用于鼓励交替步态模式，并提升穿越鲁棒性。

### 实验与结果
作者在仿真与真实世界中开展了大量实验。结果表明，该方法在挑战性地形上显著提升了成功率与落脚点精度。

### 结论
通过显著性引导的时序感知与门控记忆，以及交替损失带来的对称性正则化，该框架能够在仅依赖机载深度观测的条件下，提升人形机器人在稀疏落脚点与狭窄支撑地形上的跑酷表现。

## Overview

While recent advances in perceptive locomotion have enabled humanoid robots to traverse structured terrains, agile parkour in highly discontinuous environments remains an open challenge. In particular, crossing sparse footholds and narrow support regions requires precise foothold selection, effective use of visual observations, and consistent alternating foot placement during fast transitions. In this paper, we present a perceptive humanoid parkour framework that enables stable traversal across terrains with limited foothold availability using only onboard depth observations. The framework features a saliency-guided temporal perception module that combines a saliency prior with gated memory. It retains informative depth features across frames, enabling reliable foot placement from partial observations. By introducing an alternation loss, our symmetry regularization encourages alternating gait patterns and improves traversal robustness. Extensive experiments show that our method significantly improves success rate and foothold accuracy on challenging terrains in both simulation and the real world.

## 参考
- https://arxiv.org/abs/2609.28960
