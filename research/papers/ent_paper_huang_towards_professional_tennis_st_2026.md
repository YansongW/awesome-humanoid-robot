---
$id: ent_paper_huang_towards_professional_tennis_st_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking
  zh: Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking
  ko: Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking
summary:
  en: Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional
    motion styles while maintaining strong task performance remains challenging. In this work, we propose AdaPT, an Adaptive
    Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from broadcast
    videos. This hierarchical design ...
  zh: AdaPT是一个自适应运动规划与跟踪框架，用于让仿人机器人从广播视频中学习专业网球发球和回合风格。该框架由Tao Huang等人提出，通过分层设计和运动速度适配器解决仿真到现实的差距，并在Unitree G1和全尺寸Dobot Atom仿人机器人上验证了有效性。
  ko: Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional
    motion styles while maintaining strong task performance remains challenging. In this work, we propose AdaPT, an Adaptive
    Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from broadcast
    videos. This hierarchical design ...
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
- humanoid_robotics
- adaptive_motion_planning
- sim_to_real
- tennis_skills
- motion_tracking
- style_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.20087);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2608.20087 Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking
  url: https://arxiv.org/abs/2608.20087
  date: '2026-08-20'
  accessed_at: '2026-08-24'
---

## 概述

AdaPT框架的核心洞察是分层设计：规划器生成风格化的运动学轨迹，而跟踪器以最小干扰执行这些轨迹。尽管在仿真中有效，但现实机器人上跟踪性能会退化，且自回归规划部分忽视此退化，噪声感知进一步加剧问题。为此，自适应机制通过学习跟踪随机化执行速度来提升鲁棒性，并让规划器基于学习到的运动速度适配器来缓解复合误差。真实世界实验在Unitree G1上证明了该机制能弥合仿真到现实的差距，并在全尺寸Dobot Atom（1.7米）上实现了无需动作捕捉的野外发球。

## 核心内容

### 问题背景
仿人机器人在真实球类运动中已展现潜力，但实现专业运动风格同时保持强任务性能仍是挑战。现有方法通常难以从人类演示中提取风格化动作，且仿真到现实的迁移常因跟踪退化而失败。

### 方法
AdaPT采用分层架构：
- **规划器**：从广播视频中学习专业网球发球和回合的风格化运动学轨迹，生成具有人类风格的关节运动。
- **跟踪器**：执行规划轨迹，并设计为对规划干扰最小化。
- **自适应机制**：针对仿真到现实差距，跟踪器学习跟踪随机化执行速度以增强鲁棒性；规划器则通过运动速度适配器（motion-speed adapter）调整生成速度，以缓解自回归规划中的复合误差。

### 实验设置与结果
- **仿真实验**：验证了分层设计的有效性，但暴露了跟踪性能在现实中的退化问题。
- **真实世界实验**：
  - 在Unitree G1上测试，自适应机制显著提升了跟踪鲁棒性，弥合了仿真到现实的差距。
  - 在Dobot Atom（1.7米全尺寸）上部署AdaPT策略，实现了无需动作捕捉的野外发球。
- **关键洞察**：实验揭示了算法和工程层面的见解，为未来仿人机器人球类系统提供指导。

### 结论
AdaPT通过自适应运动规划与跟踪，成功将专业网球风格迁移到真实仿人机器人，并解决了仿真到现实的关键瓶颈。代码和视频已公开。

## Overview

Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional motion styles while maintaining strong task performance remains challenging. In this work, we propose AdaPT, an Adaptive Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from broadcast videos. This hierarchical design is motivated by the key insight that the planner generates stylistic kinematic motions, while the tracker executes them with minimal interference with planning. Despite its effectiveness in simulation, a substantial sim-to-real gap emerges: tracking performance inevitably degrades on real robots, and this degradation is partially overlooked by autoregressive planning and further compounded by noisy perception. To address these issues, our adaptation mechanism improves tracking robustness by learning to track randomized execution speeds, while conditioning the planner on a learned motion-speed adapter to mitigate compounding errors. Real-world experiments on the Unitree G1 demonstrate the effectiveness of our adaptation mechanism in bridging the sim-to-real gap. We further deploy AdaPT policies on the full-size Dobot Atom humanoid robot (1.7m) and demonstrate in-the-wild serving without motion capture. Beyond these results, our real-world experiments reveal both algorithmic and engineering insights for future humanoid ball-sports systems. Videos and code are available on our \href{https://humanoidtennis.github.io/AdaPT/}{project website}.

## 参考
- https://arxiv.org/abs/2608.20087
