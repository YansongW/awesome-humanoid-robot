---
$id: ent_paper_yang_zero_hlm_generalizable_humanoi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data'
  zh: 'Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data'
  ko: 'Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data'
summary:
  en: Learning generalizable humanoid loco-manipulation remains bottlenecked by costly real-world demonstrations. Simulation
    provides a scalable alternative, but requires visually faithful, physics-ready scenes and executable whole-body motions.
    We present Zero-HLM, a real-to-sim-to-real framework that transforms smartphone captures and simulated source demonstrations
    into scalable training data for ...
  zh: Zero-HLM 是一个 real-to-sim-to-real 框架，可将智能手机拍摄画面与仿真源演示转化为人形机器人 loco-manipulation 的可扩展训练数据。作者提出高斯引导的智能体式 real-to-sim 重建与运动-环境协同自适应机制，生成
    4,800 条通过物理校验的演示。在三个 Unitree G1 任务上，仿真训练的 GR00T N1.7 实现 66.7% 平均全任务成功率，高于真实数据训练的 46.7%。
  ko: Learning generalizable humanoid loco-manipulation remains bottlenecked by costly real-world demonstrations. Simulation
    provides a scalable alternative, but requires visually faithful, physics-ready scenes and executable whole-body motions.
    We present Zero-HLM, a real-to-sim-to-real framework that transforms smartphone captures and simulated source demonstrations
    into scalable training data for ...
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
- real_to_sim_to_real
- sim_to_real_transfer
- gaussian_splatting
- whole_body_control
- zero_shot_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.35075);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.35075 Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data'
  url: https://arxiv.org/abs/2610.35075
  date: '2026-10-26'
  accessed_at: '2026-11-02'
---

## 概述

人形机器人 loco-manipulation 的泛化学习受制于昂贵的真实世界演示数据，而仿真虽可扩展，却需要视觉逼真、物理可用的场景与可执行全身运动。Zero-HLM 通过 real-to-sim-to-real 流程解决这一瓶颈：利用高斯引导的智能体式重建对齐视觉与物理场景，并通过 rollout 反馈进行运动-环境协同自适应，修正全身参考与交互几何。基于该流程生成 4,800 条物理校验演示，在三个 Unitree G1 任务上实现零样本迁移。仿真训练的 GR00T N1.7 平均全任务成功率达 66.7%，优于真实数据训练的 46.7%；在泛化配置下，扩展仿真训练将汇总成功率从真实数据基线策略的 23% 提升至 69%，且无需额外真实演示。

## 核心内容

### 问题背景
人形机器人 loco-manipulation 的泛化能力受限于真实世界演示数据的高昂成本。仿真提供了可扩展的替代方案，但前提是场景在视觉上忠实、在物理上可用，并且全身运动可执行。Zero-HLM 旨在打通从真实场景到仿真再到真实部署的完整数据生成与迁移链路。

### 方法
- **real-to-sim 重建**：采用高斯引导的智能体式（agentic）重建流程，将智能手机拍摄画面转化为仿真场景，并对齐视觉与物理属性。
- **运动-环境协同自适应**：利用 rollout 反馈修正全身运动参考与交互几何，使生成的运动在仿真中物理可执行。
- **数据生成**：基于上述流程生成 4,800 条通过物理校验的演示，用于人形机器人 loco-manipulation 训练。

### 实验设置
- 平台：Unitree G1 人形机器人。
- 任务：三个 loco-manipulation 任务，采用零样本迁移评估。
- 策略模型：GR00T N1.7。
- 对比条件：仿真数据训练 vs. 真实数据训练；基础训练 vs. 扩展仿真训练。

### 关键结果
- 仿真训练的 GR00T N1.7 平均全任务成功率为 66.7%，真实数据训练为 46.7%。
- 在泛化配置下，扩展仿真训练将汇总成功率从基础训练真实数据策略的 23% 提升至 69%，且未使用额外真实演示。

### 结论
Zero-HLM 表明，借助视觉与物理对齐的 real-to-sim 重建以及运动-环境协同自适应，仅依靠仿真生成的数据即可支撑人形机器人 loco-manipulation 的零样本迁移，并在泛化配置上显著优于真实数据训练的策略。

## Overview

Learning generalizable humanoid loco-manipulation remains bottlenecked by costly real-world demonstrations. Simulation provides a scalable alternative, but requires visually faithful, physics-ready scenes and executable whole-body motions. We present Zero-HLM, a real-to-sim-to-real framework that transforms smartphone captures and simulated source demonstrations into scalable training data for humanoid loco-manipulation. Gaussian-guided agentic real-to-sim reconstruction aligns visual and physical scenes; motion-environment co-adaptation uses rollout feedback to correct whole-body references and interaction geometry. We generate 4,800 physically validated demonstrations for zero-shot transfer across three Unitree G1 tasks. Simulation-trained GR00T N1.7 achieves 66.7% mean full-task success, versus 46.7% with real-data training. On generalized configurations, expanded simulation training raises pooled success from 23% for base-trained real-data policies to 69%, without additional real demonstrations. Project page: https://young-bit.github.io/zero-hlm/

## 参考
- https://arxiv.org/abs/2610.35075
