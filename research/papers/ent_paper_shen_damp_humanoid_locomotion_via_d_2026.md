---
$id: ent_paper_shen_damp_humanoid_locomotion_via_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors'
  zh: 'DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors'
  ko: 'DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors'
summary:
  en: Humanoid robots possess the structural capability to traverse complex terrains. However, achieving stable t raversal
    without relying on perceived information remains challenging, particularly in complex environments. This paper introduces
    DAMP, a reinforcement learning framework aimed at achieving robust and naturalistic humanoid locomotion over challenging
    terrains, with the assumption that no ...
  zh: DAMP 是一个面向人形机器人的强化学习框架，由 Puying Shen、Wenhao Cui、Huaxing Huang、Bangyu Qin、Shengtao Li、Ziyang Dong、Guoteng Zhang 提出，目标是在不依赖感知信息的假设下实现复杂地形上的稳定且自然的行走。该框架利用循环神经网络捕捉时序依赖，并隐式推断特权信息及其他与任务相关的潜在信息，通过将所学表示与任务目标对齐来实现鲁棒且目标一致的运动策略学习。该端到端框架完成了从仿真到真实环境的迁移学习，验证了方法的鲁棒性与泛化能力。
  ko: Humanoid robots possess the structural capability to traverse complex terrains. However, achieving stable t raversal
    without relying on perceived information remains challenging, particularly in complex environments. This paper introduces
    DAMP, a reinforcement learning framework aimed at achieving robust and naturalistic humanoid locomotion over challenging
    terrains, with the assumption that no ...
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
- humanoid_locomotion
- reinforcement_learning
- recurrent_neural_networks
- sim_to_real_transfer
- adversarial_motion_priors
- legged_robotics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.11505);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.11505 DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors'
  url: https://arxiv.org/abs/2610.11505
  date: '2026-10-08'
  accessed_at: '2026-10-12'
---

## 概述

人形机器人具备穿越复杂地形的结构条件，但在没有感知信息可用的前提下实现稳定穿越仍然困难，尤其是在复杂环境中。为此，作者提出 DAMP，一个以无感知信息为假设前提的强化学习框架，用于在挑战性地形上实现鲁棒且自然的类人行走。该框架借助循环神经网络捕捉时序依赖，并隐式推断特权信息以及其他与任务相关的潜在信息。通过将学习到的表示与任务目标对齐，方法能够实现鲁棒且与目标一致的运动策略学习。整个框架为端到端形式，并实现了从仿真到真实环境的迁移学习，展示了所提方法的鲁棒性与泛化能力。

## 核心内容

### 问题背景

人形机器人在结构上具备穿越复杂地形的能力，但在不依赖感知信息的情况下实现稳定穿越仍具挑战，复杂环境中尤为明显。本文针对这一设定展开研究，即假设机器人无法获得感知信息。

### 方法

作者提出 DAMP，一个强化学习框架，用于在挑战性地形上实现鲁棒且自然的类人行走。其核心设计包括：

- 采用循环神经网络捕捉时序依赖，并隐式推断特权信息及其他与任务相关的潜在信息；
- 将学习到的表示与任务目标对齐，从而支持鲁棒且目标一致的运动策略学习；
- 整体为端到端框架，并实现从仿真到真实环境的迁移学习。

### 实验与结果

摘要未给出具体实验设置、对比基线或量化指标。作者报告该端到端框架完成了仿真到真实环境的迁移学习，体现了所提方法的鲁棒性与泛化能力。真实环境演示视频见：https://youtu.be/AkI7TZB2DDM。

### 结论

DAMP 在无感知信息的假设下，通过循环神经网络隐式推断特权与任务相关潜在信息，并将表示与任务目标对齐，实现了复杂地形上鲁棒且自然的类人行走，并成功迁移至真实环境。

## Overview

Humanoid robots possess the structural capability to traverse complex terrains. However, achieving stable t raversal without relying on perceived information remains challenging, particularly in complex environments. This paper introduces DAMP, a reinforcement learning framework aimed at achieving robust and naturalistic humanoid locomotion over challenging terrains, with the assumption that no perceived information is available. The framework leverages recurrent neural networks to capture temporal dependencies and implicitly infer privileged and other task-relevant latent information. By aligning the learned representations with the task objective, the method enables robust and goal-consistent policy learning. This end-to-end framework achieves transfer learning from simulation to real-world environments, demonstrating the proposed method's robustness and generalization capabilities. The video of the real-world demonstration can be found at the following link: https://youtu.be/AkI7TZB2DDM.

## 参考
- https://arxiv.org/abs/2610.11505
